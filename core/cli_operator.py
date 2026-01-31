import sys
import json
import os
from core.operator import run_operator_flow

def main():
    if len(sys.argv) != 4:
        print("Usage: python -m core.cli_operator <PRODUCT_ID> <BATCH_ID> <PAYLOAD_JSON>")
        sys.exit(1)

    product_id = sys.argv[1]
    batch_id = sys.argv[2]
    payload = json.loads(sys.argv[3])

    factory_id = os.environ.get("LDCE_FACTORY_ID")
    if not factory_id:
        print("ERROR: LDCE_FACTORY_ID environment variable not set")
        sys.exit(1)

    result = run_operator_flow(
        product_id=product_id,
        batch_id=batch_id,
        payload=payload,
        source_type="manual",
        factory_id=factory_id
    )

    print("\n--- OPERATOR RESULT ---")
    for k, v in result.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
