# Recovery & Continuity

## Rolling Checkpoints
- Written asynchronously
- Contain full virtual state (routing tables, tempo, specialization stats, effective scale)
- Versioned and immutable once written

## Self-Healing
- Virtual chip failure → reload last consistent checkpoint
- Mesh reshape on the fly
- No single point of failure in the digital design

## 72h+ Operation
The system is structured so multiple sequential jobs can chain via artifact checkpoints, maintaining continuity across the full duration.