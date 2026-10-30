"""
Training Machine: full orchestrator for data processing, training,
reasoning, and learning on the digital datacenter.
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
    ):
        self.model = model
        self.tokenizer = tokenizer
        self.router = router
        self.data_loader = data_loader
        self.reasoning = reasoning_module
        self.learning = learning_module
        self.checkpoint_manager = checkpoint_manager
        self.mesh = mesh
        self.global_step = 0
        self.stage = 1

    def run(self, max_steps: int = 10000, stage: int = 1):
        """
        Main training loop.
        Scales over the virtual mesh.
        """
        self.stage = stage
        self.data_loader.set_stage(stage)
        print(f"Starting Training Machine - Stage {stage} on mesh {self.mesh}")

        for batch in self.data_loader:
            if self.global_step >= max_steps:
                break

            # Data processing
            if not hasattr(self, "processor") or self.processor.filter_premium(batch):
                depth = self.reasoning.compute_reasoning_depth(
                    batch.get("difficulty", 0.5), batch.get("domain", "general")
                )

                # Forward
                encoded = self.tokenizer.encode(batch["text"])
                output = self.model.forward(
                    encoded["fine_tokens"], tempo=depth, domain=batch.get("domain")
                )

                # Reasoning & Learning signals
                trace = self.reasoning.generate_verifiable_trace(output)
                experts = self.router.route(tempo=depth, domain=batch.get("domain"))
                self.learning.specialize_experts(batch.get("domain", "general"), experts)
                adapt_loss = self.learning.meta_adapt(batch)

                # Checkpoint periodically
                if self.global_step % 1000 == 0:
                    self.checkpoint_manager.save_async(
                        self.global_step,
                        {"step": self.global_step, "stage": self.stage},
                        mesh_shape=getattr(self.mesh, "shape", (8, 8, 8)),
                    )

                self.global_step += 1

                if self.global_step % 100 == 0:
                    print(f"Step {self.global_step} | Tempo {depth:.2f} | Domain {batch.get('domain')}")

        print(f"Training stage {stage} complete at step {self.global_step}")
        return {"final_step": self.global_step, "stage": stage}

    def advance_stage(self):
        self.stage += 1
        print(f"Advanced to training stage {self.stage}")
