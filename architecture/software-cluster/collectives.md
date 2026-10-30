# Collective Communication Design

## Required Primitives
- **AllReduce**: Gradient synchronization (ring + tree hybrid for large scale)
- **AllToAll**: MoE expert routing (highest priority, must be low-latency)
- **AllGather / ReduceScatter**: Parameter and optimizer state sharding (ZeRO-style)
- **Broadcast**: Initial weight distribution and control messages

## Optimization Targets
- Overlap with compute via CUDA Graphs / persistent kernels
- Topology-aware routing (prefer NVLink domains for experts)
- Compression / quantization of gradients where safe
- Priority scheduling: expert AllToAll > attention AllReduce > other

## Fault Handling
- Timeout and retry with speculative backup
- Partial failure isolation
- Consistent state recovery via checkpoint