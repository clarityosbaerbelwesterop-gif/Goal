# Execution Model

## Per-Token Path
1. Hierarchical tokenize → chunks
2. Tempo estimate (difficulty)
3. Route to small set of experts (top-k)
4. Execute only active experts at the required depth
5. Early exit if confidence high
6. Update specialization statistics
7. Discard raw token data

## Per-Step Accounting
- Active parameters ≈ (experts_activated / total_experts) × virtual_width
- Effective FLOPs reduced by hierarchical compression × adaptive depth factor
- Thermal load tracked and used for scheduling

## Long-Running Behavior
- Rolling checkpoints every N steps
- Mesh can be resized between checkpoints
- Curriculum and domain mix evolve continuously
- No global stop required