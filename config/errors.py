"""
    Definizioni errori HTTP
"""

ERROR_DEFINITIONS = {
    403: "Error 403: Forbidden - Not authorized",
    404: "Error 404: Not Found",
    500: "Error 500: Internal Server Error",
    502: "HTTP Error 502: Bad Gateway",
    503: "Error 503: Service Unavailable",
    504: "HTTP Error 504: Gateway Timeout",
    524: "HTTP Error 524: unknown",
}

SPECIAL_MAPPING = {
    "impossible to verify": "403",
    "unable to retrieve properties from the endpoint": "404",
    "unable to retrieve classes from the endpoint": "404",
    "no dump available": "404",
    "unable": "404",
    "invalid-uri": "404"
}