dimensions = {
    "Unknown": {
        "category": "Uncategorized",
        "definition": "Unspecified dimension or generic default category.",
    },

    "Availability": {
        "category": "Accessibility",
        "definition": "The extent to which data (or the SPARQL endpoint) is present, retrievable, and ready for use.",
    },

    "Licensing": {
        "category": "Accessibility",
        "definition": "The explicit provision of machine-readable or human-readable information granting permission to use and reuse the data.",
    },

    "Interlinking": {
        "category": "Accessibility",
        "definition": "The degree to which entities in the dataset are connected to entities in external datasets, facilitating navigation and discovery.",
    },

    "Security": {
        "category": "Accessibility",
        "definition": "The extent to which data access is restricted to authorized users to prevent misuse or alteration (e.g., via HTTPS or authentication).",
    },

    "Performance": {
        "category": "Accessibility",
        "definition": "The efficiency of the system in responding to requests, typically measured by latency or throughput of the endpoint.",
    },

    "Semantic Accuracy": {
        "category": "Intrinsic",
        "definition": "The degree to which data values correctly represent the real-world facts or objects they are meant to describe.",
    },

    "Consistency": {
        "category": "Intrinsic",
        "definition": "The absence of logical contradictions or format violations within the data and with respect to the schema.",
    },

    "Conciseness": {
        "category": "Intrinsic",
        "definition": "The extent to which the data is free of redundancy, both at the schema level (intensional) and data level (extensional).",
    },

    "Reputation": {
        "category": "Trust",
        "definition": "The level of trust or reliability associated with the data provider or the dataset's origin.",
    },

    "Believability": {
        "category": "Trust",
        "definition": "The degree to which the information is accepted as true, real, and credible by the user.",
    },

    "Verifiability": {
        "category": "Trust",
        "definition": "The degree to which a user can inspect the data and its provenance to verify its correctness.",
    },

    "Currency": {
        "category": "Dataset dynamicity",
        "definition": "The speed at which the data is updated following changes in the real world (data freshness).",
    },

    "Timeliness": {
        "category": "Dataset dynamicity",
        "definition": "The extent to which the data is available and valid at the specific time it is needed for a task.",
    },

    "Completeness": {
        "category": "Contextual",
        "definition": "The degree to which all required information is present in the dataset without significant gaps regarding the specific domain.",
    },

    "Amount of data": {
        "category": "Contextual",
        "definition": "The volume or quantity of available data (e.g., number of triples), used to assess the scope of coverage.",
    },

    "Representational-conciseness": {
        "category": "Representational",
        "definition": "The extent to which the data representation is compact, using efficient structures and short URIs.",
    },

    "Interoperability": {
        "category": "Representational",
        "definition": "The ability of systems to exchange and make use of the data, facilitated by the adoption of shared standards.",
    },

    "Understandability": {
        "category": "Representational",
        "definition": "The ease with which a human consumer can comprehend the data, supported by adequate labels and descriptions.",
    },

    "Interpretability": {
        "category": "Representational",
        "definition": "The ability of the data to be correctly interpreted and processed by machines (e.g., correct usage of RDF types).",
    },

    "Versatility": {
        "category": "Representational",
        "definition": "The availability of the data in different serialization formats (e.g., JSON-LD, Turtle) or through different access methods.",
    },
}