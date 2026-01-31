from compliance.batch_confidence import calculate_batch_confidence
from compliance.risk_engine import evaluate_risks
from compliance.status import compliance_status
from compliance.critical_fields import CRITICAL_FIELDS
from compliance.guidance import guidance_for_risks

def evaluate(batch_view):
    """
    Main compliance evaluation entrypoint
    """

    batch_conf = calculate_batch_confidence(batch_view, CRITICAL_FIELDS)
    risks = evaluate_risks(batch_view, CRITICAL_FIELDS)
    status = compliance_status(batch_conf, risks)

    return {
        "batch_confidence": batch_conf,
        "status": status,
        "risks": risks,
        "guidance": guidance_for_risks(risks)
    }
