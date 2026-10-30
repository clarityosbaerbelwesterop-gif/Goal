# Physical Inspiration Mapped to Digital

| Physical Concept | Digital Equivalent |
|------------------|--------------------|
| Rack / Pod | Virtual mesh domain |
| Liquid cooling | Priority + rate-limited scheduler for hot experts |
| Power delivery | Tempo and expert activation budget |
| NVLink / ICI | In-memory collectives + hierarchical AllToAll |
| HBM | Hot streaming buffers |
| Checkpoint to storage | Async sharded digital checkpoints |
| Failure domain | Isolated virtual chip restart |
| 24/7 uptime | Continuous loop with rolling state |

These mappings keep the operational discipline of real datacenters while remaining pure software.