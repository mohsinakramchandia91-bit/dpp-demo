import sys
from auditor.verifier import verify_dpp


def main():
    if len(sys.argv) != 3:
        print("Usage: python -m auditor.cli <PRODUCT_ID> <VERSION>")
        sys.exit(1)

    product_id = sys.argv[1]
    version = sys.argv[2]

    valid, message = verify_dpp(product_id, version)

    print("\n--- AUDITOR VERIFICATION RESULT ---")
    print(f"Product ID : {product_id}")
    print(f"Version    : {version}")
    print(f"Result     : {'PASS' if valid else 'FAIL'}")
    print(f"Message    : {message}")


if __name__ == "__main__":
    main()
