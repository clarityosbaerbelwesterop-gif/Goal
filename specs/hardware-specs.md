# Target Hardware Specifications for Digital Datacenter

## Objective
Pure software-defined cluster matching the performance of:
- 8x TPU v5p pods (or equivalent Trillium / Ironwood scale)
- + 1000x NVIDIA GB300 (Blackwell Ultra)

## Reference Numbers (as of Oct 2026)

### TPU Side
- TPU v5p: 459 TFLOPS BF16/chip, 96 GB HBM, 64-chip pods ~29.5 PFLOPS
- TPU v6e (Trillium): 918 TFLOPS BF16/chip, 32 GB HBM, 256-chip pods ~235 PFLOPS
- TPU7x (Ironwood): ~2,307 TFLOPS BF16/chip, 192 GiB HBM, 9,216-chip pods

**8x v5p equivalent**: ~235 PFLOPS BF16, ~49 TB HBM

### GB300 Side
- Per GB300: 2,500 TFLOPS BF16, 288 GB HBM3e, 8 TB/s BW, 1.4 kW
- 1000 units: 2.5 EFLOPS BF16, 288 TB HBM

### Combined Target
- **Compute**: ~2.7 EFLOPS BF16 peak (with high MFU target >50%)
- **Memory**: ~340 TB HBM-equivalent (distributed VRAM + host RAM + offload)
- **Interconnect**: Simulated high-bandwidth domains (NVLink-style within nodes, InfiniBand 800G+ scale-out)
- **Topology**: Virtual 3D torus / fat-tree over physical cluster

## Software Abstractions Needed
- Virtual device mesh mapping logical TPU/GPU chips to physical GPUs
- XLA/PJRT-like compiler for sharding
- Collective communication library (NCCL backend + custom)
- ZeRO-style memory management + activation checkpointing
- Fault tolerance and elastic training

See `research/tpu-analysis.md` and `research/gb300-analysis.md` for detailed breakdowns.
