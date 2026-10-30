# Program-as-Weights (PAW) & Hybrid Execution

## Idea
Represent skills and knowledge as executable code, symbolic rules, decision graphs, and hyperdimensional vectors where possible, instead of (or in addition to) dense neural weights.

## Practical Hybrid
- Deterministic or verifiable sub-tasks (sorting, parsing, formal math steps, tool calls) → pure code execution
- Open-ended language, reasoning, and adaptation → sparse neural components or external model calls
- Routing layer decides per request which path to take

## Mobile / iPad Constraint
- Full 100B-parameter models cannot run locally on an iPad
- Feasible on-device: small specialized models, code executors, cached symbolic programs, and lightweight routing
- Heavy reasoning can be offloaded to jobs / remote workers while the device handles orchestration and light inference

## Adaptation Loop
- Jobs run tests, Chain-of-Thought evaluations, and synthetic feedback
- Successful code or prompt improvements are committed back
- Neural parts (if any) stay small enough for the target device or are called remotely