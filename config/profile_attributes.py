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
        "access_methods": [META],
        "dimension": "Understanbility",
    },

    "KG name": {
        "predicate": DCTERMS.title,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Understanbility",
    },

    "Description": {
        "predicate": DCTERMS.description,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Understanbility",
    },

    "Languages (metadata)": {
        "predicate": DCTERMS.language,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Versatility",
    },

    "Offline dumps": {
        "predicate": EX.offlineDumps,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Availability",
    },

    "Vocabularies": {
        "predicate": VOID.vocabulary,
        "datatype": XSD.string,
        "access_methods": [SPA, VO],
        "dimension": "Verifiability",
    },

    "Contributor": {
        "predicate": DCTERMS.contributor,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Verifiability",
    },

    "URL for download the dataset": {
        "predicate": VOID.dataDump,
        "datatype": XSD.string,
        "access_methods": [META, SPA, VO],
        "dimension": "Availability",
    },

    "External links": {
        "predicate": EX.hasExternalLinks,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Availability",
    },

    "Dataset update frequency": {
        "predicate": EX.accrualPeriodicity,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "",
    },

    "Sources": {
        "predicate": DCTERMS.source,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Availability",
    },

    "Publisher": {
        "predicate": DCTERMS.publisher,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Verifiability",
    },

    "Dataset URL": {
        "predicate": DCAT.accessURL,
        "datatype": XSD.anyURI,
        "access_methods": [SPA],
        "dimension": "Availability",
    },

    "Sparql endpoint": {
        "predicate": VOID.sparqlEndpoint,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Availability",
    },

    "SPARQL endpoint URL": {
        "predicate": DCAT.endpointURL,
        "datatype": XSD.anyURI,
        "access_methods": [SPA],
        "dimension": "Availability",
    },

    "Availability for download (metadata)": {
        "predicate": EX.availabilityForDownload,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Availability",
    },

    "Author (query)": {
        "predicate": DCTERMS.creator,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Verifiability",
    },

    "Author (metadata)": {
        "predicate": DCTERMS.creator,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Verifiability",
    },

    "License machine redeable (metadata)": {
        "predicate": DCTERMS.license,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Licensing",
    },

    "License machine redeable (query)": {
        "predicate": DCTERMS.license,
        "datatype": XSD.anyURI,
        "access_methods": [SPA],
        "dimension": "Licensing",
    },

    "License human redeable": {
        "predicate": EX.hasHumanReadableLicense,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Licensing",
    },

    "Use HTTPS": {
        "predicate": EX.usesHTTPS,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Security",
    },

    "Requires authentication": {
        "predicate": EX.requiresAuthentication,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Security",
    },

    "Availability of a common accepted Media Type": {
        "predicate": EX.availebilityMediaType,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Availability",
    },

    "Availability of RDF dump (query)": {
        "predicate": VOID.dataDump,
        "datatype": XSD.decimal,
        "access_methods": [SPA, VO],
        "dimension": "Versatility",
    },

    "Availability of RDF dump (metadata)": {
        "predicate": VOID.dataDump,
        "datatype": XSD.boolean,
        "access_methods": [META, VO],
        "dimension": "Versatility",
    },

    "Inactive links": {
        "predicate": EX.inactiveLinks,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Availability",
    },

    "Availability for download (query)" : {
        "predicate": EX.availabilityForDownload,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Availability",
    },

    "Availability VoID file": {
        "predicate": EX.availabilityVoIDFile,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Availability",
    },

    "Uses RDF structures": {
        "predicate": EX.usesRDFStructures,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Interpretability",
    },

    "Ontology Hijacking problem": {
        "predicate": EX.hasOntologyHijacking,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Consistency",
    },

    "Limited": {
        "predicate": EX.isLimited,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "",
    },

    "Is on a trusted provider list": {
        "predicate": EX.isTrustedProvider,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Believability",
    },

    "Age of data": {
        "predicate": DCTERMS.created,
        "datatype": XSD.boolean,
        "access_methods": [SPA, VO],
        "dimension": "Currency",
    },

    "Presence of example": {
        "predicate": EX.hasExample,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Understandability",
    },

    "metadata-media-type": {
        "predicate": DCAT.mediaType,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "",
    },

    "Languages (query)": {
        "predicate": DCTERMS.language,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Versatility",
    },

    "Serialization formats": {
        "predicate": DCTERMS.format,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Versatility",
    },
}