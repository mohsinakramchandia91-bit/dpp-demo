def get_branding(company_id):
    BRANDING = {
        "cmp_edc3151e": {
            "company_name": "Pak Textile Ltd",
            "logo_url": "https://via.placeholder.com/140x40?text=PAK+TEXTILE",
            "primary_color": "#0f766e",
            "footer": "© 2026 Pak Textile Ltd – Verified Supply Chain"
        },
        "default": {
            "company_name": "Digital Product Passport",
            "logo_url": "",
            "primary_color": "#2563eb",
            "footer": "Independent verification supported"
        }
    }
    return BRANDING.get(company_id, BRANDING["default"])
