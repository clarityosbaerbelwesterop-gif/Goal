# MoE Routing & Expert Parallelism

## Routing Design
- **Fluid / Dynamic Routing**: Continuous allocation based on token complexity (not just static top-k)
- **Top-k with Load Balancing**: Top-8 to top-16, auxiliary loss for balance
- **Expert Specialization**: Encourage experts to specialize (math, code, reasoning, agents, computer-use)
- **Hierarchy**: Shared experts + specialized experts

## Communication
- AllToAll is the critical path for expert parallel
- Prefer placement of experts within high-bandwidth domains (NVLink-style)
- Overlap AllToAll with compute of previous/next layers

## Training Considerations
- Auxiliary losses: load balance + z-loss + specialization bonus
- Expert dropout / capacity factor for robustness
- Routing statistics logged for analysis and adaptive training

## Integration with Virtual Mesh
- Experts mapped to virtual chips with locality preference
- Routing table can be remapped on elastic changes