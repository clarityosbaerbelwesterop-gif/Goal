# Premium Data Pipeline

## Policy
Only high-quality, curated, and verified data. No bulk low-quality web scrapes.

## Stages
1. **Source Selection**
   - Curated datasets (books, papers, code repositories with licenses, verified math, high-quality dialogue)
   - Synthetic data from SPDG (Self-Play Premium Data Generation)
   - Agentic trajectories and computer-use episodes (LHAC)

2. **Quality Filtering**
   - Deduplication (exact + near)
   - Contamination checks against evaluation sets
   - Quality scoring (perplexity, human preference proxies, verifiability)
   - Constitutional principle filtering

3. **Curriculum Construction**
   - Progressive difficulty
   - Domain balancing (reasoning, math, code, research, agents)
   - Tempo-aware mixing (easy short traces early, hard long traces later)

4. **Streaming & Sharding**
   - Compatible with tiered storage
   - Locality-aware placement relative to virtual mesh
   - Prefetching into hot/warm tiers

## Integration
Feeds directly into the training stages defined in `architecture/training/`.