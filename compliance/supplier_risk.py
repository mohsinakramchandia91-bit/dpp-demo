from compliance.country_risk import country_risk

def evaluate_supplier_risk(batch_view):
    risks = []

    origin = batch_view.get("origin_country")
    material = batch_view.get("material")

    if origin:
        level = country_risk(origin.get("value"))

        if level == "HIGH":
            risks.append(
                f"High-risk origin country detected ({origin.get('value')})"
            )

    if material and origin:
        if material.get("value") == "cotton" and country_risk(origin.get("value")) == "HIGH":
            risks.append(
                "Cotton sourced from high-risk region – enhanced due diligence required"
            )

    return risks
