# Mixture-of-Agents & Swarm Intelligence

## Structure
- Hierarchical swarms: meta-orchestrator decomposes tasks and delegates to specialized agents
- Agents live as code + prompts in the repository
- Asynchronous updates via GitHub workflows or artifact exchange
- Synthetic feedback loops: evaluation workflows test variations and merge improvements

## Relation to MoE
Agents can be seen as very large, interpretable "experts" that are invoked sparsely.

## Current Implementation Status
Design and orchestration hooks are defined. Full autonomous swarm training still requires either real model backends or continued simulation.