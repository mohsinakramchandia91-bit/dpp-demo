import os
import time

LOCK_DIR = "data/locks"

def ensure_lock_dir():
    os.makedirs(LOCK_DIR, exist_ok=True)

def lock_path(name):
    return os.path.join(LOCK_DIR, f"{name}.lock")

def acquire_lock(name, timeout=5):
    ensure_lock_dir()
    path = lock_path(name)
    start = time.time()

    while True:
        try:
            fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.close(fd)
            return True
        except FileExistsError:
            if time.time() - start > timeout:
                raise TimeoutError(f"Lock timeout: {name}")
            time.sleep(0.05)

def release_lock(name):
    path = lock_path(name)
    if os.path.exists(path):
        os.remove(path)
