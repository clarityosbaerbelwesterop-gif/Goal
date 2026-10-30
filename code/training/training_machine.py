"""
Training Machine: full pure-software orchestrator.
No GPUs, TPUs, or hardware required.
"""

from typing import Optional

class TrainingMachine:
    def __init__(
        self,
        model,
        tokenizer,
        router,
        data_loader,
        reasoning_module,
        learning_module,
        checkpoint_manager,
        mesh,
        simulator=None,
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.router = router
        self.data_loader = data_loader
        self.reasoning = reasoning_module
        self.learning = learning_module
        self.checkpoint_manager = checkpoint_manager
        self.mesh = mesh
        self.simulator = simulator
        self.global_step = 0
        self.stage = 1
        self.running = False

    def run(self, max_steps: int = 10000, stage: int = 1):
        """
        Main pure-software training loop.
        """
        self.stage = stage
        self.running = True
        self.data_loader.set_stage(stage)
        print(f"[SOFTWARE-ONLY] Starting Training Machine - Stage {stage}")
        print(f"Mesh: {getattr(self.mesh, 'shape', 'virtual')} | Mode: pure software")

        data_iter = iter(self.data_loader)
        while self.global_step < max_steps and self.running:
            try:
                batch = next(data_iter)
            except StopIteration:
                break

            depth = self.reasoning.compute_reasoning_depth(
                batch.get("difficulty", 0.5), batch.get("domain", "general")
            )

            encoded = self.tokenizer.encode(batch["text"])
            output = self.model.forward(
                encoded["fine_tokens"], tempo=depth, domain=batch.get("domain")
            )

            # Software collectives (if simulator present)
            if self.simulator:
                output = self.simulator.all_reduce(output)

            trace = self.reasoning.generate_verifiable_trace(output)
            experts = self.router.route(tempo=depth, domain=batch.get("domain"))
            self.learning.specialize_experts(batch.get("domain", "general"), experts)
            self.learning.meta_adapt(batch)

            if self.global_step % 1000 == 0:
                self.checkpoint_manager.save_async(
                    self.global_step,
                    {"step": self.global_step, "stage": self.stage, "mode": "software"},
                    mesh_shape=getattr(self.mesh, "shape", (8, 8, 8)),
                )

            self.global_step += 1

            if self.global_step % 100 == 0:
                eff = self.simulator.simulate_step_overhead() if self.simulator else 1.0
                print(f"Step {self.global_step} | Tempo {depth:.2f} | Domain {batch.get('domain')} | Eff ~{eff}x")

        self.running = False
        print(f"[SOFTWARE-ONLY] Stage {stage} complete at step {self.global_step}")
        return {"final_step": self.global_step, "stage": stage, "mode": "pure_software"}

    def stop(self):
        self.running = False

    def advance_stage(self):
        self.stage += 1
        print(f"Advanced to stage {self.stage}")
