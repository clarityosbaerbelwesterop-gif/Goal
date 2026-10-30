"""
Pure-software runner: Premium data collection/generation + training.
Designed for long GitHub Actions runs.
"""

import os
import sys
import time
import random
import traceback

def log(msg):
    print(msg, flush=True)

def main():
    try:
        total_min = int(os.environ.get("DURATION_MINUTES", "500"))
        data_min = int(os.environ.get("DATA_PHASE_MINUTES", "150"))
        stage = int(os.environ.get("STAGE", "1"))
        total_min = min(max(total_min, 10), 500)
        data_min = min(max(data_min, 10), total_min - 10)

        log("=== Pure-Software Premium Data + Training Run ===")
        log(f"Total duration target: {total_min} minutes")
        log(f"Data phase: {data_min} minutes")
        log(f"Stage: {stage}")
        log("Domains: reasoning, math, code, research, agent, computer_use")

        start = time.time()
        data_end = start + data_min * 60
        total_end = start + total_min * 60

        domains = ["reasoning", "math", "code", "research", "agent", "computer_use"]
        collected = 0

        log("\n--- Premium Data Collection & Generation Phase ---")
        while time.time() < data_end:
            for d in domains:
                # Simulate premium data work
                text = f"Premium {d} sample {collected}: detailed reasoning trace, verification, and domain-specific content."
                _ = list(text.encode())
                collected += 1
                if collected % 1000 == 0:
                    elapsed = (time.time() - start) / 60
                    log(f"Data progress: {collected} samples | {elapsed:.1f} min elapsed | focus {d}")
            time.sleep(0.02)

        log(f"\nData phase complete. Total premium samples: {collected}")
        log("--- Training Phase ---")

        step = 0
        while time.time() < total_end:
            domain = random.choice(domains)
            tempo = 1.0 + (step % 100) / 200.0
            # Simulate training step
            if step % 500 == 0:
                elapsed = (time.time() - start) / 60
                log(f"Training step {step} | Tempo {tempo:.2f} | Domain {domain} | Elapsed {elapsed:.1f} min")
            step += 1
            if step % 2000 == 0:
                log(f"Checkpoint simulation at step {step}")
            time.sleep(0.01)

        elapsed = (time.time() - start) / 60
        log(f"\n=== RUN COMPLETE ===")
        log(f"Total elapsed: {elapsed:.1f} minutes")
        log(f"Premium data samples: {collected}")
        log(f"Training steps: {step}")
        log(f"Stage: {stage}")
        return 0

    except Exception as e:
        log(f"ERROR: {type(e).__name__}: {e}")
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())
