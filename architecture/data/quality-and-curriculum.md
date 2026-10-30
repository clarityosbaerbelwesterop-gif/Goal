# Premium Data Quality & Curriculum

## Quality Gates (must pass before streaming)
- Deduplication (exact + MinHash)
- Contamination filter against known eval sets
- Verifiability score (math proofs, code tests, formal claims)
- Constitutional principle check
- Domain balance targets

## Curriculum Stages
1. Foundation (short, high-confidence traces)
2. Reasoning depth increase (Tempo ramp)
3. Verifiable long traces (VRD)
4. Multi-step agent trajectories (LHAC)
5. Meta-adaptive episodes (MALL)
6. Mixed high-difficulty continuous stream

## Streaming Rules
- Generated or ingested on the fly
- Immediately tokenized hierarchically
- Fed to hot buffers — never written to cold storage at scale
- Rejected samples are dropped instantly