from lifecycle.dpp import DPP
from lifecycle.versioning import next_version
from lifecycle.storage import save_dpp

def build_dpp(product_id, batch_id, batch_view, compliance_report):
    version = next_version(product_id)

    dpp = DPP(
        product_id=product_id,
        batch_id=batch_id,
        version=version,
        batch_view=batch_view,
        compliance_report=compliance_report
    )

    path = save_dpp(dpp)
    return path, dpp
