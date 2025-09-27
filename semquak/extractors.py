from rdflib import Graph, Literal, URIRef
from pandas import Series

from config.profile_attributes import profile_attributes
from config.namespaces import PROV, XSD
from config.metrics import metrics 

from semquak.helpers import get_profile_uri
from semquak.utils import clean_value

def get_latest_assessment_for_kg(g: Graph, kg_id: str) -> URIRef:
    """
    Restituisce l'assessment più recente per un dato KG ID.
    """    
    assessments = get_all_assessments_for_kg(g, kg_id)
    latest_assessment = None
    latest_date = None

    for ass in assessments:
        for _, _, dt in g.triples((ass, PROV.generateAtTime, None)):
            if isinstance(dt, Literal) and dt.datatype == XSD.dateTime:
                date_val = dt.toPython()
                if latest_date is None or date_val > latest_date:
                    latest_date = date_val
                    latest_assessment = ass

    return latest_assessment

def extract_metrics_values(g: Graph, assessment_uri: URIRef) -> list:
    metrics_query = """
        PREFIX dqv: <http://www.w3.org/ns/dqv#>

        SELECT ?measurement ?metricValue
        WHERE {
            VALUES ?assessment { <%(assessment_uri)s> }
            ?assessment dqv:hasQualityMeasurement ?measurement .
            ?measurement dqv:value ?metricValue .
        }
    """ % {"assessment_uri": assessment_uri}

    return g.query(metrics_query)

def extract_assessment_attribute_values(g: Graph, assessment_uri: URIRef) -> list:
    attributes_query = """
        PREFIX ex: <http://example.org/>
        PREFIX dcterms: <http://purl.org/dc/terms/>

        SELECT ?attrUri ?pred ?attrValue
        WHERE {
            VALUES ?assessment { <%(assessment_uri)s> }
            ?assessment_uri ex:hasProfileAttribute ?attrUri .
            ?attrUri ?pred ?attrValue .
            FILTER( 
                ?pred NOT IN (rdf:type, ex:attributeProperty, prov:generateAtTime)
            )
        }
    """ % {"assessment_uri": assessment_uri}

    return g.query(attributes_query)

def extract_assessment_values(g: Graph, assessment_uri: URIRef) -> dict:
    """
    Estrae valori delle metriche e attributi di profilo da un assessment RDF.

    Ritorna un dizionario con struttura:
    {
        'metrics': { metric_name: value },
        'attributes': { attr_name: value }
    }
    """
    values = {"metrics": {}, "attributes": {}}

    metrics_results = extract_metrics_values(g, assessment_uri)
    for row in metrics_results:
        metric_name = str(row.measurement.split("/")[-3].replace('_', ' '))
        values["metrics"][metric_name] = clean_value(row.metricValue)

    attributes_results = extract_assessment_attribute_values(g, assessment_uri)
    for row in attributes_results:
        attr_name = str(row.attrUri.split("/")[-3]).replace("_", " ")
        pred = str(row.pred)
        if attr_name in profile_attributes:
            expected_pred = str(profile_attributes[attr_name]["predicate"])
            if pred == expected_pred:
                values["attributes"][attr_name] = clean_value(row.attrValue)

    return values

def extract_current_values_from_csv(row: Series):
    """
    Estrae i valori correnti delle metriche e degli attributi di profilo da una riga del CSV.
    """
    values = {'metrics': {}, 'attributes': {}}

    def _process(name, container):
        raw_value = row.get(name)
        cleaned = clean_value(raw_value)
        container[name] = cleaned if cleaned is not None else None

    for metric_name in metrics.items():
       _process(metric_name, values['metrics'])

    for attr_name in profile_attributes.items():
        _process(attr_name, values['attributes'])

    return values

def get_attribute_value(g: Graph, attribute_uri: URIRef, predicate: URIRef) -> object | None:
    """
    Restituisce il valore di un attributo dato il suo URI e il predicato.
    """
    query = """
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX dqv: <http://www.w3.org/ns/dqv#>
        PREFIX ex: <http://example.org/ns#>
        PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX dcat: <http://www.w3.org/ns/dcat#> 
        PREFIX dcterms: <http://purl.org/dc/terms/>
        PREFIX profile: <http://www.w3.org/ns/dx/profile/> 
        PREFIX prov: <http://www.w3.org/ns/prov#>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

        SELECT ?attrValue
        WHERE {
            <%(attribute_uri)s> <%(predicate)s> ?attrValue .
        } 
    """ % {"attribute_uri": attribute_uri, "predicate": predicate}

    results = g.query(query)
    for row in results:
        return row.attrValue

    return None

def get_all_assessments_for_kg(g: Graph, kg_id: str) -> list[URIRef]:
    """
    Restituisce tutti gli assessment associati a un dato KG ID.
    """
    profile_uri = get_profile_uri(kg_id)

    query = """
    PREFIX dqv: <http://www.w3.org/ns/dqv#>
    PREFIX ex: <http://example.org/>
    PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    PREFIX profile: <http://www.w3.org/ns/dx/profile/>

    SELECT ?assessment
    WHERE {
        <%(profile_uri)s> ex:hasAssessment ?assessment .
    }
    """ % {"profile_uri": profile_uri}

    return g.query(query)
