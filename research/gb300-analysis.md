# NVIDIA GB300 (Blackwell Ultra) Hardware Analysis

## Overview
The NVIDIA GB300 is the Blackwell Ultra generation GPU, available in NVL72 rack-scale systems. As of October 2026, it is the current flagship for AI training and inference, with next-gen Vera Rubin (Rubin architecture) beginning to ship in limited quantities.

### Per-GPU Specifications (Blackwell Ultra / GB300)
- **Architecture**: Blackwell Ultra (dual reticle dies, ~208B transistors, TSMC 4NP)
- **CUDA Cores**: 20,480
- **Tensor Cores**: 640 (5th Gen)
- **HBM Memory**: 288 GB HBM3e
- **Memory Bandwidth**: 8 TB/s
- **Peak Performance (dense)**:
  - BF16/FP16: 2,500 TFLOPS
  - FP8: 5,000 TFLOPS
  - FP4 (NVFP4): 15,000 TFLOPS
  - FP32: ~80 TFLOPS
- **TDP**: 1,400 W
- **NVLink**: 1.8 TB/s bidirectional per GPU
- **Host Interface**: PCIe Gen 6 x16
- **Form Factor**: SXM / Superchip (Grace + Blackwell Ultra)

### GB300 NVL72 Rack Specifications
- **Configuration**: 72 Blackwell Ultra GPUs + 36 Grace CPUs
- **GPU Memory**: ~20.7 TB HBM3e total
- **GPU Memory Bandwidth**: 576 TB/s aggregate
- **Fast Memory**: Up to 37 TB
- **CPU Memory**: 17 TB LPDDR5X
- **NVLink Domain Bandwidth**: 130 TB/s
- **Peak Performance (rack)**:
  - FP16/BF16 Tensor: 360 PFLOPS
  - FP8/FP6: 720 PFLOPS
  - FP4 (dense): 1,080 PFLOPS
  - FP4 (sparse): 1,440 PFLOPS
- **Power**: Fully liquid-cooled, ~135 kW typical
- **Networking**: ConnectX-8 SuperNIC 800 Gbps per GPU

### Comparison Notes
- ~1.5x dense FP4 vs previous Blackwell
- 2x attention performance improvement
- Designed for test-time scaling, reasoning, and agentic workloads
- Cloud pricing (Oct 2026): ~$13/GPU/hour on-demand

## Implications for Software Cluster
A 1000x GB300 equivalent target provides:
- ~2.5 EFLOPS BF16 peak
- ~288 TB HBM-equivalent
- High-bandwidth NVLink domains + InfiniBand for scale-out

This aligns with the repo goal of matching high-end hardware in a pure software-defined cluster.
