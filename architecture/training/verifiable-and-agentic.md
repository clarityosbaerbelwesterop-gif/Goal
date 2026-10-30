# Verifiable Reasoning & Agentic Training

## VRD (Verifiable Reasoning Distillation)
- Only traces that pass an external or self-check are used for distillation
- Math: symbolic or numeric verification
- Code: unit-test execution
- Research claims: citation or consistency check

## LHAC (Long-Horizon Agentic Consistency)
- Synthetic multi-step trajectories (coding sessions, research tasks, computer-use episodes)
- Consistency loss across steps
- Successful completion reward
- Sub-agent handoff training

## Integration
Both signals are applied inside the continuous or stage-based machines without requiring persistent raw data storage.