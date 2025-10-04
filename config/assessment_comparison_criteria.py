"""
Attributi da considerare per determinare se due assessment sono identici.
Include tutti gli attributi con access_methods che contengono META più lo Sparql endpoint.
"""

assessment_comparison_criteria = [
    "Sparql endpoint",
    "Offline dumps",
    "Contributor",
    "Dataset update frequency",
    "Sources",
    "Publisher",
    "Author (metadata)",
    "License machine redeable (metadata)",
    "Requires authentication",
    "Availability of a common accepted Media Type",
    "Availability of RDF dump (metadata)",
    "Inactive links",
    "Availability VoID file",
    "Uses RDF structures",
    "Is on a trusted provider list",
    "Presence of example",
    "metadata-media-type",
    "Serialization formats",
]