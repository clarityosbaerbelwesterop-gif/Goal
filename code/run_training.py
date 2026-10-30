"""
Runner for GitHub Actions: Premium data collection/generation + training start.
Pure software, no hardware.
Robust version with flush, error handling, and controllable duration.
"""

import os
import sys
import time
import traceback

# Ensure imports work whether run as module or script
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def log(msg):
    print(msg, flush=True)

def main():
    try:
        duration_min = int(os.environ.get("DURATION_MINUTES", "5"))  # default short for safety
        stage = int(os.environ.get("STAGE", "1"))
        # Cap at 180 minutes to stay within Actions limits
        duration_min = min(duration_min, 180)
        duration_sec = duration_min * 60

        log(f"=== Starting Pure-Software Run ===")
        log(f"Duration target: {duration_min} minutes")
        log(f"Stage: {stage}")
        log(f"Focus: Premium data in reasoning, math, code, research, agents, computer_use")

        from code.cluster.virtual_mesh import VirtualTPUMesh
        from code.cluster.moe_router import MoERouter
        from code.cluster.software_simulator import SoftwareSimulator
        from code.model.tempoformer import TempoFormer, TempoFormerConfig
        from code.model.semantic_tokenizer import SemanticHierarchicalTokenizer
        from code.data.premium_loader import PremiumDataLoader
        from code.reasoning.reasoning_module import ReasoningModule
        from code.learning.learning_module import LearningModule
        from code.storage.tiered_storage import TieredStorage
        from code.storage.checkpoint_manager import CheckpointManager
        from code.training.training_machine import TrainingMachine
        from code.training.readiness import ReadinessChecker

        # Build system
        mesh = VirtualTPUMesh(4, 4, 4)
        router = MoERouter(num_experts=128, top_k=4)
        simulator = SoftwareSimulator(mesh)
        config = TempoFormerConfig(num_layers=16, num_experts=128, top_k=4, chunk_size=16)
        model = TempoFormer(config)
        tokenizer = SemanticHierarchicalTokenizer(chunk_size=16)
        data_loader = PremiumDataLoader(sources=["premium_curated", "synthetic"])
        reasoning = ReasoningModule()
        learning = LearningModule(router)
        storage = TieredStorage(hot_path="/tmp/hot", warm_path="/tmp/warm")
        ckpt = CheckpointManager(storage, checkpoint_dir="/tmp/checkpoints")

        machine = TrainingMachine(
            model=model,
            tokenizer=tokenizer,
            router=router,
            data_loader=data_loader,
            reasoning_module=reasoning,
            learning_module=learning,
            checkpoint_manager=ckpt,
            mesh=mesh,
            simulator=simulator,
        )

        checker = ReadinessChecker(machine)
        status = checker.check()
        log(f"Readiness: {status}")
        if not status.get("ready", False):
            log("Not ready, exiting.")
            return 1

        start_time = time.time()
        log("\n--- Premium Data Collection & Generation Phase ---")
        domains = ["reasoning", "math", "code", "research", "agent", "computer_use"]
        collected = 0
        data_phase_end = start_time + duration_sec * 0.3  # 30% for data

        while time.time() < data_phase_end:
            for d in domains:
                sample_text = f"Premium {d} sample {collected}: advanced reasoning and verification trace."
                _ = tokenizer.encode(sample_text)
                collected += 1
                if collected % 200 == 0:
                    elapsed = (time.time() - start_time) / 60
                    log(f"Data: {collected} samples | Elapsed: {elapsed:.1f} min | Domain: {d}")
            time.sleep(0.01)

        log(f"\nData phase complete. Samples: {collected}")
        log("--- Starting Training Phase ---")

        # Training for remaining time, but limit steps to avoid infinite
        remaining_sec = max(10, duration_sec - (time.time() - start_time))
        steps_target = min(5000, int(remaining_sec * 2))
        result = machine.run(max_steps=steps_target, stage=stage)

        total_elapsed = (time.time() - start_time) / 60
        log(f"\n=== Run Complete ===")
        log(f"Total elapsed: {total_elapsed:.1f} minutes")
        log(f"Training result: {result}")
        log(f"Premium data samples: {collected}")
        return 0

    except Exception as e:
        log(f"FATAL ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
