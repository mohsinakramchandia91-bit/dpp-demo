# Simple, explainable country risk levels
# Source: public perception / regulatory guidance (not paid data)

COUNTRY_RISK = {
    "PK": "MEDIUM",
    "IN": "MEDIUM",
    "BD": "MEDIUM",
    "VN": "LOW",
    "TR": "LOW",
    "CN": "HIGH",
    "UZ": "HIGH",
    "TM": "HIGH"
}

def country_risk(country_code):
    return COUNTRY_RISK.get(country_code, "UNKNOWN")
