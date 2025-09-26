from rdflib import Graph, Literal, URIRef
from datetime import datetime
import pandas as pd
import os

from config.metrics import metrics 
from config.profile_attributes import profile_attributes
from config.assessment_attributes import assessment_attributes
from config.namespaces import EX, PROF, QM, DQV, PROV, DCAT, RDFS, RDF, UN, XSD

from semquak.extractors import extract_assessment_values, get_all_assessments_for_kg, get_attribute_value, get_latest_assessment_for_kg
from semquak.helpers import add_categories_and_dimensions_nodes, add_distribution_and_errors_nodes, bind_common_namespaces, get_assessment_uri, get_attribute_uri, get_dimension_uri, get_metric_uri, get_profile_attribute_uri, get_profile_uri, get_quality_measurement_uri
from semquak.utils import add_new_metric_to_config, clean_identifier, clean_value, map_http_error, safe_literal, validate_datatype

def load_existing_graph(output_file: str) -> Graph | None:
    """
    Carica il grafo esistente da file TTL, se presente.
    """
    g = Graph()
    if os.path.exists(output_file):
        g.parse(output_file, format="turtle")
        print("Caricato grafo esistente da", output_file)
        return g
    else:
        print("Nessun grafo esistente da load_existing_graph")
        return None
    
# TODO: Implementare il confronto con gli assessment e non solo con l'ultimo
def add_new_assessment(g: Graph, row: pd.Series, new_timestamp: datetime, new_version_tag: str):
    """
    Aggiunge un nuovo assessment al grafo, se estiste almeno una metrica diversa da quella dell' assessment precedente.
    Se tutte le metriche sono uguali, aggiorna solo la data di generazione dell'assessment uguale.
    """
    kg_id = str(row['KG id']).strip()
    profile_uri = get_profile_uri(kg_id) 
    new_assessment_uri = get_assessment_uri(kg_id, new_version_tag)

    temp_g = Graph()

    temp_g.add((new_assessment_uri, RDF.type, EX.Assessment))
    temp_g.add((profile_uri, RDF.type, DCAT.Dataset))
    temp_g.add((profile_uri, EX.hasAssessment, new_assessment_uri))
    temp_g.add((new_assessment_uri, PROF.hasProfile, profile_uri))
    temp_g.add((new_assessment_uri, PROV.generateAtTime, Literal(new_timestamp, datatype=XSD.dateTime)))

    latest_assessment = get_latest_assessment_for_kg(g, kg_id)
    
    if latest_assessment is not None:
        print("Trovato assessment precedente")
        prev_values = extract_assessment_values(g, latest_assessment)
    else:
        print("Nessun assessment precedente trovato")
        prev_values = {'metrics': {}, 'attributes': {}}

    changed = add_metrics(temp_g, row, new_version_tag, new_assessment_uri, prev_values['metrics'])
    add_profile_attributes(g, row, profile_uri, new_assessment_uri, new_timestamp, changed)
    
    if changed:
        print("Aggiungo il nuovo assessment al grafo\n\n")
        g += temp_g
    else:
        if (latest_assessment):
            print("Aggiorno solo la data di generazione dell'assessment precedente\n\n")
            g.add((latest_assessment, PROV.generateAtTime, Literal(new_timestamp, datatype=XSD.dateTime)))

def add_attribute_to_profile(g: Graph, attribute_uri: URIRef, profile_uri: URIRef, curr_value: object, config: dict, timestamp: datetime):
    """
    Aggiunge o aggiorna un attributo del profilo e la relativa data di generazione
    """
    g.add((profile_uri, EX.hasAttribute, attribute_uri))
    g.add((attribute_uri, RDF.type, EX.Attribute))
    predicate = config['predicate']
    datatype = config["datatype"]

    prev_value = str(get_attribute_value(g, attribute_uri, predicate))

    error_uri = map_http_error(curr_value)
    if error_uri:
        curr_value = error_uri
    else:
        curr_value = validate_datatype(curr_value, datatype)

    if str(prev_value) != str(curr_value):
        attribute_name = attribute_uri.split("/")[-2].replace("_", " ")
        print(f"{attribute_name} {predicate}: {prev_value} -> {curr_value}")
        g.set((attribute_uri, predicate, curr_value))
        g.set((attribute_uri, PROV.generateAtTime, Literal(timestamp, datatype=XSD.dateTime)))

# TODO: da rivedere i predicati EX.hasProfileAttribute ed EX.AttributeContextAssessment
def add_attribute_to_assessment(g: Graph, config: dict, attribute_uri: URIRef, assessment_uri: URIRef, value: object, timestamp: datetime):
    """
    Collega l'attributo all'assessment e aggiorna il valore nel contesto dell'assessment
    """
    version_tag = timestamp.strftime("%Y-%m-%d")
    attribute_uri = URIRef(f"{attribute_uri}/{version_tag}")
    g.add((assessment_uri, EX.hasProfileAttribute, attribute_uri))
    g.add((attribute_uri, RDF.type, EX.AttributeContextAssessment))
    
    safe_literal(g, value, config["predicate"], attribute_uri, datatype=XSD.string)
    attr_name = attribute_uri.split('/')[-3]
    for i, prov in enumerate(config['access_methods'], start=1):
        attr_ass_uri = URIRef(PROF[f"attribute/{attr_name}_{i}/{version_tag}"])
        g.add((attr_ass_uri, RDF.type, RDF.Property))
        g.add((attr_ass_uri, RDFS.label, Literal(attr_name, datatype=XSD.string)))
        target_uri = prov if isinstance(prov, URIRef) else URIRef(prov)
        g.add((attr_ass_uri, EX.ComputedOver, target_uri))
        g.add((attribute_uri, EX.attributeProperty, attr_ass_uri))

    g.add((attribute_uri, PROV.generateAtTime, Literal(timestamp, datatype=XSD.dataTime)))

