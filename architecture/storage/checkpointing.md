# Async Distributed Checkpointing

## Design Goals
- Non-blocking (< 2 min target)
- Consistent across virtual mesh
- Elastic recovery (restart on different number of workers)
- Sharded format to avoid single-node bottlenecks

## Strategy
1. **Snapshot Trigger**: Every N steps or on signal
2. **Sharding**: Each virtual chip / rank writes its own shard (parameters, optimizer, RNG)
3. **Placement**: Warm tier first (NVMe), then async copy to cold tier
4. **Consistency**: Barrier only for metadata; data write is async
5. **Recovery**: Load latest consistent checkpoint, remap to current mesh shape

## Implementation Notes
- Use memory-mapped or zero-copy where possible
- Overlap with next training step via separate I/O thread/process
- Versioned checkpoints with metadata (step, mesh shape, expert routing stats)
- Support partial reload for elastic scaling