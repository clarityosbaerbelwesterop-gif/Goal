# Git-Native Serverless Datacenter

## Principles
- Repository is the single source of truth (GitOps)
- Workflows spin up ephemeral workers for jobs
- State externalized (checkpoints as artifacts, routing tables in repo or object storage)
- No permanent hardware ownership required

## Mapping to Existing System
- Virtual mesh and scheduler already support this model
- Rolling checkpoints uploaded as artifacts
- Multi-job workflows chain state across runs

This aligns with the pure digital approach already built.