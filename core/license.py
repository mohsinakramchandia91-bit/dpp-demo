import os
import sys

def require_license():
    factory_id = os.environ.get("LDCE_FACTORY_ID")

    if not factory_id:
        print("ERROR: LDCE_FACTORY_ID not set")
        sys.exit(1)

    if not factory_id.startswith("PK-"):
        print("ERROR: Invalid factory license")
        sys.exit(1)

    return factory_id
