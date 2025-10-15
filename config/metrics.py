from config.namespaces import META, SPA, VO, UN
from rdflib.namespace import XSD

"""
    Definizione delle metriche
"""

metrics = {
    "SKOS mapping properties": {
        "datatype": XSD.integer,
        "access_methods": [SPA],
        "dimension": "Interlinking",
    },

    "Standard deviation of latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
    },

    " Standard deviation of throughput": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
    },

    "Average latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
    },

    "Average throughput": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
    },

    "Median latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
    },

    "Median throughput": {
         "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Performance",
    },

    "Centrality": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Interlinking",
    },

    "Clustering coefficient": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Interlinking",
    },

    "PageRank": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Reputation",
    },

    "Trust value": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Trust",
    },

    "Interlinking completeness": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Completeness",
    },

    "URIs Deferenceability": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Availability",
    },

    "FAIR score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 
    
    "F score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 

    "A score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 
    
    "R score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 
    
    "I score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 
    
    "Score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 

    "Normalized score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    },

    "Availability score": {
        "datatype": XSD.decimal,
        "access_methods": [META, SPA, VO],
        "dimension": "Amount of data",
    }, 
    
    "Licensing score": {
        "datatype": XSD.decimal,
        "access_methods": [META, SPA, VO],
        "dimension": "Amount of data",
    },
    
    "Interlinking score": {
        "datatype": XSD.decimal,
        "access_methods": [META, SPA],
        "dimension": "Amount of data",
    }, 
    
    "Performance score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    }, 
    
    "Accuracy score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    },
    
    "Consistency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    }, 

    "Conciseness score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Conciseness",
    }, 
    
    "Verifiability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, VO],
        "dimension": "Verifiability",
    },

    "Reputation score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Reputation",
    }, 
    
    "Believability score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 
    
    "Currency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, VO],
        "dimension": "Amount of data",
    },

    "Volatility score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 
    
    "Completeness score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    }, 
    
    "Amount of data score": {
        "datatype": XSD.decimal,
        "access_methods": [META],
        "dimension": "Amount of data",
    },
    
    "Representational-Consistency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    }, 
    
    "Representational-Conciseness score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Conciseness",
    },
    
    "Understandability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, META, VO],
        "dimension": "Amount of data",
    },  
    
    "Interpretability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    }, 
    
    "Versatility score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    },
    
    "Security score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    },

    "Number of entities" : {
        "datatype": XSD.integer,
        "access_methods": [VO, SPA],
        "dimension": "Amount of data",
    },

    "Modification date": {
        "datatype": XSD.string,
        "access_methods": [SPA, VO],
        "dimension": "Currency",
    },

    " Number of triples (metadata)": {
        "datatype": XSD.integer,
        "access_methods": [META, SPA],
        "dimension": "Amount of data",
    },

    "Number of property": {
        "datatype": XSD.integer,
        "access_methods": [SPA, VO],
        "dimension": "Amount of data",
    },

    "Signed": {
        "datatype": XSD.boolean,
        "access_methods": [META],
        "dimension": "Verifiability",
    },

    " Number of triples": {
        "datatype": XSD.integer,
        "access_methods": [META],
        "dimension": "Amount of data", 
    },

    "Number of triples (query)": {
        "datatype": XSD.integer,
        "access_methods": [SPA],
        "dimension": "Amount of data",
    },

	"Degree of connection": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Number of triples linked": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"U1-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"CS2-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"IN3-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"RC1-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"RC2-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"IN4-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"U5-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"PE2-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"PE3-value": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"F1-M Unique and persistent ID": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"F1-D URIs dereferenceability": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"F2a-M - Metadata availability via standard primary sources": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"F2b-M Metadata availability for all the attributes covered in the FAIR score computation": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"F3-M Data referrable via a DOI": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"F4-M Metadata registered in a searchable engine": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"A1-D Working access point(s)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"A1-M Metadata availability via working primary sources": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"A1.2 Authentication & HTTPS support": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"A2-M Registered in search engines": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"R1.1 Machine- or human-readable license retrievable via any primary source": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"R1.2 Publisher information such as authors-contributors-publishers and sources": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"R1.3-D Data organized in a standardized way": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"R1.3-M Metadata are described with VoID/DCAT predicates": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"I1-D Standard & open representation format": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"I1-M Metadata are described with VoID/DCAT predicates": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"I2 Use of FAIR vocabularies": {
		"datatype": XSD.decimal,
		"access_methods": [UN],
		"dimension": "",
	},

	"I3-D Degree of connection": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Percentage of data updated": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Average length of URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Standard deviation lenght URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Min length URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"25th percentile length URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Median length URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"75th percentile length URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Max length URIs (subject)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Average length of URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Standard deviation lenght URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Min length URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"25th percentile length URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Median length URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"75th percentile length URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Max length URIs (predicate)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Average length of URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Standard deviation lenght URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Min length URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"25th percentile length URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Median length URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"75th percentile length URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Max length URIs (object)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Use RDF structures": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Minimum latency": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"25th percentile latency": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"75th percentile latency": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Maximum latency": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Minimum throughput": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"25th percentile throughput": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"75th percentile throughput": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Maximum throughput": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Number of samAs chains": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Number of labels/comments present on the data": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	" Percentage of triples with labels": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Regex uri": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Number of blank nodes": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Deprecated classes/properties used": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Triples with misplaced property problem": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Triples with misplaced class problem": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Undefined class used without declaration": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Undefined properties used without declaration": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Extensional conciseness": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Intensional conciseness": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Triples with empty annotation problem": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Triples with white space in annotation(at the beginning or at the end)": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Triples with malformed data type literals problem": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Functional properties with inconsistent values": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Invalid usage of inverse-functional properties": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Number of triples updated": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"MinTPNoOff": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"MeanTPNoOff": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"MaxTPNoOff": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"sdTPNoOff": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Entities as member of disjoint class": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"New vocabularies defined in the dataset": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"New terms defined in the dataset": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Time elapsed since last modification": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Historical updates": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Number of entities counted with regex": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

	"Url file VoID": {
		"datatype": XSD.string,
		"access_methods": [UN],
		"dimension": "",
	},

}