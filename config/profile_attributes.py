from config.namespaces import EX, META, SPA, VO
from rdflib.namespace import DCAT, XSD, DCTERMS
from rdflib import VOID

"""
    Definizione degli attributi profilo
"""

profile_attributes = {
    "KG id": {
        "predicate": DCTERMS.identifier,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "KG name": {
        "predicate": DCTERMS.title,
        "datatype": XSD.string,
        "access_methods": [SPA]
    },

    "Description": {
        "predicate": DCTERMS.description,
        "datatype": XSD.string,
        "access_methods": [SPA]
    },

    "Languages (metadata)": {
        "predicate": DCTERMS.language,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "Offline dumps": {
        "predicate": EX.offlineDumps,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "Vocabularies": {
        "predicate": VOID.vocabulary,
        "datatype": XSD.string,
        "access_methods": [SPA, VO]
    },

    "Contributor": {
        "predicate": DCTERMS.contributor,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "URL for download the dataset": {
        "predicate": VOID.dataDump,
        "datatype": XSD.string,
        "access_methods": [META, SPA, VO]
    },

    "External links": {
        "predicate": EX.hasExternalLinks,
        "datatype": XSD.string,
        "access_methods": [SPA]
    },

    "Dataset update frequency": {
        "predicate": EX.accrualPeriodicity,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "Sources": {
        "predicate": DCTERMS.source,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "Publisher": {
        "predicate": DCTERMS.publisher,
        "datatype": XSD.string,
        "access_methods": [SPA]
    },

    "Dataset URL": {
        "predicate": DCAT.accessURL,
        "datatype": XSD.anyURI,
        "access_methods": [SPA]
    },

    "Sparql endpoint": {
        "predicate": VOID.sparqlEndpoint,
        "datatype": XSD.string,
        "access_methods": [SPA]
    },

    "SPARQL endpoint URL": {
        "predicate": DCAT.endpointURL,
        "datatype": XSD.anyURI,
        "access_methods": [SPA]
    },

    "Author (query)": {
        "predicate": DCTERMS.creator,
        "datatype": XSD.string,
        "access_methods": [SPA]
    },

    "Author (metadata)": {
        "predicate": DCTERMS.creator,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "License machine redeable (metadata)": {
        "predicate": DCTERMS.license,
        "datatype": XSD.anyURI,
        "access_methods": [META]
    },

    "License machine redeable (query)": {
        "predicate": DCTERMS.license,
        "datatype": XSD.anyURI,
        "access_methods": [SPA]
    },

    "License human redeable": {
        "predicate": EX.hasHumanReadableLicense,
        "datatype": XSD.boolean,
        "access_methods": [SPA]
    },

    "Use HTTPS": {
        "predicate": EX.usesHTTPS,
        "datatype": XSD.boolean,
        "access_methods": [SPA]
    },

    "Requires authentication": {
        "predicate": EX.requiresAuthentication,
        "datatype": XSD.boolean,
        "access_methods": [META]
    },

    "Availability of a common accepted Media Type": {
        "predicate": EX.availebilityMediaType,
        "datatype": XSD.boolean,
        "access_methods": [META]
    },

    "Availability of RDF dump (query)": {
        "predicate": VOID.dataDump,
        "datatype": XSD.decimal,
        "access_methods": [SPA, VO]
    },

    "Availability of RDF dump (metadata)": {
        "predicate": VOID.dataDump,
        "datatype": XSD.boolean,
        "access_methods": [META, VO]
    },

    "Inactive links": {
        "predicate": EX.inactiveLinks,
        "datatype": XSD.boolean,
        "access_methods": [META]
    },

    "Availability for download (query)" : {
        "predicate": EX.availabilityForDownload,
        "datatype": XSD.boolean,
        "access_methods": [SPA]
    },

    "Availability VoID file": {
        "predicate": EX.availabilityVoIDFile,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "Uses RDF structures": {
        "predicate": EX.usesRDFStructures,
        "datatype": XSD.boolean,
        "access_methods": [META]
    },

    "Ontology Hijacking problem": {
        "predicate": EX.hasOntologyHijacking,
        "datatype": XSD.boolean,
        "access_methods": [SPA]
    },

    "Limited": {
        "predicate": EX.isLimited,
        "datatype": XSD.boolean,
        "access_methods": [SPA]
    },

    "Is on a trusted provider list": {
        "predicate": EX.isTrustedProvider,
        "datatype": XSD.boolean,
        "access_methods": [META]
    },

    "Age of data": {
        "predicate": DCTERMS.created,
        "datatype": XSD.dateTime,
        "access_methods": [SPA, VO]
    },

    "Presence of example": {
        "predicate": EX.hasExample,
        "datatype": XSD.boolean,
        "access_methods": [META]
    },

    "metadata-media-type": {
        "predicate": DCAT.mediaType,
        "datatype": XSD.string,
        "access_methods": [META]
    },

    "Languages (query)": {
        "predicate": DCTERMS.language,
        "datatype": XSD.string,
        "access_methods": [SPA]
    },

    "Serialization formats": {
        "predicate": DCTERMS.format,
        "datatype": XSD.string,
        "access_methods": [META]
    },
}