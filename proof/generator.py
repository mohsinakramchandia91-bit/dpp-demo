from proof.hash_utils import compute_hash
from proof.storage import save_proof

def generate_proof(dpp_obj):
    dpp_dict = dpp_obj.to_dict()
    hash_value = compute_hash(dpp_dict)

    path = save_proof(
        product_id=dpp_obj.product_id,
        version=dpp_obj.version,
        hash_value=hash_value
    )

    return hash_value, path
