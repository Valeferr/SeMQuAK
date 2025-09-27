from rdflib import Graph, Literal, URIRef

from config.dimensions import dimensions
from config.errors import ERROR_DEFINITIONS
from config.namespaces import EX, PROF, QM, RDFS, SKOS, SPA, META, VO, UN, ERROR, XSD, DQV, DCAT, PROV, OWL, RDF

def get_assessment_uri(kg_id: str, version_tag: str) -> URIRef:
    """Genera l'URI di un assessment dato il KG ID e il version tag"""
    return URIRef(EX[f"assessment/{kg_id}/{version_tag}"])

def get_profile_uri(kg_id: str) -> URIRef:
    """Genera l'URI di un profilo dato il KG ID"""
    return URIRef(PROF[f"{kg_id}"])

def get_profile_attribute_uri(attr_name: str, kg_id: str) -> URIRef:
    """Genera l'URI di un attributo di profilo dato il nome dell'attributo e il KG ID"""
    return URIRef(PROF[f"attribute/{attr_name}/{kg_id}"])

def get_quality_measurement_uri(metric_name: str, kg_id: str, timestamp: str) -> URIRef:
    """Genera l'URI di una misurazione di una metrica di qualità dato il nome della metrica, il KG ID e il timestamp"""
    return URIRef(EX[f"measurement/{metric_name}/{kg_id}/{timestamp}"])

def get_metric_uri(metric_name: str) -> URIRef:
    """Genera l'URI di una metrica dato il nome della metrica"""
    return URIRef(QM[f"{metric_name}_"])

def get_attribute_uri(attr_name: str) -> URIRef:
    """Genera l'URI di un attributo dato il nome dell'attributo"""
    return URIRef(PROF[f"attribute/{attr_name}_"])

def get_dimension_uri(dim_name: str) -> URIRef:
    """Genera l'URI di una dimensione dato il nome della dimensione"""
    return URIRef(EX[dim_name])

def get_category_uri(category_name: str) -> URIRef:
    """Genera l'URI di una categoria dato il suo nome"""
    return URIRef(EX[category_name])

def create_error_node(graph : Graph, code: int, label: str) -> URIRef:
    """Crea i nodi di errore e li aggiunge al grafo"""
    uri = URIRef(ERROR[str(code)])
    graph.add((uri, RDF.type, DQV.Error))
    graph.add((uri, RDFS.label, Literal(label, datatype=XSD.string)))
    return uri

def add_distribution_and_errors_nodes(g: Graph):
    """
    Aggiunge i nodi delle fonti di accesso (META, SPA, VO) e gli errori definiti.
    """
    g.add((EX.AccessMethod, RDF.type, OWL.Class))
    g.add((URIRef(META), RDF.type, EX.AccessMethod))
    g.add((URIRef(SPA), RDF.type, EX.AccessMethod))
    g.add((URIRef(VO), RDF.type, EX.AccessMethod))
    g.add((URIRef(UN), RDF.type, EX.AccessMethod))

    g.add((EX.ComputedOver, RDF.type, OWL.ObjectProperty))
    g.add((EX.ComputedOver, RDFS.range, EX.AccessMethod))

    for code, label in ERROR_DEFINITIONS.items():
        create_error_node(g, code, label)

def bind_common_namespaces(graph: Graph):
    """
    Esegue il bind dei namespace più comuni nel grafo.
    """
    graph.bind("ex", EX)  
    graph.bind("profile", PROF) 
    graph.bind("qm", QM) 
    graph.bind("SPARQL", SPA)
    graph.bind("unknown", UN)
    graph.bind("METADATA", META) 
    graph.bind("VoID", VO)
    graph.bind("error", ERROR) 
    graph.bind("xsd", XSD)
    graph.bind("dqv", DQV) 
    graph.bind("dcat", DCAT) 
    graph.bind("prov", PROV) 
    graph.bind("owl", OWL)
    graph.bind("rdf", RDF)

def add_categories_and_dimensions_nodes(g: Graph):
    """
    Aggiunge i nodi delle categorie delle metriche del grafo
    """
    for dim_name, config in dimensions.items():
        dim_uri = get_dimension_uri(dim_name.replace(" ", "_"))
        category_uri = get_category_uri(config["category"].replace(" ", "_"))

        g.add((dim_uri, RDF.type, DQV.Dimension))
        g.add((dim_uri, SKOS.prefLabel, Literal(dim_name, lang="en")))
        g.add((dim_uri, SKOS.definition, Literal(config["definition"], lang="en")))
        g.add((dim_uri, DQV.inCategory, category_uri))
    