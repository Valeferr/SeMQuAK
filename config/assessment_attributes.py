from config.namespaces import EX, META, SPA, VO, XSD, VOID, DCAT, DCTERMS

"""
    Definizione degli attributi profilo dell'assessment
"""

assessment_attributes = {
        
    "Languages (metadata)": {
        "predicate": DCTERMS.language,
        "datatype": XSD.string,
        "access_methods": [META, VO],
        "dimension": "Versatility",
        "metric_output": "absent: if no lang is indicated in the metadata; list of langs: if at least a lang tag is retrieved",
        "description": "Checking whether metadata is available in different languages",
    },

    "Offline dumps": {
        "predicate": EX.offlineDumps,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Availability",
        "metric_output": "",
        "description": "",
    },

    "Vocabularies": {
        "predicate": VOID.vocabulary,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Understandability",
        "metric_output": "[]: if the vocabularies used are not indicated; -: the SPARQL endpoint is missing; list of vocabularies: if the vocabularies used are indicated.",
        "description": "checking whether a list of vocabularies used in the dataset is provided",
    },

    "URL for download the dataset": {
        "predicate": VOID.dataDump,
        "datatype": XSD.string,
        "access_methods": [META, SPA, VO],
        "dimension": "Versatility",
        "metric_output": "[]: if the sparql endpoint or rdf dump is not online;  list of links: if SPARQL endpoint and RDF dump are online.",
        "description": "Checking whether the data is available as a SPARQL endpoint and is available for download as an RDF dump",
    },

    "External links": {
        "predicate": EX.hasExternalLinks,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Interlinking",
        "metric_output": "",
        "description": "",
    },

    "Dataset update frequency": {
        "predicate": EX.accrualPeriodicity,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Timeliness",
        "metric_output": "[]: the update frequency is not indicated; -: the SPARQL endpoint is missing; list of strings: the update frequency is indicated.",
        "description": "it corresponds to the 'stating the [...] frequency of data validation"
    },

    "Dataset URL": {
        "predicate": DCAT.accessURL,
        "datatype": XSD.anyURI,
        "access_methods": [SPA, VO, META],
        "dimension": "Availability",
        "metric_output": "url: the dataset url; absent: if the dataset url can't be retrieved",
        "description": "Dataset URL"
    },

    "Sparql endpoint": {
        "predicate": VOID.sparqlEndpoint,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Availability",
        "metric_output": "Offline: if the sparql endpoint is not online;  Available: if SPARQL endpoint is online.; -:The SPARQL endpoint is missing.",
        "description": "Checking whether the server responds to a SPARQL query",
    },

    "SPARQL endpoint URL": {
        "predicate": DCAT.endpointURL,
        "datatype": XSD.anyURI,
        "access_methods": [SPA],
        "dimension": "Versatility",
        "metric_output": "",
        "description": "",
    },

     "License machine redeable (metadata)": {
        "predicate": DCTERMS.license,
        "datatype": XSD.string,
        "access_methods": [META, VO],
        "dimension": "Licensing",
        "metric_output": "string: the license if it can be recovered; False: the license is not indicated",
        "description": "detection of the indication of a license in the VoID description or in the dataset itself",
    },

    "License machine redeable (query)": {
        "predicate": DCTERMS.license,
        "datatype": XSD.anyURI,
        "access_methods": [SPA],
        "dimension": "Licensing",
        "metric_output": "string: the license if it can be recovered; -: the license is not indicated or the SPARQL endpoint is missing.",
        "description": "detection of the indication of a license in the VoID description or in the dataset itself",
    },

    "License human redeable": {
        "predicate": EX.hasHumanReadableLicense,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Licensing",
        "metric_output": "True: the human readable license is indicated; False: the human readable license is not indicated; -: The SPARQL endpoint is missing.",
        "description": "Detection of a license in the documentation of the dataset",
    },

    "Use HTTPS": {
        "predicate": EX.usesHTTPS,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Security",
        "metric_output": "False: Does not use HTTPS; True: Uses HTTPS; -: The SPARQL endpoint is missing.",
        "description": "HTTPS support",
    },

    "Requires authentication": {
        "predicate": EX.requiresAuthentication,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Security",
        "metric_output": "False: Authentication is not required; True: authentication required; -: The SPARQL endpoint is missing.",
        "description": "use of login credentials (or use of SSL or SSH)",
    },

    "Availability of a common accepted Media Type": {
        "predicate": EX.availebilityMediaType,
        "datatype": XSD.boolean,
        "access_methods": [SPA, VO, META],
        "dimension": "Availability",
        "metric_output": "True: if at least one commonly accepted serialization format is provided; False: if no commonly accepted serialization format is provided; No dump available: if no dump is available;",
        "description": "checking whether data is available in a rdf serialization format that is commonly accepted",
    },

    'Inactive links': {
        'predicate': EX.inactiveLinks,
        'datatype': XSD.boolean,
        'access_methods': [META],
        'dimension': 'Availability',
        "metric_output": "",
        "description": "",
    },

    "Availability for download (query)" : {
        "predicate": EX.availabilityForDownload,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Availability",
        "metric_output": "False: The RDF dump is offline;  True: The RDF dump is online. -: The RDF dump is missing.",
        "description": "Checking whether an RDF dump is provided and can be downloaded",
    },

    "Uses RDF structures": {
        "predicate": EX.usesRDFStructures,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Interpretability",
        "metric_output": "",
        "description": "",
    },

    "Ontology Hijacking problem": {
        "predicate": EX.hasOntologyHijacking,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Consistency",
        "metric_output": "True: if ontology hijacking problem is detected; False: if ontology hijacking problem is not detected; -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "detection of the redefinition by third parties of external classes/ properties such that reasoning over data using those external terms is affected",
    },

    "Limited": {
        "predicate": EX.isLimited,
        "datatype": XSD.boolean,
        "access_methods": [SPA],
        "dimension": "Unknown",
        "metric_output": "",
        "description": "",
    },

    "Is on a trusted provider list": {
        "predicate": EX.isTrustedProvider,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Believability",
        "metric_output": "boolean: true if the provider is trusted; false: if the provider is not trusted",
        "description": "checking whether the provider/contributor is contained in a list of trusted providers",
    },

    "Presence of example": {
        "predicate": EX.hasExample,
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Understandability",
        "metric_output": "False: if examples are not provided; True: if examples are provided.",
        "description": "detecting whether examples of SPARQL queries are provided",
    },

    "metadata-media-type": {
        "predicate": DCAT.mediaType,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Versatility",
        "metric_output": "[]: if no serialization format is provided; list of serialization formats: if at least one serialization format is provided",
        "description": "checking whether data is available in different serialization formats",
    },

    "Languages (query)": {
        "predicate": DCTERMS.language,
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Versatility",
        "metric_output": "False: if no lang tag is retrieved; list of langs: if at least a lang tag is retrieved; -: if the SPARQL endpoint is missing.",
        "description": "Checking whether data is available in different languages",
    },

    "Serialization formats": {
        "predicate": DCTERMS.format,
        "datatype": XSD.string,
        "access_methods": [META, VO, SPA],
        "dimension": "Versatility",
        "metric_output": "[]: if no serialization format is provided; list of serialization formats: if at least one serialization format is provided; -: if the SPARQL endpoint is missing.",
        "description": "checking whether data is available in different serialization formats",
    },

    "Availability VoID file": {
        "predicate": EX.availabilityVoIDFile,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Availability",
        "metric_output": "",
        "description": "",
    },

    "Author (metadata)": {
        "predicate": DCTERMS.creator,
        "datatype": XSD.string,
        "access_methods": [META, VO],
        "dimension": "Verifiability",
        "metric_output": "False: if the author is not indicated; string with authors: if the author is indicated.",
        "description": "stating the author and his contributors, the publisher of the data and its sources",
    },

    "Sources": {
        "predicate": DCTERMS.source,
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Verifiability",
        "metric_output": "string: the website, the name and the email of the source; False: if the sources are not indicated.",
        "description": "stating the author and his contributors, the publisher of the data and its sources",
    },

    "Availability for download (metadata)": {
        "predicate": EX.availabilityForDownload,
		"datatype": XSD.string,
		"access_methods": [META, VO],
		"dimension": "Availability",
        "metric_output": "0: The RDF dump is offline;  1: The RDF dump is online. -1: The RDF dump is missing.",
        "description": "Checking whether an RDF dump is provided and can be downloaded",
	},

    "Availability of RDF dump (metadata)": {
        "predicate": VOID.dataDump,
        "datatype": XSD.boolean,
        "access_methods": [META, VO],
        "dimension": "Versatility",
        "metric_output": "0: The RDF dump is offline;  1: The RDF dump is online. -1: The RDF dump is missing.",
        "description": "Checking whether an RDF dump is provided and can be downloaded",
    },

    "Contributor": {
        "predicate": DCTERMS.contributor,
        "datatype": XSD.string,
        "access_methods": [SPA, VO],
        "dimension": "Verifiability",
        "metric_output": "[]: if the contributors is not indicated; -: the SPARQL endpoint is missing; list of contributors: if the contributors is indicated.",
        "description": "stating the author and his contributors, the publisher of the data and its sources",
    },

    "Publisher": {
        "predicate": DCTERMS.publisher,
        "datatype": XSD.string,
        "access_methods": [SPA, VO],
        "dimension": "Verifiability",
        "metric_output": "[]: if the publisher is not indicated; -: the SPARQL endpoint is missing; list of publishers: if the publisher is indicated.",
        "description": "stating the author and his contributors, the publisher of the data and its sources",
    },
}