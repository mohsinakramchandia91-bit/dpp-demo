import json

def safe_json_load(payload_str):
    try:
        return json.loads(payload_str), None
    except Exception as e:
        return None, f"Invalid JSON payload: {str(e)}"
