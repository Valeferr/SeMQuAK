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

}