def add_profile_attributes(g: Graph, row: pd.Series, profile_uri: URIRef, assessment_uri: URIRef, timestamp: datetime, changed: bool):
    """
    Aggiunge gli attributi del profilo di un KG al grafo.
    """
    kg_id = str(row['KG id']).strip()

    for attr_name, config in profile_attributes.items():
        raw_value = row.get(attr_name)
        if raw_value is None:
            continue
        
        value = clean_value(raw_value)
        if value is None:
            continue
        
        cleaned_attr_name = clean_identifier(attr_name)
        attr_prof_uri = get_profile_attribute_uri(cleaned_attr_name, kg_id)

        add_attribute_to_profile(g, attr_prof_uri, profile_uri, value, config, timestamp)

        if attr_name in assessment_attributes and not changed:
           add_attribute_to_assessment(g, config, attr_prof_uri, assessment_uri, value, timestamp)
        
        for i, prov in enumerate(config['access_methods'], start=1):
            attr_uri = URIRef(f"{get_attribute_uri(cleaned_attr_name)}_{i}")
            g.add((attr_uri, RDF.type, RDF.Property))
            g.add((attr_uri, RDFS.label, Literal(attr_name, datatype=XSD.string)))
            target_uri = prov if isinstance(prov, URIRef) else URIRef(prov)
            g.add((attr_uri, EX.ComputedOver, target_uri))
            g.add((attr_prof_uri, EX.attributeProperty, attr_uri))

def add_metrics(g: Graph, row: pd.Series, new_timestamp: str, assessment_uri: URIRef, pred_values: dict | None = None) -> bool:
    """
    Aggiunge le metriche di qualità di un KG al grafo e fa il confronto con le metriche dell'assessment precedente

    Returns:
        bool: 
            - True se sono state rilevate differenze o aggiunte nuove metriche
            - False se NON ci sono differenze rispetto all'assessment precedente
    """
    kg_id = str(row['KG id']).strip()
    changed = False

    for metric_name in row.index:
        if metric_name in profile_attributes:
            continue

        value = clean_value(row[metric_name])
        if value is None:
            continue

        cleaned_metric_name = clean_identifier(metric_name)

        if metric_name in metrics:
            config = metrics[metric_name]
            datatype = config['datatype']
            access_methods = config['access_methods']
            dimension = config["dimension"].replace(" ", "_")

            prev_value = pred_values.get(metric_name) if pred_values else None
            if prev_value is None or str(value) != str(prev_value):
                print(f"Metrica '{metric_name}' cambiata: {prev_value} -> {value}")
                changed = True

        else:
            # Aggiungo la metrica sconosciuta con configurazione di default
            datatype = "string"
            access_methods = [UN]
            add_new_metric_to_config(metric_name, datatype)
            changed = True

        qa_uri = get_quality_measurement_uri(cleaned_metric_name, kg_id, new_timestamp)
        g.add((assessment_uri, DQV.hasQualityMeasurement, qa_uri))
        g.add((qa_uri, RDF.type, DQV.QualityMeasurement))
        g.add((qa_uri, DQV.computedOn, assessment_uri)) 
        safe_literal(g, value, DQV.value, qa_uri, datatype=datatype)

        for i, prov in enumerate(access_methods, start=1):
            metric_uri = URIRef(f"{get_metric_uri(cleaned_metric_name)}{i}")
            g.add((metric_uri, RDF.type, DQV.Metric))
            g.add((metric_uri, RDFS.label, Literal(metric_name, datatype=XSD.string)))
            target_uri = prov if isinstance(prov, URIRef) else URIRef(prov)
            g.add((metric_uri, EX.ComputedOver, target_uri))
            g.add((qa_uri, DQV.isMeasurementOf, metric_uri))
            add_dimension(g, dimension, metric_uri)

    if changed:
        print("Cambiamenti rilevati")
    else:
        print("Nessuna differenza trovata")

    return changed

def add_dimension(g: Graph, dim_name: str, metric_uri: URIRef):
    """
    Aggiunge alla metrica il nodo della dimensione
    """
    dimension_uri = get_dimension_uri(dim_name)

    g.add((metric_uri, DQV.inDimension, dimension_uri))

def first_interaction(timestamp: datetime, version_tag: str, filename: str) -> Graph:
    """
    Crea un nuovo grafo da zero partendo dai dati CSV.
    Da usare solo nella prima esecuzione.
    """
    print("Prima esecuzione: creazione del grafo da zero...")
    
    g = Graph()
    bind_common_namespaces(g)
    add_distribution_and_errors_nodes(g)
    add_categories_and_dimensions_nodes(g)

    df = pd.read_csv(filename)
    for _, row in df.iterrows():
        kg_id = str(row['KG id']).strip()
        profile_uri = get_profile_uri(kg_id)

        print(f"\nElaboro KG ID: {kg_id}")
       
        assessment_uri = get_assessment_uri(kg_id, version_tag)
        print(f"Creo assessment: {assessment_uri}")

        g.add((assessment_uri, RDF.type, EX.QualityAssessment)) 
        g.add((assessment_uri, PROF.hasProfile, profile_uri))          
        g.add((assessment_uri, PROV.generateAtTime, Literal(timestamp, datatype=XSD.dateTime)))

        g.add((profile_uri, RDF.type, DCAT.Dataset))
        g.add((profile_uri, EX.hasAssessment, assessment_uri))  

        add_profile_attributes(g, row, profile_uri, assessment_uri, timestamp, False)
        add_metrics(g, row, version_tag, assessment_uri)
    return g