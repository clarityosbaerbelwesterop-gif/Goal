# Effective Storage Architecture

High-performance tiered storage for premium training data, checkpoints, and intermediates.

## Tiers
1. **Hot Tier (HBM / GPU VRAM + high-speed NVMe)**
   - Active model parameters, activations, optimizer states
   - Streaming token batches for current step
   - Target: sub-millisecond access for critical path

2. **Warm Tier (Host RAM + NVMe SSD arrays)**
   - Prefetched data shards
   - Recent checkpoints
   - Intermediate activations for recompute
   - ZeRO-style offloading target

3. **Cold Tier (Distributed object store / S3-compatible or custom)**
   - Full training corpus (premium data only)
   - Historical checkpoints
   - Evaluation datasets and traces
   - Long-term archival

## Data Pipeline Requirements
- Streaming dataset loader with prefetching and sharding
- Token-level quality filtering (premium data only)
- Deduplication and contamination checks
- Support for 20T+ tokens with efficient random access for curriculum
- Checkpoint format: sharded, async, consistent across virtual mesh

## Key Metrics
- Data loading should not be the bottleneck (overlap with compute)
- Checkpoint time < 2 minutes (non-blocking)
- Support for elastic recovery without full reload

## Implementation Notes
- Use memory-mapped files + distributed caching where possible
- Integrate with virtual mesh for locality-aware placement
- Future: custom storage engine optimized for sequential token streams + random expert routing