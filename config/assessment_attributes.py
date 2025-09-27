from config.namespaces import EX, META, SPA, VO, XSD, VOID, DCAT, DCTERMS

"""
    Definizione degli attributi profilo dell'assessment
"""

assessment_attributes = {
        
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

    "License machine redeable (metadata)": {
        "predicate": DCTERMS.license,
        "datatype": XSD.anyURI,
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

    'Inactive links': {
        'predicate': EX.inactiveLinks,
        'datatype': XSD.boolean,
        'access_methods': [META]
    },

    "Availability for download (query)" : {
        "predicate": EX.availabilityForDownload,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
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