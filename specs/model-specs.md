# Model Specifications

## Architecture Summary
- Type: Sparse Mixture-of-Experts Transformer
- Total parameters: 8–15T
- Active parameters: 1–2T
- Layers: 250–300
- Experts: 2048+
- Routing: Top-k with fluid/dynamic allocation
- Context: 1M+ tokens (extendable)

## Target Capabilities
Must demonstrate SOTA or near-SOTA performance on:
- Reasoning (complex multi-step, scientific, mathematical)
- Research (source-grounded, long-horizon synthesis)
- Adaptive Thinking & Learning (in-context, meta-learning, continual)
- Working / Computer Use (GUI interaction, multi-day tasks)
- Math (competition-level, formal verification)
- Coding (full-stack, agentic, secure code generation)
- Agents (multi-agent coordination, tool synthesis, sub-agents)

## Training Data
- Premium only: curated high-quality, synthetic self-play, verified sources
- No low-quality web scrape bulk
- Strong deduplication and contamination controls
- Curriculum designed for progressive capability building

## Evaluation
- Comprehensive benchmark suite covering all target capabilities
- Live agentic evaluations (coding environments, computer use)
- Safety and alignment evaluations