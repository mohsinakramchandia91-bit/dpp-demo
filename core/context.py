import os

ENV_FACTORY = "LDCE_FACTORY_ID"

def get_factory_id():
    fid = os.environ.get(ENV_FACTORY)
    if not fid:
        raise RuntimeError(
            f"Factory not set. Run:\n"
            f"export {ENV_FACTORY}=YOUR_FACTORY_ID"
        )
    return fid
