# Mobile & iPad Constraints

## Reality
- iPad-class devices have limited RAM (typically 8 GB) and no high-end GPU for large models
- Even 7B–13B models are challenging; 100B is impossible locally

## What Can Run Locally
- Program-as-Weights executors
- Tiny neural routers or classifiers
- Cached reasoning templates and tool definitions
- Lightweight Chain-of-Thought orchestration

## What Requires Jobs / Remote
- Large model inference or adaptation
- Massive synthetic data generation
- Heavy evaluation sweeps
- Checkpoint updates for bigger components

The architecture keeps the control plane and light execution on-device while scaling the heavy parts through workflows.