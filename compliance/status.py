def compliance_status(batch_confidence, risks):
    if batch_confidence == 0:
        return "FAIL"

    if risks:
        return "WARN"

    return "PASS"
