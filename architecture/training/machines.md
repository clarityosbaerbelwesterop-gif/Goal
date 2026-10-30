# Training Machines

## 1. Continuous 24/7 Machine
- Entry: `code/datacenter/continuous_loop.py`
- Runs indefinitely
- Streaming data + rolling checkpoints
- Best for long-horizon accumulation

## 2. Digital Scale Machine
- Entry: `code/digital_scale_runner.py`
- Targets high data-point counts
- Produces 10B-representation checkpoints
- Optimized for volume

## 3. Stage Orchestrator
- Entry: `code/training/training_machine.py`
- Explicit stages (base, VRD, LHAC, MALL, etc.)
- Integrates Reasoning and Learning modules

## 4. Full Integrated Machine
Combines scheduler, virtual mesh, streaming, TempoFormer logic, and checkpointing into one long-running process.

All machines are pure software and designed for extended operation.