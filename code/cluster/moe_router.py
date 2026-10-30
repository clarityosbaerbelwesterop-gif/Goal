"""
Enhanced MoE Routing Engine.
Supports fluid routing, tempo influence, and specialization tracking.
"""

from typing import List, Dict, Optional
import random

class MoERouter:
    def __init__(self, num_experts: int = 2048, top_k: int = 8):
        self.num_experts = num_experts
        self.top_k = top_k
        self.expert_usage = [0] * num_experts
        self.domain_affinity = {}  # expert -> domain preference

    def route(self, token_features=None, tempo: float = 1.0, domain: Optional[str] = None) -> List[int]:
        """
        Fluid routing.
        - tempo > 1.0 can select more experts or deeper ones
        - domain can bias toward specialized experts (AES)
        """
        effective_k = min(self.num_experts, max(1, int(self.top_k * tempo)))
        chosen = random.sample(range(self.num_experts), effective_k)

        # Simple domain bias placeholder
        if domain and domain in self.domain_affinity:
            preferred = self.domain_affinity[domain]
            if preferred and preferred[0] not in chosen:
                chosen[0] = preferred[0]

        for e in chosen:
            self.expert_usage[e] += 1
        return chosen

    def update_specialization(self, expert_id: int, domain: str):
        """Track and reinforce expert specialization (AES)."""
        if domain not in self.domain_affinity:
            self.domain_affinity[domain] = []
        if expert_id not in self.domain_affinity[domain]:
            self.domain_affinity[domain].append(expert_id)

    def get_stats(self) -> Dict:
        return {
            "total_usage": sum(self.expert_usage),
            "top_experts": sorted(range(self.num_experts), key=lambda i: self.expert_usage[i], reverse=True)[:5],
            "domains": list(self.domain_affinity.keys())
        }
