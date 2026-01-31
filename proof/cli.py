import sys

# IMPORTANT: relative import
from .verifier import verify_dpp

def main():
    if len(sys.argv) != 3:
        print("Usage: python -m proof.cli <PRODUCT_ID> <VERSION>")
        sys.exit(1)

    product_id = sys.argv[1]
    version = sys.argv[2]

    valid, message = verify_dpp(product_id, version)

    print("\n--- DPP VERIFICATION RESULT ---")
    print("Product ID:", product_id)
    print("Version:", version)
    print("Result:", "PASS" if valid else "FAIL")
    print("Message:", message)

if __name__ == "__main__":
    main()
