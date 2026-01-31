from datetime import datetime
import uuid
from lifecycle.timeline import load_timeline

class DPP:
    def __init__(self, product_id, batch_id, version, batch_view, compliance_report):
        self.dpp_id = str(uuid.uuid4())
        self.product_id = product_id
        self.batch_id = batch_id
        self.version = version
        self.created_at = datetime.utcnow().isoformat()
        self.batch_view = batch_view
        self.compliance_report = compliance_report
        self.timeline = load_timeline(product_id)

    def to_dict(self):
        return {
            "dpp_id": self.dpp_id,
            "product_id": self.product_id,
            "batch_id": self.batch_id,
            "version": self.version,
            "created_at": self.created_at,
            "batch_view": self.batch_view,
            "compliance_report": self.compliance_report,
            "lifecycle_timeline": self.timeline
        }
