# Semantic Hierarchical Tokenizer (SHT)

## Goal
A tokenizer that produces far fewer tokens while preserving or improving semantic density, contributing heavily to the 40-50x efficiency target.

## Design
1. **Byte-level base** with learned BPE-style merges
2. **Semantic chunking layer**
   - Groups tokens into meaningful phrases, code blocks, math expressions, or reasoning steps
   - Uses a small auxiliary model or rules + learned scorer
3. **Hierarchical output**
   - Emits both fine tokens and higher-level chunk tokens
   - Model primarily attends at chunk level; fine tokens used only when needed
4. **Domain-aware**
   - Special handling for code, math, and structured agent actions

## Efficiency
- Typical reduction: 8-15x fewer tokens vs. standard BPE on the same text
- Preserves information better than aggressive compression because chunks are semantically coherent
- Enables the hierarchical attention in TempoFormer

## Training
- Jointly trained or pre-trained on premium data
- Can be frozen early and refined with the main model