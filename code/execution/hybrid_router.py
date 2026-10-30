"""
Hybrid router: decides between code execution and neural/simulated path.
"""

class HybridRouter:
    def __init__(self):
        self.code_tasks = {"sort", "parse", "calculate", "verify", "format"}

    def route(self, task_type: str, complexity: float) -> str:
        if task_type in self.code_tasks or complexity < 0.3:
            return "code"
        if complexity > 0.8:
            return "remote_or_heavy"
        return "light_neural"

    def execute_code_path(self, task: str, data):
        # Placeholder for deterministic execution
        return {"result": f"executed_{task}", "compute": "cpu_minimal"}
