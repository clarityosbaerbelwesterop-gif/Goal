"""
Collective communication primitives for the software cluster.
Backend-agnostic interface (NCCL, custom, or simulated).
"""

from typing import List

class CollectiveOps:
    def __init__(self, mesh):
        self.mesh = mesh

    def all_reduce(self, tensor, op: str = "sum"):
        """AllReduce across virtual mesh."""
        # Placeholder: in production call NCCL or custom ring/tree
        return tensor

    def all_to_all(self, tensor, routing_map):
        """AllToAll for MoE expert routing. Critical path."""
        # Placeholder for expert parallel communication
        return tensor

    def all_gather(self, tensor):
        return tensor

    def reduce_scatter(self, tensor):
        return tensor
