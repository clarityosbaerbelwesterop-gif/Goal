# Tempo Training

## Concept
Control the "tempo" (depth and length) of reasoning dynamically during training.

## Mechanism
- Introduce a tempo signal (scalar or learned) that influences number of reasoning tokens / internal loops
- Early epochs: force short tempo (fast, shallow)
- Later epochs: allow variable tempo, reward correct answers that used appropriate depth
- Auxiliary loss: penalize unnecessary long reasoning on easy problems, reward sufficient depth on hard ones

## Benefits for Target Capabilities
- Better adaptive thinking
- More efficient inference (model learns when to think hard)
- Stronger performance on reasoning, math, and research tasks

## Integration
Works naturally with the fluid MoE routing and System-2 scratchpad design.