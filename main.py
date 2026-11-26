"""Best Meal You Ever Had — make.fun entry.

Writes one sentence (at most 200 characters) about the best meal ever had
to /output/entry.txt. Deterministic: no network, no clock, no randomness.
"""

import os

SENTENCE = (
    "At my grandmother's kitchen table in Jakarta, rain drumming on the "
    "tin roof, I tore into rendang so dark and slow-cooked it fell apart "
    "before the spoon reached my mouth."
)

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def main() -> int:
    text = SENTENCE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(text)}")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    # Clean only the contents of the output folder, never the folder itself.
    for name in os.listdir(OUTPUT_DIR):
        path = os.path.join(OUTPUT_DIR, name)
        if os.path.isfile(path) and path != OUTPUT_PATH:
            os.remove(path)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Verify the write round-trips byte-identical: what the judge reads is
    # exactly the sentence above, with no trailing newline or re-encoding.
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != text:
        raise SystemExit("entry.txt does not match the sentence")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
