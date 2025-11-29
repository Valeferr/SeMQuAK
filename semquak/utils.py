from urllib.parse import urlparse
import pandas as pd
import re
from pathlib import Path
import sys
from datetime import datetime
from rdflib import XSD, Graph, Literal, URIRef

from config.errors import ERROR_DEFINITIONS, SPECIAL_MAPPING
from config.namespaces import ERROR

INVALID_VALUES = {
        "none", "nan", "null","", "-", "absent", "[]", "{}",
        "void file absent", "\"\"", "''", " ", "[\'\']", "[\'\'. \'\']", "[, ]"
}

BOOLEAN_TRUE = {"true", "1", "yes", "on"}
BOOLEAN_FALSE = {"false", "0", "no", "off"}

DATETIME_FORMATS = [
    "%Y-%m-%d",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%S.%f",
]

RE_DECIMAL_COMMA = re.compile(r'^[+-]?\d+,\d+(?:[eE][+-]?\d+)?$')
RE_KG_ID_CHARS = re.compile(r'[^a-zA-Z0-9_\-]')
RE_MULTI_DASH = re.compile(r'-+')
RE_MULTI_UNDERSCORE = re.compile(r'_+')
RE_MATCH_ERROR = re.compile(r'\b([45]\d{2})\b')
INVALID_URI_CHARS = {' ', '<', '>', '\"', '{', '}', '|', '\\', '^', '`', '\’'}

CONFIG_FILE = Path("config/metrics.py")
added_metrics = set()

def extract_timestamp_from_filename(filename: str) -> datetime:
    """
    Estrae la data dal nome del file CSV.
    """
    name = Path(filename).stem
    try:
        parts = name.split("-")
        return datetime(int(parts[0]), int(parts[1]), int(parts[2]))
    except (ValueError, IndexError) as e:
        print(f"Impossibile estrarre data dal filename: {filename}. Errore: {e}")
        raise

def clean_value(value: object) -> str | None:
    """
    Pulisce un valore dai casi invalidi e normalizza separatori decimali.
    """
    if value is None or pd.isna(value):
        return None
    
    s = str(value).strip()
    if s.lower() in INVALID_VALUES:
        return None
    
    if RE_DECIMAL_COMMA.match(s):
        s = s.replace(",", ".")

    return s.replace("\"\"", "").replace("''", "")

def normalize_string(v: any) -> str:
    """
    Normalizza una stringa per il confronto.
    """
    if v is None:
        return ""
    return str(v).strip().replace("'", '"').replace(" ", "")

def validate_datatype(value: object, datatype: XSD) -> Literal | URIRef | None:
    """
    Converte un valore stringa in un Literal RDF con tipo corretto.
    Gestisce integer, decimal, boolean, dateTime, URI.
    """
    s = clean_value(value)
    if s is None:
        return None
    
    try:
        if datatype == XSD.anyURI:
            return URIRef(s) if is_valid_uri(s) else None
            
        elif datatype == XSD.integer:
                s = s.split(".")
                return Literal(int(s[0]), datatype=XSD.integer)
            
        elif datatype in (XSD.decimal, XSD.double):
                return Literal(float(s), datatype=datatype) 
            
        elif datatype == XSD.boolean:
            sl = s.lower()
            if sl in BOOLEAN_TRUE:
                return Literal("True", datatype=XSD.boolean)
            elif sl in BOOLEAN_FALSE:
                return Literal("False", datatype=XSD.boolean)
            else:
                return None
            
        elif datatype == XSD.dateTime:
            for fmt in DATETIME_FORMATS:
                try:
                    dt = datetime.strptime(s, fmt)
                    return Literal(dt.isoformat(), datatype=XSD.dateTime)
                except ValueError:
                    continue
            print(f"Formato data non riconosciuto per: {s}")
            return None
        
    except ValueError:
        return None
    
    return Literal(s, datatype=XSD.string)

