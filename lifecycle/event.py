from datetime import datetime

class LifecycleEvent:
    def __init__(self, event_type, details):
        self.event_type = event_type
        self.details = details
        self.timestamp = datetime.utcnow().isoformat()

    def to_dict(self):
        return {
            "type": self.event_type,
            "details": self.details,
            "timestamp": self.timestamp
        }
