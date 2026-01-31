from core.raw_event import RawEvent
from core.storage import save_raw_event

def smoke_test():
    payload = {
        "material": "cotton",
        "cotton_percent": None,
        "energy_source": "unknown"
    }

    event = RawEvent(
        source_type="manual",
        payload=payload,
        factory_id="PK-FACTORY-001",
        batch_id="BATCH-0001"
    )

    save_raw_event(event)
    print("RawEvent saved")
    print(event.to_dict())

if __name__ == "__main__":
    smoke_test()

from normalization.normalizer import normalize_raw_event

def normalization_test():
    payload = {
        "material": "cotton",
        "cotton_percent": None,
        "energy_source": "unknown"
    }

    event = RawEvent(
        source_type="manual",
        payload=payload,
        factory_id="PK-FACTORY-001",
        batch_id="BATCH-0002"
    )

    normalized = normalize_raw_event(event)

    print("\n--- NORMALIZED OUTPUT ---")
    for k, v in normalized.items():
        print(k, "=>", v.to_dict())

if __name__ == "__main__":
    normalization_test()

from normalization.pipeline import process_event

def day3_test():
    payload = {
        "material": "cotton",
        "cotton_percent": None,
        "energy_source": "unknown"
    }

    event = RawEvent(
        source_type="manual",
        payload=payload,
        factory_id="PK-FACTORY-001",
        batch_id="BATCH-0003"
    )

    path = process_event(event)
    print("\n--- DAY 3 NORMALIZED SAVED ---")
    print("Saved at:", path)

if __name__ == "__main__":
    day3_test()

from normalization.batch_aggregator import aggregate_batch

def day4_test():
    batch_id = "BATCH-0003"
    aggregated = aggregate_batch(batch_id)

    print("\n--- DAY 4 BATCH AGGREGATED VIEW ---")
    for k, v in aggregated.items():
        print(k, "=>", v)

if __name__ == "__main__":
    day4_test()

from normalization.batch_aggregator import aggregate_batch
from compliance.critical_fields import CRITICAL_FIELDS
from compliance.batch_confidence import calculate_batch_confidence
from compliance.risk_engine import evaluate_risks
from compliance.status import compliance_status

def day5_test():
    batch_id = "BATCH-0003"
    batch_view = aggregate_batch(batch_id)

    batch_conf = calculate_batch_confidence(batch_view, CRITICAL_FIELDS)
    risks = evaluate_risks(batch_view, CRITICAL_FIELDS)
    status = compliance_status(batch_conf, risks)

    print("\n--- DAY 5 COMPLIANCE REPORT ---")
    print("Batch ID:", batch_id)
    print("Batch Confidence:", batch_conf)
    print("Status:", status)
    print("Risks:")
    for r in risks:
        print("-", r)

if __name__ == "__main__":
    day5_test()

from lifecycle.builder import build_dpp

def day6_test():
    batch_id = "BATCH-0003"
    product_id = "PRODUCT-TSHIRT-001"

    batch_view = aggregate_batch(batch_id)

    batch_conf = calculate_batch_confidence(batch_view, CRITICAL_FIELDS)
    risks = evaluate_risks(batch_view, CRITICAL_FIELDS)
    status = compliance_status(batch_conf, risks)

    compliance_report = {
        "batch_confidence": batch_conf,
        "status": status,
        "risks": risks
    }

    path, dpp = build_dpp(
        product_id=product_id,
        batch_id=batch_id,
        batch_view=batch_view,
        compliance_report=compliance_report
    )

    print("\n--- DAY 6 DPP CREATED ---")
    print("Saved at:", path)
    print("DPP Version:", dpp.version)
    print("DPP Status:", status)

if __name__ == "__main__":
    day6_test()

from output.public_view import generate_public_view

def day7_test():
    batch_id = "BATCH-0003"
    product_id = "PRODUCT-TSHIRT-001"

    batch_view = aggregate_batch(batch_id)

    batch_conf = calculate_batch_confidence(batch_view, CRITICAL_FIELDS)
    risks = evaluate_risks(batch_view, CRITICAL_FIELDS)
    status = compliance_status(batch_conf, risks)

    compliance_report = {
        "batch_confidence": batch_conf,
        "status": status,
        "risks": risks
    }

    path, dpp = build_dpp(
        product_id=product_id,
        batch_id=batch_id,
        batch_view=batch_view,
        compliance_report=compliance_report
    )

    public_path = generate_public_view(dpp)

    print("\n--- DAY 7 PUBLIC DPP GENERATED ---")
    print("Public view saved at:", public_path)

if __name__ == "__main__":
    day7_test()

from proof.generator import generate_proof

def day8_test():
    batch_id = "BATCH-0003"
    product_id = "PRODUCT-TSHIRT-001"

    batch_view = aggregate_batch(batch_id)

    batch_conf = calculate_batch_confidence(batch_view, CRITICAL_FIELDS)
    risks = evaluate_risks(batch_view, CRITICAL_FIELDS)
    status = compliance_status(batch_conf, risks)

    compliance_report = {
        "batch_confidence": batch_conf,
        "status": status,
        "risks": risks
    }

    path, dpp = build_dpp(
        product_id=product_id,
        batch_id=batch_id,
        batch_view=batch_view,
        compliance_report=compliance_report
    )

    hash_value, proof_path = generate_proof(dpp)

    print("\n--- DAY 8 DPP PROOF GENERATED ---")
    print("DPP Version:", dpp.version)
    print("Hash:", hash_value)
    print("Proof saved at:", proof_path)

if __name__ == "__main__":
    day8_test()
