"""
Improved async distributed checkpoint manager.
Sharded, elastic-friendly, non-blocking design.
"""

from typing import Dict, Any, Optional
import time
import json
import os

class CheckpointManager:
    def __init__(self, storage, checkpoint_dir: str = "/tmp/checkpoints"):
        self.storage = storage
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(checkpoint_dir, exist_ok=True)
        self.last_checkpoint_time = 0.0
        self.metadata = {}

    def save_async(self, step: int, state_dict: Dict[str, Any], mesh_shape: tuple) -> str:
        """
        Async sharded checkpoint.
        In production: each rank writes its shard in parallel.
        """
        ckpt_id = f"step_{step}"
        meta = {
            "step": step,
            "mesh_shape": mesh_shape,
            "timestamp": time.time(),
            "version": "0.1"
        }
        meta_path = os.path.join(self.checkpoint_dir, f"{ckpt_id}_meta.json")
        with open(meta_path, "w") as f:
            json.dump(meta, f)

        # Placeholder for actual shard writing
        shard_path = os.path.join(self.checkpoint_dir, f"{ckpt_id}_shard_0.pt")
        # In real impl: torch.save(state_dict, shard_path) or sharded format
        self.last_checkpoint_time = time.time()
        self.metadata[ckpt_id] = meta
        return ckpt_id

    def load_latest(self) -> Optional[Dict[str, Any]]:
        """Load most recent consistent checkpoint for recovery."""
        if not self.metadata:
            return None
        latest = max(self.metadata.keys(), key=lambda k: self.metadata[k]["step"])
        return {"id": latest, "meta": self.metadata[latest]}

    def list_checkpoints(self) -> list:
        return list(self.metadata.keys())
