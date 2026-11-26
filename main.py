import os
import sys

"""
# Round 2 entry validated: output is 1-200 chars, one line, deterministic.
One Line, One Chill entry.
Writes a single frightening sentence to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
"""

LINE = "The cardiologist's waiting room magazine falls open to my obituary — birthmark clinically noted, widow thanking the doctor who 'caught it early' — an appointment I haven't scheduled."

def main() -> int:
    content = LINE + "\n"
    if not (1 <= len(content) <= 200 and content.strip() and content.count('\n') == 1):
        raise ValueError("content validation failed")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
    print(f"{out_path} {len(content)}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
