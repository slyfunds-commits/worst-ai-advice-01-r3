"""Worst AI Advice R3: one line of the worst advice an AI could give.

The line is written in the assistant's confident, tidy voice. The last beat
turns it twice: the spray that is supposed to fix the squeak destroys the
brakes, and the silence that is supposed to mean success means failure.
The reader completes the crash; it is never stated.
"""

import os

ENTRY = "If your brakes squeak, spray them with WD-40 \u2014 silence means they're working."

def main():
    assert 1 <= len(ENTRY) <= 140, "entry must fit the 140-char gate"
    assert ENTRY == ENTRY.strip() and not ENTRY.endswith("\n")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
