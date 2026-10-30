# Digital Datacenter Architecture

Software-defined compute cluster equivalent to 8× TPU v5p + 1000× GB300 (Blackwell Ultra).

## Design Principles
- Pure software abstraction over heterogeneous physical hardware
- High Model FLOPS Utilization (MFU > 55% target)
- Fault tolerance and elastic scaling
- Deterministic training where possible
- Separation of compute, storage, and networking layers

## Components
1. **Compute Layer**: Virtual mesh (TPU-style 3D torus + GB300 NVLink domains)
2. **Storage Layer**: Tiered high-performance storage for data, checkpoints, and intermediates
3. **Orchestration**: Workflow engine for job scheduling, elasticity, and monitoring
4. **Networking Abstraction**: Collective primitives over physical interconnects

## Scale Targets
- Peak compute: ~2.7 EFLOPS BF16 equivalent
- Aggregate memory: ~340 TB HBM-equivalent
- Training tokens: 20T+ (premium data only)
- Checkpoint interval: < 2 min (async)

See subdirectories for detailed designs.