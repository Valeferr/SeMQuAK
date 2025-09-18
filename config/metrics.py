from config.namespaces import META, SPA, VO, UN
from rdflib.namespace import XSD

"""
    Definizione delle metriche
"""

metrics = {
    "SKOS mapping properties": {
        "datatype": XSD.integer,
        "access_methods": [SPA],
    },

    "Standard deviation of latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
    },

    " Standard deviation of throughput": {
        "datatype": XSD.decimal,
        "access_methods": [META],
    },

    "Average latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
    },

    "Average throughput": {
        "datatype": XSD.decimal,
        "access_methods": [META],
    },

    "Median latency": {
        "datatype": XSD.decimal,
        "access_methods": [META],
    },

    "Median throughput": {
         "datatype": XSD.decimal,
        "access_methods": [META],
    },

    "Centrality": {
        "datatype": XSD.decimal,
        "access_methods": [META],
    },

    "Clustering coefficient": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    },

    "PageRank": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    },

    "Trust value": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    },

    "Interlinking completeness": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    },

    "URIs Deferenceability": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    },

    "FAIR score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "F score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 

    "A score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "R score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "I score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "Score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 

    "Normalized score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    },

    "Availability score": {
        "datatype": XSD.decimal,
        "access_methods": [META, SPA, VO]
    }, 
    
    "Licensing score": {
        "datatype": XSD.decimal,
        "access_methods": [META, SPA, VO]
    },
    
    "Interlinking score": {
        "datatype": XSD.decimal,
        "access_methods": [META, SPA]
    }, 
    
    "Performance score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA]
    }, 
    
    "Accuracy score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA],
    },
    
    "Consistency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA]
    }, 

    "Conciseness score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "Verifiability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, VO]
    },

    "Reputation score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "Believability score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "Currency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, VO]
    },

    "Volatility score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "Completeness score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    }, 
    
    "Amount of data score": {
        "datatype": XSD.decimal,
        "access_methods": [META]
    },
    
    "Representational-Consistency score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA]
    }, 
    
    "Representational-Conciseness score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA]
    },
    
    "Understandability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA, META, VO]
    },  
    
    "Interpretability score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA]
    }, 
    
    "Versatility score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA]
    },
    
    "Security score": {
        "datatype": XSD.decimal,
        "access_methods": [SPA]
    },

    "Number of entities" : {
        "datatype": XSD.integer,
        "access_methods": [VO, SPA]
    },

    "Modification date": {
        "datatype": XSD.string,
        "access_methods": [SPA, VO]
    },

    " Number of triples (metadata)": {
        "datatype": XSD.integer,
        "access_methods": [META, SPA],
    },

    "Number of property": {
        "datatype": XSD.integer,
        "access_methods": [SPA, VO]
    },

    "Signed": {
        "datatype": XSD.boolean,
        "access_methods": [META]
    },

    " Number of triples": {
        "datatype": XSD.integer,
        "access_methods": [META] 
    },

    "Number of triples (query)": {
        "datatype": XSD.integer,
        "access_methods": [SPA]
    },

}