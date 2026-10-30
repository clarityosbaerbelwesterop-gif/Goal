"""
Readiness checker for the pure software training machine.
Verifies all components are wired before start.
"""

class ReadinessChecker:
    def __init__(self, machine):
        self.machine = machine

    def check(self) -> dict:
        checks = {
            "model": self.machine.model is not None,
            "tokenizer": self.machine.tokenizer is not None,
            "router": self.machine.router is not None,
            "data_loader": self.machine.data_loader is not None,
            "reasoning": self.machine.reasoning is not None,
            "learning": self.machine.learning is not None,
            "checkpoint_manager": self.machine.checkpoint_manager is not None,
            "mesh": self.machine.mesh is not None,
            "software_only": True,
        }
        all_ready = all(checks.values())
        return {
            "ready": all_ready,
            "checks": checks,
            "message": "System ready for software-only training start" if all_ready else "Missing components",
        }
