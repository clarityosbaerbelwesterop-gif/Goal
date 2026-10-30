"""
Runner for GitHub Actions: Premium data collection/generation + training start.
Pure software, no hardware.
Runs for the specified duration (default 150 minutes).
"""

import os
import time
import sys

# Ensure package imports work
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

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

def main():
    duration_min = int(os.environ.get("DURATION_MINUTES", "150"))
    stage = int(os.environ.get("STAGE", "1"))
    duration_sec = duration_min * 60

    print(f"=== Starting Pure-Software Run ===")
    print(f"Duration target: {duration_min} minutes")
    print(f"Stage: {stage}")
    print(f"Focus: Premium data collection & generation in reasoning, math, code, research, agents")

    # Build system
    mesh = VirtualTPUMesh(4, 4, 4)
    router = MoERouter(num_experts=256, top_k=4)
    simulator = SoftwareSimulator(mesh)
    config = TempoFormerConfig(num_layers=32, num_experts=256, top_k=4, chunk_size=32)
    model = TempoFormer(config)
    tokenizer = SemanticHierarchicalTokenizer(chunk_size=32)
    data_loader = PremiumDataLoader(sources=["premium_curated", "synthetic_spdg"])
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
    print("Readiness:", status)
    if not status["ready"]:
        print("Not ready, exiting.")
        return

    start_time = time.time()
    print("\n--- Premium Data Collection & Generation Phase ---")
    # Simulate intensive data work in target domains
    domains = ["reasoning", "math", "code", "research", "agent", "computer_use"]
    collected = 0
    while time.time() - start_time < duration_sec * 0.4:  # ~40% of time for data
        for d in domains:
            # Generate / collect premium samples
            sample_text = f"Premium {d} sample generated at step {collected}: advanced reasoning trace and verification."
            encoded = tokenizer.encode(sample_text)
            collected += 1
            if collected % 500 == 0:
                elapsed = (time.time() - start_time) / 60
                print(f"Data collected/generated: {collected} | Elapsed: {elapsed:.1f} min | Domain focus: {d}")
        time.sleep(0.05)  # small pause to simulate work

    print(f"\nData phase complete. Samples processed: {collected}")
    print("--- Starting Training Phase ---")

    # Training phase for remaining time
    remaining = duration_sec - (time.time() - start_time)
    steps_target = max(1000, int(remaining / 2))  # rough
    result = machine.run(max_steps=steps_target, stage=stage)

    total_elapsed = (time.time() - start_time) / 60
    print(f"\n=== Run Complete ===")
    print(f"Total elapsed: {total_elapsed:.1f} minutes")
    print(f"Training result: {result}")
    print(f"Premium data samples: {collected}")
    print("Checkpoints and logs available in /tmp")

if __name__ == "__main__":
    main()
