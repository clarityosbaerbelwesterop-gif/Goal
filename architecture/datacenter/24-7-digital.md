# 24/7 Pure Digital Datacenter

## Design Principles
Physics informs the structure (heat, bandwidth, locality, failure domains) but does not limit the abstraction.
The datacenter runs continuously without physical accelerators.

## Core Layers

### 1. Power & Energy Abstraction
- Logical power domains mapped to process groups
- Dynamic allocation: high-tempo reasoning tasks receive more "power budget"
- Idle experts and early-exit paths consume near-zero

### 2. Cooling & Thermal Model
- Virtual thermal zones
- High-activity MoE experts and long-horizon agent traces are placed in "cooled" high-priority schedulers
- Automatic throttling of tempo when simulated thermal load rises
- Inspiration: liquid cooling loops → priority queues and rate limiters

### 3. Networking Fabric
- Virtual mesh with hierarchical bandwidth
  - Intra-node: memory-speed
  - Intra-rack: high-bandwidth collectives
  - Inter-rack: compressed / hierarchical routing
- AllToAll for expert routing is overlapped with computation

### 4. Storage Hierarchy (inspired by real tiers)
- Hot: in-memory streaming buffers (never persisted)
- Warm: local SSD-equivalent for active checkpoints and routing tables
- Cold: object-storage equivalent for long-term checkpoint history
- Data is streamed, not stored at scale

### 5. Compute Abstraction
- Virtual chips organized in the mesh
- Each virtual chip runs a slice of the MoE + hierarchical attention
- Elastic: chips can be added/removed without stopping the 24/7 loop

### 6. Continuous Operation
- Never-stopping training loop
- Rolling checkpoints
- Live expert specialization updates
- Automatic stage progression or continuous mixed curriculum
- Health monitoring and self-healing (restart failed virtual chips)

## Scaling Narrative
Just as 1 GB once cost millions and GPUs were considered the only future until TPUs/NPUs appeared, this design treats "compute" as a software scheduling and sparsity problem rather than a hardware monopoly.

The 10B+ effective parameter capacity and 100B+ data streaming are expressed through the combination of:
- Extreme MoE sparsity
- Hierarchical semantic compression
- Continuous streaming
- Adaptive depth