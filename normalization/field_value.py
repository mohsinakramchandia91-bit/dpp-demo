class FieldValue:
    """
    FieldValue = value + truth metadata
    """

    def __init__(self, value, unit=None, source=None, confidence=0):
        self.value = value
        self.unit = unit
        self.source = source
        self.confidence = confidence

    def to_dict(self):
        return {
            "value": self.value,
            "unit": self.unit,
            "source": self.source,
            "confidence": self.confidence
        }
