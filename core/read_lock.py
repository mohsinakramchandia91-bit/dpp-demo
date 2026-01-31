from core.file_lock import acquire_lock, release_lock

def with_read_lock(name, fn):
    acquire_lock(name)
    try:
        return fn()
    finally:
        release_lock(name)