def clean_identifier(s: str) -> str:
    """
    Rimuove caratteri non ammessi negli identificatori RDF.
    """
    return s.replace(' ', '_').replace('.', '_').replace('-', '_').replace('/', '_').replace('(', '').replace(')', '').strip()

def safe_kg_id(kg_id: str) -> str:
    """
    Pulisce un KG ID rimuovendo prefissi URL e caratteri non ammessi.
    """
    if not isinstance(kg_id, str):
        kg_id = str(kg_id)

    kg_id = kg_id.replace("https", "").replace("http", "")
    kg_id = RE_KG_ID_CHARS.sub('_', kg_id)
    kg_id = RE_MULTI_DASH.sub('', kg_id)
    kg_id = RE_MULTI_UNDERSCORE.sub('_', kg_id)
    
    return clean_identifier(kg_id.strip('_'))

def map_http_error(value):
    """
    Mappa gli errori HTTP a URI di errore predefiniti.
    """
    if value is None:
        return None

    str_value = str(value).strip()
    code = None
    match = re.search(RE_MATCH_ERROR, str_value)

    if match:
        found_code = int(match.group(1))
        if found_code in ERROR_DEFINITIONS:
            code = found_code

    elif str_value.lower() in SPECIAL_MAPPING:
        code = SPECIAL_MAPPING[str_value.lower()]

    if code:
        return ERROR[str(code)]
    
    return None

def check_value(value: object) -> URIRef | object:
    cleaned = clean_value(value)
    err_value = map_http_error(value)
    return err_value if err_value else cleaned

def safe_literal(g: Graph, value: object, predicate: URIRef, subject_uri: URIRef, datatype: URIRef = None) -> None:
    """
    Aggiunge una triple con valore validato, gestendo errori e tipi.
    """
    if value is None:
        return

    cleaned = clean_value(value)
    if cleaned is None:
        return

    error_uri = map_http_error(cleaned)
    if error_uri:
        g.add((subject_uri, predicate, error_uri))
        return

    literal = validate_datatype(cleaned, datatype)
    if literal is not None:
        g.add((subject_uri, predicate, literal))
    else:
        print(f"Validazione fallita: '{cleaned}' come {datatype} per {subject_uri}")

def add_new_metric_to_config(metric_name, datatype: str="string", dimension: str="Uncategorized", output_metric: str="", description: str="", access_methods: str="[UN]") -> None:
    """
    Aggiunge una nuova metrica al file metrics.py che non esiste
    """    
    if metric_name in added_metrics:
        return 

    try:
        content = CONFIG_FILE.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File di configurazione non trovato: {CONFIG_FILE}")
        return

    if f'metrics["{metric_name}"]' in content:
        return

    print(f"Metrica sconosciuta rilevata: '{metric_name}'. Aggiorno {CONFIG_FILE}...")
    
    new_entry = (
        f'\t"{metric_name}": {{\n'
        f'\t\t"datatype": XSD.{datatype},\n'
        f'\t\t"access_methods": {access_methods},\n'
        f'\t\t"dimension": "{dimension}",\n'
        f'\t\t"description": "{description}",\n'
        f'\t\t"metric_output": "{output_metric}",\n'
        f'\t}},\n'
    )

    pos = content.rfind("}")
    if pos == -1:
        print("Impossibile trovare la chiusura del dizionario metrics in config.")
        return
    
    new_content = content[:pos] + new_entry + content[pos:]

    CONFIG_FILE.write_text(new_content, encoding="utf-8")
    added_metrics.add(metric_name)
    print(f"Metrica '{metric_name}' aggiunta con successo.")

def is_valid_uri(uri: str) -> bool:
    """
    Controlla se una stringa è un URI valido secondo le regole RDF/Turtle.
    """
    if not isinstance(uri, str) or not uri.strip():
        return False
    
    parsed = urlparse(uri)
    if not (parsed.scheme and parsed.netloc):
        return False

    if any(ch in uri for ch in INVALID_URI_CHARS):
        return False

    return True
