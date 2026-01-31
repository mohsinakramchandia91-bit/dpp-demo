from normalization.pipeline import process_event
from normalization.batch_aggregator import aggregate_batch
from compliance.engine import evaluate
from dpp.builder import build_dpp
from public.generator import generate_public_view
from public.qr import generate_qr
from proof.generator import generate_proof
from audit.builder import build_audit_package
from audit.zipper import zip_audit_package


def run_operator_flow(product_id, batch_id, payload, source_type, factory_id):
    # 1. Normalize input event
    process_event(
        type("E", (), {
            "source_type": source_type,
            "payload": payload,
            "factory_id": factory_id,
            "batch_id": batch_id
        })()
    )

    # 2. Aggregate batch data
    batch_view = aggregate_batch(factory_id, batch_id)

    # 3. Compliance evaluation
    compliance = evaluate(batch_view)

    # 4. Build DPP  ✅ FIX HERE (factory_id added)
    dpp_path, dpp = build_dpp(
        factory_id=factory_id,
        product_id=product_id,
        batch_id=batch_id,
        batch_view=batch_view,
        compliance_report=compliance
    )

    # 5. Public HTML
    public_path = generate_public_view(dpp)

    # 6. QR (text-based, portable)
    qr_path = generate_qr(public_path)

    # 7. Proof
    hash_value, proof_path = generate_proof(dpp)

    # 8. Audit folder
    build_audit_package(
        product_id=product_id,
        version=dpp.version,
        paths={
            "dpp": dpp_path,
            "proof": proof_path,
            "public": public_path,
            "qr": qr_path
        }
    )

    # 9. Audit ZIP
    zip_path = zip_audit_package(product_id, dpp.version)

    return {
        "product_id": product_id,
        "batch_id": batch_id,
        "factory_id": factory_id,
        "version": dpp.version,
        "status": compliance.get("status"),
        "public_view": public_path,
        "qr": qr_path,
        "hash": hash_value,
        "proof": proof_path,
        "audit_package": zip_path,
        "risks": compliance.get("risks", []),
        "guidance": compliance.get("guidance", [])
    }

# 10. White-label buyer page
from buyer.view import generate_verify_page

verify_page = generate_verify_page(
    company_id=factory_id,
    product_id=product_id,
    version=dpp.version
)

result["buyer_verify"] = verify_page

# 11. Domain-based buyer page
from buyer.view import generate_verify_page

verify_page = generate_verify_page(
    company_id=factory_id,
    product_id=product_id,
    version=dpp.version
)

result["buyer_verify"] = verify_page
