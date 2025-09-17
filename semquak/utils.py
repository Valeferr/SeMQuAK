from urllib.parse import urlparse
import pandas as pd

from datetime import datetime
from rdflib import XSD, Graph, Literal, URIRef

from config.errors import ERROR_DEFINITIONS, special_mapping
from config.namespaces import ERROR

invalid_values = {
        "none", "nan", "null","", "-", "absent", "[]", "{}",
        "void file absent", "\"\"", "''", " ", "[\'\']"
}

BOOLEAN_TRUE = {"true", "1", "yes", "on"}
BOOLEAN_FALSE = {"false", "0", "no", "off"}

DATETIME_FORMATS = [
    "%Y-%m-%d",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%S.%f",
]

def extract_timestamp_from_filename(filename: str) -> datetime:
    """
    Estrae la data dal nome del file CSV.
    """
    filename = filename.replace("dati_prova/", "").replace(".csv", "").split("-")
    return datetime(int(filename[0]), int(filename[1]), int(filename[2]))

def clean_value(value: object) -> str | None:
    """
    Pulisce un valore dai casi invalidi e normalizza separatori decimali.
    """
    if pd.isna(value) or str(value).strip().lower() in invalid_values:
        return None
    s = str(value).strip()
    return s.replace(',', '.')

def validate_datatype(value: object, datatype: XSD) -> Literal | URIRef | None:
    """
    Converte un valore stringa in un Literal RDF con tipo corretto.
    Gestisce integer, decimal, boolean, dateTime, URI.
    """
    s = clean_value(value)
    if s is None:
        return None
    
    if datatype == XSD.anyURI:
        parsed = urlparse(s)
        if parsed.scheme and parsed.netloc:
            return URIRef(s)
        return None
        
    elif datatype == XSD.integer:
        try:
            return Literal(int(s), datatype=XSD.integer)
        except ValueError:
            return None
        
    elif datatype in (XSD.decimal, XSD.double):
        try:
            return Literal(float(s), datatype=datatype) 
        except ValueError:
            return None
        
    elif datatype == XSD.boolean:
        sl = s.lower()
        if sl in BOOLEAN_TRUE:
            return Literal(True, datatype=XSD.boolean)
        elif sl in BOOLEAN_FALSE:
            return Literal(False, datatype=XSD.boolean)
        else:
            return None
        
    elif datatype == XSD.dateTime:
        for fmt in DATETIME_FORMATS:
            try:
                dt = datetime.strptime(s, fmt)
                return Literal(dt.isoformat(), datatype=XSD.dateTime)
            except ValueError:
                continue
        return None
    
    return Literal(s, datatype=XSD.string)

def clean_identifier(s: str) -> str:
    """
    Rimuove caratteri non ammessi negli identificatori RDF.
    """
    return s.replace(' ', '_').replace('.', '_').replace('-', '_').replace('/', '_').replace('(', '').replace(')', '')

def map_http_error(value):
    """
    Mappa stringhe di errore HTTP a URI di errore predefiniti.
    """
    if value.isdigit():
        code = int(value)
        if code in ERROR_DEFINITIONS:
            return ERROR[str(code)]

    code = special_mapping.get(value.lower())
    if code:
        return ERROR[code]

    return None

def safe_literal(g: Graph, value: object, predicate: URIRef, subject_uri: URIRef, datatype: URIRef =None) -> None:
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
        print(f"Warning: Non posso validare '{cleaned}' come {datatype} per {subject_uri} -> {predicate}")
