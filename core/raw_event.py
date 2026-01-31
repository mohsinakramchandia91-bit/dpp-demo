from datetime import datetime
import uuid

class RawEvent:
    """
    RawEvent = system ki aankh
    Jo mila, jaisa mila, waisa hi store hota hai
    """

    def __init__(self, source_type, payload, factory_id, batch_id):
        self.event_id = str(uuid.uuid4())
        self.source_type = source_type
        self.payload = payload
        self.factory_id = factory_id
        self.batch_id = batch_id
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "source_type": self.source_type,
            "payload": self.payload,
            "factory_id": self.factory_id,
            "batch_id": self.batch_id,
            "timestamp": self.timestamp
        }
