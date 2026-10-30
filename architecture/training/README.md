# Training Methods

Formalized training paradigms for the SOTA MoE model. Combines established techniques with new methods tailored to reasoning, adaptive learning, agents, and long-horizon capabilities.

## Core Methods
1. **Premium Data Pre-training**
   - High-quality curated + synthetic only
   - Curriculum with progressive difficulty

2. **MoE-Specific Training**
   - Expert specialization losses
   - Fluid routing optimization
   - Capacity-aware load balancing

3. **Constitutional + RLAIF Hybrid**
   - Principle-based critique and revision
   - AI-generated preference data

## New / Invented Methods

### 1. Tempo Training
Progressive tempo control of reasoning depth and compute allocation.
- Early training: short reasoning traces
- Later: variable-length System-2 traces controlled by a tempo signal
- Model learns to allocate more thinking tokens to hard problems
- Combines with adaptive compute (early exit / extra loops for hard tokens)

### 2. Adaptive Expert Specialization (AES)
Online clustering of expert usage + reward for specialization.
- Track which experts handle which capability domains
- Soft constraint that pushes related tokens to the same expert groups
- Improves interpretability and efficiency

### 3. Long-Horizon Agentic Consistency (LHAC)
Training signal for multi-day / multi-step agent workflows.
- Synthetic long trajectories (coding sessions, research tasks, computer-use episodes)
- Consistency loss across steps + successful completion reward
- Sub-agent handoff training

### 4. Verifiable Reasoning Distillation (VRD)
- Generate reasoning traces that can be checked (math proofs, code tests, formal claims)
- Distill only traces that pass verification
- Reduces hallucination in reasoning-heavy domains

### 5. Self-Play Premium Data Generation (SPDG)
- Model generates high-quality synthetic data in domains where it is strong
- Filter with verification + constitutional principles
- Feeds back into training (premium data only)

### 6. Meta-Adaptive Learning Loop (MALL)
- Explicit training for in-context adaptation and continual learning
- Episodes where the model must learn a new skill from few examples and retain it
- Forgetting mitigation via replay + elastic weight consolidation style signals

## Training Stages (Proposed Order)
1. Base MoE pre-training on premium data (with Tempo + AES)
2. Reasoning & verifiable distillation (VRD)
3. Constitutional / RLAIF alignment
4. Agentic & long-horizon fine-tuning (LHAC + computer use)
5. Meta-adaptive and continual refinement (MALL)
6. Final preference optimization and safety hardening

## Data Policy
Premium only. No bulk low-quality web data. Heavy filtering, deduplication, and contamination control.