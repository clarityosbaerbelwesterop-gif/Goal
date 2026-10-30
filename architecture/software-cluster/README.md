# Software Cluster Design

## Virtual Topology
- Primary: 3D torus (matching TPU pods) mapped onto physical GPUs
- Secondary: High-bandwidth NVLink domains (72-GPU equivalent) for expert parallelism
- Fallback: Fat-tree / InfiniBand for scale-out

## Compute Abstraction
- `VirtualTPUMesh` / `VirtualGPUMesh` maps logical chips to physical devices
- Supports fractional mapping (multiple virtual chips per physical GPU)
- Expert parallel routing for MoE
- Pipeline, tensor, sequence, and data parallelism

## Communication Primitives
- AllReduce (ring + tree hybrid)
- AllGather / ReduceScatter
- AllToAll (critical for MoE expert routing)
- Overlap compute/comms via CUDA Graphs / JAX XLA
- Collective scheduling with priority for attention and expert layers

## Fault Tolerance
- Async distributed checkpointing
- Elastic training (add/remove workers)
- Speculative execution for stragglers
- Automatic restart from last consistent checkpoint

## Implementation Roadmap
- Phase 1: Virtual mesh + basic collectives (current)
- Phase 2: Multi-node + InfiniBand backend
- Phase 3: Full MoE routing + fault tolerance
- Phase 4: Production training orchestration