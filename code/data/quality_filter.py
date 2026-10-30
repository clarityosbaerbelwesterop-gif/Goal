"""
Premium data quality filter.
"""

class QualityFilter:
    def __init__(self):
        self.rejected = 0
        self.accepted = 0

    def accept(self, sample: dict) -> bool:
        text = sample.get("text", "")
        if len(text) < 20:
            self.rejected += 1
            return False
        if sample.get("verifiable", False) or sample.get("difficulty", 0) > 0.3:
            self.accepted += 1
            return True
        self.rejected += 1
        return False

    def stats(self):
        return {"accepted": self.accepted, "rejected": self.rejected}
