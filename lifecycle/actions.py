from lifecycle.event import LifecycleEvent
from lifecycle.timeline import append_event

def record_repair(product_id, repair_details):
    event = LifecycleEvent("REPAIR", repair_details)
    return append_event(product_id, event)

def record_export(product_id, export_details):
    event = LifecycleEvent("RE_EXPORT", export_details)
    return append_event(product_id, event)

def record_recycle(product_id, recycle_details):
    event = LifecycleEvent("RECYCLE", recycle_details)
    return append_event(product_id, event)
