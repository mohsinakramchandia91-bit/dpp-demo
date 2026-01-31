from normalization.field_value import FieldValue
from normalization.confidence import base_confidence

def normalize_raw_event(raw_event):
    normalized = {}

    for key, value in raw_event.payload.items():
        confidence = base_confidence(raw_event.source_type, value)

        normalized[key] = FieldValue(
            value=value,
            unit=None,
            source=raw_event.source_type,
            confidence=confidence
        )

    return normalized
