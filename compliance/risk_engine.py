def evaluate_risks(batch_view, critical_fields):
    risks = []

    for field in critical_fields:
        data = batch_view.get(field)

        if data is None:
            risks.append(f"{field} is missing")
            continue

        if data.get("confidence", 0) < 40:
            risks.append(f"{field} confidence too low ({data.get('confidence')})")

    return risks
