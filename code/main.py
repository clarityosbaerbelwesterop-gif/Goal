"""
Entry point for the pure software training machine.
Assembles all components and waits for explicit start.
"""

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

def build_system():
    mesh = VirtualTPUMesh(4, 4, 4)  # smaller for pure software
    router = MoERouter(num_experts=128, top_k=4)
    simulator = SoftwareSimulator(mesh)
    config = TempoFormerConfig(num_layers=16, num_experts=128, top_k=4, chunk_size=16)
    model = TempoFormer(config)
    tokenizer = SemanticHierarchicalTokenizer(chunk_size=16)
    data_loader = PremiumDataLoader(sources=["premium"])
    reasoning = ReasoningModule()
    learning = LearningModule(router)
    storage = TieredStorage()
    ckpt = CheckpointManager(storage)

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
    return machine

def check_and_report():
    machine = build_system()
    checker = ReadinessChecker(machine)
    status = checker.check()
    print("=== READINESS CHECK ===")
    print(status)
    return machine, status

if __name__ == "__main__":
    machine, status = check_and_report()
    if status["ready"]:
        print("\nSystem is fully assembled and ready.")
        print("Waiting for explicit GO to start pure-software training.")
    else:
        print("System not ready.")
