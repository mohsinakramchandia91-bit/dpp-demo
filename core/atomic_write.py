import os
import json
import tempfile

def atomic_json_write(path, data):
    dir_name = os.path.dirname(path)

    with tempfile.NamedTemporaryFile(
        mode="w",
        dir=dir_name,
        delete=False
    ) as tmp:
        json.dump(data, tmp)
        tmp_path = tmp.name

    os.replace(tmp_path, path)
