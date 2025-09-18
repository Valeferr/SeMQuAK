from rdflib import  Namespace

"""
    Definizione dei namespaces
"""

EX = Namespace("http://example.org/")
PROF = Namespace("http://www.w3.org/ns/dx/profile/") 
DCTERMS = Namespace("http://purl.org/dc/terms/")
DQV = Namespace("http://www.w3.org/ns/dqv#")        
DCAT = Namespace("http://www.w3.org/ns/dcat#")      
PROV = Namespace("http://www.w3.org/ns/prov#") 
OWL = Namespace("http://www.w3.org/2002/07/owl#")
RDF  = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
RDFS = Namespace("http://www.w3.org/2000/01/rdf-schema#")
XSD  = Namespace("http://www.w3.org/2001/XMLSchema#")
VOID = Namespace("http://rdfs.org/ns/void#")

QM = Namespace(EX["metric/"])
ERROR = Namespace(EX["error/"])
META = Namespace(EX["metadata/"])  
SPA = Namespace(EX["SPARQL_endpoint/"])
UN = Namespace(EX["unknown/"])
VO = Namespace(EX["void_file/"])
PB = Namespace(EX["publisher/"])
