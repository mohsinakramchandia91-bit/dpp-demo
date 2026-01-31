from saas.context import with_company
from saas.guard import enforce_all
from core.operator import run_operator_flow

def run_as_company(company_id, product_id, batch_id, payload):
    factory_id = company_id

    env = with_company(company_id)

    # 🚨 HARD ENFORCEMENT
    enforce_all(company_id, env["PLAN"])

    for k, v in env.items():
        globals()[k] = v

    return run_operator_flow(
        product_id=product_id,
        batch_id=batch_id,
        payload=payload,
        source_type="manual",
        factory_id=factory_id
    )
