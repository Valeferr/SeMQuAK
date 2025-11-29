from config.namespaces import META, SPA, VO, UN
from rdflib.namespace import XSD

"""
    Definizione delle metriche
"""

metrics = {
    "SKOS mapping properties": {
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Interlinking",
        "metric_output": "integer: the number of mapping properties; -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query. False: if no mapping property is present.",
        "description": "skos:closeMatch | skos:exactMatch | skos:broadMatch | skos:narrowMatch | skos:relatedMatch",
    },

    "Standard deviation of latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
        "metric_output": "",
        "description": "",
    },

    " Standard deviation of throughput": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
        "metric_output": "",
        "description": "",
    },

    "Degree of connection": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "Interlinking",
        "metric_output": "integer: the degree of connection; -: if the dataset is not interlinked.",
        "description": "detection of (a) interlinking degree, (b) clustering coefficient, (c) centrality, (d) open sameAs chains and (e) description richness through sameAs by using network measures",
	},

    "Average latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
        "metric_output": "",
        "description": "",
    },

    "Average throughput": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
        "metric_output": "",
        "description": "",
    },

    "Median latency": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Performance",
        "metric_output": "Median latency in milliseconds. Best value: <1000 ms",
        "description": "if an HTTP-request is not answered within an average time of one second, the latency of the data source is considered too low",
    },

    "Median throughput": {
         "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Performance",
        "metric_output": "# of requests answered per second. Best value: Higher is better",
        "description": "ino. of answered HTTP-requests per second",
    },

    "Centrality": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Interlinking",
        "metric_output": "float: the centrality; empty: if the dataset is not interlinked.",
        "description": "detection of (a) interlinking degree, (b) clustering coefficient, (c) centrality, (d) open sameAs chains and (e) description richness through sameAs by using network measures",
    },

    "Clustering coefficient": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Interlinking",
        "metric_output": "float: the clustering coefficient; {}: if the dataset is not interlinked.",
        "description": "detection of (a) interlinking degree, (b) clustering coefficient, (c) centrality, (d) open sameAs chains and (e) description richness through sameAs by using network measures",
    },

    "PageRank": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Reputation",
        "metric_output": "float: the page rank; empty: if the dataset is not interlinked.",
        "description": "analyzing page rank of the dataset",
    },

    "Trust value": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Believability",
        "metric_output": "float: the trust value;",
        "description": "Meta-information about the identity of information provider",
    },

    "Interlinking completeness": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Completeness", 
        "metric_output": "[0,1]. Best value: 1. insufficient data: if the interlinking completeness can't be calculated.",
        "description": "degree to which interlinks are not missing",
    },

    "URIs Deferenceability": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Accessibility",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "HTTP URIs should be dereferenceable, i.e. HTTP clients should be able to retrieve the resources identified by the URI",
    },

    "FAIR score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "FAIR",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall FAIR score computed as a linear combination of all scores of the individual FAIR principles",
    }, 
    
    "F score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "FAIR",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall FAIR score computed as a linear combination of all scores of the individual F subprinciples",
    }, 

    "A score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "FAIR",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall Accessibility score computed as a linear combination of all scores of the individual A subprinciples",
    }, 
    
    "R score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "FAIR",
        "metric_score": "[0,1]. Best value: 1.",
        "description": "Overall Reusability score computed as a linear combination of all scores of the individual R subprinciples",
    }, 
    
    "I score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "FAIR",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall Interoperability score computed as a linear combination of all scores of the individual I subprinciples",
    }, 
    
    "Score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall quality score computed as a linear combination of all scores of the individual quality dimensions",
    }, 

    "Normalized score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
        "metric_output": "[0,100]. Best value: 100.",
        "description": "Overall quality score computed as a linear combination of all scores of the individual quality dimensions.",
    },

    "Availability score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Availability",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the availability dimension computed as a linear combination of the individual availability metrics scores",
    }, 
    
    "Licensing score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Licensing",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the licensing dimension computed as a linear combination of the individual licensing metrics scores",
    },
    
    "Interlinking score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Interlinking",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the interlinking dimension computed as a linear combination of the individual interlinking metrics scores",
    }, 
    
    "Performance score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the performance dimension computed as a linear combination of the individual performance metrics scores",
    }, 
    
    "Accuracy score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Accuracy",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the accuracy dimension computed as a linear combination of the individual accuracy metrics scores",
    },
    
    "Consistency score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Consistency",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the consistency dimension computed as a linear combination of the individual consistency metrics scores",
    }, 

    "Conciseness score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Conciseness",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the conciseness dimension computed as a linear combination of the individual conciseness metrics scores",
    }, 
    
    "Verifiability score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Verifiability",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the verifiability dimension computed as a linear combination of the individual verifiability metrics scores",
    },

    "Reputation score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Reputation",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the reputation dimension computed as a linear combination of the individual reputation metrics scores",
    }, 
    
    "Believability score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Believability",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the believability dimension computed as a linear combination of the individual believability metrics scores",
    }, 
    
    "Currency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, VO],
        "dimension": "Currency",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the currency dimension computed as a linear combination of the individual currency metrics scores",
    },

    "Volatility score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Timeliness",
        "metric_output": "",
        "description": "",
    }, 
    
    "Completeness score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Completeness",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the completeness dimension computed as a linear combination of the individual completeness metrics scores",
    }, 
    
    "Amount of data score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the amount of data dimension computed as a linear combination of the individual amount of data metrics scores",
    },
    
    "Representational-Consistency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Interoperability",
    }, 
    
    "Representational-Conciseness score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Conciseness",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the representational-conciseness dimension computed as a linear combination of the individual representational-conciseness metrics scores",
    },
    
    "Understandability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, META, VO],
        "dimension": "Interoperability",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the understandability dimension computed as a linear combination of the individual understandability metrics scores",
    },  
    
    "Interpretability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Interpretability",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the interpretability dimension computed as a linear combination of the individual interpretability metrics scores",
    }, 
    
    "Versatility score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Versatility",
        "metric_score": "[0,1]. Best value: 1.",
        "description": "Overall score for the versatility dimension computed as a linear combination of the individual versatility metrics scores",
    },
    
    "Security score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Security",
        "metric_output": "[0,1]. Best value: 1.",
        "description": "Overall score for the security dimension computed as a linear combination of the individual security metrics scores",
    },

    "Timeliness score": {
		"datatype": XSD.decimal,
		"access_methods": [META],
		"dimension": "Timeliness",
		"metric_output": "[0,1]. Best value: 1.",
		"description": "Overall score for the timeliness dimension computed as a linear combination of the individual timeliness metrics scores",
	},

	"Interoperability score": {
		"datatype": XSD.decimal,
		"access_methods": [META],
		"dimension": "Interoperability",
		"metric_output": "[0,1]. Best value: 1.",
		"description": "Overall score for the interoperability dimension computed as a linear combination of the individual interoperability metrics scores",
	},

    "Number of entities" : {
        "datatype": XSD.integer,
        "access_methods": [VO, SPA],
        "dimension": "Amount of data",
        "metric_output": "integer: the number of entities; -: if the number of entities can't be retrieved or the SPARQL endpoint is missing.",
        "description": "Number of entities",
    },

    "Modification date": {
        "datatype": XSD.string,
        "access_methods": [SPA, VO],
        "dimension": "Currency",
		"metric_output": "-: if the modification date can't be retrieved; date: if the modification date is correctly retrieved",
        "description": "Use of dates as the point in time of the last verification of a statement represented by dcterms:modifieds",
    },

    " Number of triples (metadata)": {
        "datatype": XSD.integer,
        "access_methods": [META, VO],
        "dimension": "Amount of data",
        "metric_output": "integer: the number of triples; -: if the number of triples can't be retrieved",
        "description": "Number of triples",
    },

    "Number of property": {
        "datatype": XSD.integer,
        "access_methods": [SPA, VO],
        "dimension": "Amount of data",
        "metric_output": "integer: the number of properties; -: if the number of properties can't be retrieved or the SPARQL endpoint is missing.",
        "description": "Number of properties",
    },

    "Signed": {
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Verifiability",
        "metric_output": "boolean: true if the dataset is signed; false: if the dataset is not signed.",
        "description": "checking whether the dataset is signed",
    },

    " Number of triples": {
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Amount of data", 
        "metric_output": "",
        "description": "",
    },

    "Number of triples (query)": {
        "datatype": XSD.integer,
        "access_methods": [SPA],
        "dimension": "Amount of data",
        "metric_output": "integer: the number of triples; -: The SPARQL endpoint is missing.",
        "description": "Number of triples",
    },
    
	"Extensional conciseness": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Conciseness",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "number of unique objects in relation to the overall number of object representations in the dataset",
	},

	"Intensional conciseness": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Conciseness",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "number of unique objects in relation to the overall number of object representations in the dataset",
	},
    
	"Use RDF structures": {
		"datatype": XSD.boolean,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "True: if RDF structures are used; False: if RDF structures aren't used.; -: The SPARQL endpoint is missing.",
        "description": "detection of the non-standard usage of collections, containers and reification",
	},

	"Number of triples linked": {
		"datatype": XSD.integer,
		"access_methods": [SPA],
		"dimension": "Consistency",
        "metric_output": "",
        "description": "",
	},

	"U1-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Understandability",
        "metric_output": "",
        "description": "",
	},

	"CS2-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Conciseness",
        "metric_output": "",
        "description": "",
	},

	"IN3-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Interoperability",
        "metric_output": "",
        "description": "",
	},

	"RC1-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"RC2-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"IN4-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Interpretability",
        "metric_output": "",
        "description": "",
	},

	"U5-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Understandability",
        "metric_output": "",
        "description": "",
	},

	"PE2-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Performance",
        "metric_output": "",
        "description": "",
	},

	"PE3-value": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Performance",
        "metric_output": "",
        "description": "",
	},

	"F1-M Unique and persistent ID": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: dataset registered in a search engine that provides a persistent DOI; 0: otherwise",
        "description": "Unique and persistent identifiers",
	},

	"F1-D URIs dereferenceability": {
		"datatype": XSD.decimal,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "# of dereferenceable URIs / total # of URIs. Best value: 1.",
        "description": "URIs dereferenceability",
	},

	"F2a-M - Metadata availability via standard primary sources": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: SPARQL endpoint, searchable engine, or VoID/DCAT; 0: otherwise",
        "description": "Metadata availability via standard primary sources",
	},

	"F2b-M Metadata availability for all the attributes covered in the FAIR score computation": {
		"datatype": XSD.decimal,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "# of covered attributes / total # of attributes. Best value: 1.",
        "description": "Coverage of required attributes",
	},

	"F3-M Data referrable via a DOI": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: metadata attach DOI(s) to data; 0: otherwise",
        "description": "Data referrable via a DOI",
	},

	"F4-M Metadata registered in a searchable engine": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: dataset registered in any search engine; 0: otherwise",
        "description": "Metadata registered in a searchable engine",
	},

	"A1-D Working access point(s)": {
		"datatype": XSD.decimal,
		"access_methods": [META],
		"dimension": "FAIR",
        "description": "Working access point(s)",
        "metric_output": "1: operational SPARQL or accessible data dump; 0.5: accessible SPARQL endpoint or data dump; 0: otherwise",
	},

	"A1-M Metadata availability via working primary sources": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: sources discovered in F2a-M woek and contain metadata; 0: otherwise",
        "description": "Working primary sources with metadata",
	},

	"A1.2 Authentication & HTTPS support": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: security requirements can be discovered via SPARQL; 0: otherwise",
        "description": "Authentication & HTTPS support",
	},

	"A2-M Registered in search engines": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: dataset registered in any search engine; 0: otherwise",
        "description": "Registered in search engines",
	},

	"R1.1 Machine- or human-readable license retrievable via any primary source": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: license explicitly reported; 0: otherwise",
        "description": "Any license retrievable",
	},

	"R1.2 Publisher information such as authors-contributors-publishers and sources": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: publisher info explicitly reported; 0: otherwise",
		"description": "Publisher details",
	},

	"R1.3-D Data organized in a standardized way": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: SPARQL endpoint or valid data dump or OWL/RDFS; 0: otherwise",
        "description": "Data organized in standardized way",
	},

	"R1.3-M Metadata are described with VoID/DCAT predicates": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: published according to VoID/DCAT specs; 0: otherwise",
        "description": "VoID/DCAT description",
	},

	"I1-D Standard & open representation format": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: valid mediatypes or OWL/RDF(S); 0: otherwise",
		"description": "Standard & open representation format",
	},

	"I1-M Metadata are described with VoID/DCAT predicates": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: published according to VoID/DCAT specs; 0: otherwise",
		"description": "VoID/DCAT description",
	},

	"I2 Use of FAIR vocabularies": {
		"datatype": XSD.decimal,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "# of FAIR vocabularies / total # of vocabularies. Best value: 1.",
		"description": "Usage of FAIR vocabularies",
	},

	"I3-D Degree of connection": {
		"datatype": XSD.integer,
		"access_methods": [META],
		"dimension": "FAIR",
        "metric_output": "1: contains link to another dataset; 0: otherwise",
		"description": "Degree of connection",
	},

	"Average length of URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "Average # of characters in URIs (subject). Best value: <80 characters",
        "description": "detection of long URIs or those that contain query param-eters",
	},

	"Standard deviation lenght URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"Median length URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"Average length of URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "Average # of characters in URIs (predicate). Best value: <80 characters",
        "description": "detection of long URIs or those that contain query param-eters",
	},

	"Standard deviation lenght URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"Median length URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"Max length URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"Average length of URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "Average # of characters in URIs (object). Best value: <80 characters",
        "description": "detection of long URIs or those that contain query parameters",
	},

	"Standard deviation lenght URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"Median length URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Representational-conciseness",
        "metric_output": "",
        "description": "",
	},

	"Number of samAs chains": {
		"datatype": XSD.string,
		"access_methods": [META],
		"dimension": "Interlinking",
        "metric_output": "False: no sameAs chains in the dataset; -: the SPARQL endpoint is missing; integer: number of sameAs chains in the dataset.",
        "description": "detection of (a) interlinking degree, (b) clustering coefficient, (c) centrality, (d) open sameAs chains and (e) description richness through sameAs by using network measures",
	},

	"Number of labels/comments present on the data": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Understandability",
        "metric_output": "integer: the number of labels/comments; -: the SPARQL endpoint is missing; False: if no label/comment is present or error during the execution of the sparql query.",
        "description": "no. of entities described by stating an rdfs:label or rdfs:comment in the dataset / total no. of entities described in the data.",
	},

	"Regex uri": {
		"datatype": XSD.string,
		"access_methods": [VO, SPA],
		"dimension": "Understandability",
        "metric_output": "[] or empty value: no regex provided; -: if the SPARQL endpoint is missing; list of regex: if at least a regex is provided.",
        "description": "detecting whether a regular expression that matches the URIs is present",
	},

	"Number of blank nodes": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Interpretability",
        "metric_output": "integer: the number of blank nodes; -: if the SPARQL endpoint is missing; False: if no blank node is present or error during the execution of the sparql query.",
        "description": "detecting the use of blank nodes",
	},

	"Deprecated classes/properties used": {
		"datatype": XSD.decimal,
		"access_methods": [SPA],
		"dimension": "Consistency",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online.",
        "description": "detection of use of OWL classes owl:DeprecatedClass and owl:DeprecatedProperty",
	},

	"Triples with misplaced property problem": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Consistency",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query. insufficient data: if the property cannot be recovered.",
        "description": "Detection of a URI defined as a class is used as a property or a URI defined as a property is used as a class",
	},

	"Triples with misplaced class problem": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Consistency",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query. insufficient data: if the class cannot be recovered.",
        "description": "Detection of a URI defined as a class is used as a property or a URI defined as a property is used as a class",
	},

	"Undefined class used without declaration": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Consistency",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query. insufficient data: if the class cannot be recovered.",
		"description": "detection of classes and properties used without any formal definition",
	},

	"Undefined properties used without declaration": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Consistency",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query. insufficient data: if the property cannot be recovered.",
        "description": "detection of classes and properties used without any formal definition",
	},

	"Triples with empty annotation problem": {
		"datatype": XSD.decimal,
		"access_methods": [SPA],
		"dimension": "Accuracy",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "labels, comments, notes which identifies triples whose property’s object value is empty string",
	},

	"Triples with white space in annotation(at the beginning or at the end)": {
		"datatype": XSD.decimal,
		"access_methods": [SPA],
		"dimension": "Accuracy",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "presence of white space in labels",
	},

	"Triples with malformed data type literals problem": {
		"datatype": XSD.decimal,
		"access_methods": [SPA],
		"dimension": "Accuracy",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "Incompatible with data type range",
	},

	"Functional properties with inconsistent values": {
		"datatype": XSD.decimal,
		"access_methods": [SPA],
		"dimension": "Accuracy",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "FP = 1 - num of triples of with inconsistent values for functional properties / num of triples",
	},

	"Invalid usage of inverse-functional properties": {
		"datatype": XSD.decimal,
		"access_methods": [SPA],
		"dimension": "Accuracy",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "IFP = 1 - num of triples of with inconsistent values for functional properties / num of triples",
	},

	"Number of triples updated": {
		"datatype": XSD.string,
		"access_methods": [META],
		"dimension": "Currency",
        "metric_output": "",
        "description": "",
	},

	"MeanTPNoOff": {
		"datatype": XSD.string,
		"access_methods": [META],
		"dimension": "Semantic Accuracy",
        "metric_output": "",
        "description": "",
	},

	"sdTPNoOff": {
		"datatype": XSD.string,
		"access_methods": [META],
		"dimension": "Semantic Accuracy",
        "metric_output": "",
        "description": "",
	},

	"Entities as member of disjoint class": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Consistency",
        "metric_output": "[0,1]. Best value: 1. -: if the SPARQL endpoint is missing or not online or error during the execution of the sparql query.",
        "description": "no. of entities described as members of disjoint classes / total no. of entities described in the dataset",
	},

	"New vocabularies defined in the dataset": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Interoperability",
        "metric_output": "[]: if no new vocabulary is defined; -: the SPARQL endpoint is missing; list of new vocabularies: if at least a new vocabulary is defined.",
        "description": "usage of established vocabularies",
	},

	"New terms defined in the dataset": {
		"datatype": XSD.string,
		"access_methods": [SPA],
		"dimension": "Interoperability",
        "metric_output": "[]: if no new term is defined; -: the SPARQL endpoint is missing; list of new terms: if at least a new term is defined.",
        "description": "detection of whether existing terms from all relevant vo-cabularies for that particular domain have been reuse",
	},

	"Time elapsed since last modification": {
		"datatype": XSD.integer,
		"access_methods": [SPA, VO],
		"dimension": "Currency",
        "metric_output": "-: if the modification date is not correctly retrieved or not indicated; an integer: if the modification date is correctly retrieved",
        "description": "Currency only measures the time since the last modification",
	},

	"Historical updates": {
		"datatype": XSD.string,
		"access_methods": [SPA, VO],
		"dimension": "Currency",
        "metric_output": "",
        "description": "",
	},

	"Number of entities counted with regex": {
		"datatype": XSD.string,
		"access_methods": [VO, SPA],
		"dimension": "Amount of data",
        "metric_output": "number: the number of entities; -: if the number of entities can't be retrieved or the SPARQL endpoint is missing.",
        "description": "Number of entities",
	},

	"Url file VoID": {
		"datatype": XSD.string,
		"access_methods": [META, SPA],
		"dimension": "Availability",
        "metric_output": "url: if VoID file url exists; - or empty: if the VoID file url does not exist",
        "description": "VoID file URL",
	},
    
	"Author (query)": {
        "datatype": XSD.string,
        "access_methods": [SPA],
        "dimension": "Verifiability",
        "metric_output": "[]: if the author is not indicated; -: the SPARQL endpoint is missing; list of authors: if the author is indicated.",
        "description": "stating the author and his contributors, the publisher of the data and its sources",
    },
    
	"Availability for download (metadata)": {
		"datatype": XSD.string,
		"access_methods": [META],
		"dimension": "Availability",
        "metric_output": "0: The RDF dump is offline;  1: The RDF dump is online. -1: The RDF dump is missing.",
        "description": "Checking whether an RDF dump is provided and can be downloaded",
	},
    
	"Availability of RDF dump (query)": {
        "datatype": XSD.boolean,
        "access_methods": [SPA, VO],
        "dimension": "Availability",
        "metric_output": "False: The RDF dump is offline;  True: The RDF dump is online. -: The RDF dump is missing.",
        "description": "Checking whether an RDF dump is provided and can be downloaded",
    },
    
	"Contributor": {
        "datatype": XSD.string,
        "access_methods": [META],
        "dimension": "Verifiability",
        "metric_output": "[]: if the contributors is not indicated; -: the SPARQL endpoint is missing; list of contributors: if the contributors is indicated.",
        "description": "stating the author and his contributors, the publisher of the data and its sources",
    },

}