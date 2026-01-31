def calculate_batch_confidence(batch_view, critical_fields):
    confidences = []

    for field in critical_fields:
        data = batch_view.get(field)

        if data is None:
            # Missing critical field = zero trust
            return 0

        confidences.append(data.get("confidence", 0))

    # Conservative rule: weakest link
    return min(confidences)
