# Infrastructure

## Components That Enable Continuous Operation

### Virtual Mesh
- Logical 3D topology
- Maps to software processes or threads
- Supports live remapping

### Collectives (Software)
- AllReduce, AllToAll implemented in-memory or via efficient simulation
- Overlapped with local expert computation

### Storage Tiers (Digital)
- Hot: streaming ring buffers
- Warm: active routing tables + recent checkpoints
- Cold: historical checkpoint archive

### Scheduler
- Tempo- and thermal-aware
- Prioritizes high-value domains (reasoning, math, code, agents)
- Enforces power/cooling budgets via rate limits

### Monitoring & Self-Healing
- Continuous health of virtual chips
- Automatic restart and state recovery from last rolling checkpoint

This infrastructure is what allows long-duration pure digital training and data streaming.