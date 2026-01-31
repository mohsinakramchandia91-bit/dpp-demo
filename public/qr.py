import os

QR_DIR = "data/qr"

def generate_qr(public_path):
    os.makedirs(QR_DIR, exist_ok=True)

    text = f"OPEN DPP:\n{public_path}"
    filename = os.path.basename(public_path).replace(".html", ".txt")
    path = os.path.join(QR_DIR, filename)

    with open(path, "w") as f:
        f.write(text)

    return path
