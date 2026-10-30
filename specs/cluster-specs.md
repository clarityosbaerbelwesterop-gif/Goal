# Cluster Specifications

## Target Equivalence
- Compute: 8× TPU v5p pods + 1000× GB300 equivalent
- Peak BF16: ~2.7 EFLOPS
- Memory: ~340 TB HBM-equivalent (distributed)
- Interconnect: Virtual high-bandwidth domains + scale-out fabric

## Virtual Mesh
- Default topology: 8×8×8 = 512 virtual chips (adjustable)
- Mapping: Fractional or one-to-one onto available physical GPUs
- Parallelism support: Data, Tensor, Pipeline, Expert, Sequence

## Performance Targets
| Metric | Target |
|--------|--------|
| MFU | > 55% |
| Communication overhead | < 15% of step time |
| Checkpoint time | < 2 min (async) |
| Scale efficiency | > 90% weak scaling |
| MTBF | > 24 hours |

## Software Requirements
- Python 3.10+
- PyTorch / JAX with custom collectives
- NCCL / RCCL backend
- Distributed checkpointing library
- Monitoring (metrics, dashboard)