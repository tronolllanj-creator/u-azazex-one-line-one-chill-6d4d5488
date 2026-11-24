"""
# Entry validated: output is 1-200 chars, one line, deterministic.
Entry point that writes a specific suspense line to the output directory.
"""

import os

LINE = "My husband whispered I looked so peaceful asleep, which froze my blood, because I was staring at the ceiling, and his warm breath came from the empty pillow inches from my ear."

def main():
    content = LINE + "\n"
    
    # Validate content
    if not (1 <= len(content) <= 200 and content.strip()):
        raise ValueError("Content validation failed")
    if content.count("\n") != 1 or content.endswith("\n\n"):
        raise ValueError("Must contain exactly one line")
        
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    
    primary_path = os.path.join(out_dir, "entry.txt")
    with open(primary_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    if out_dir != "/output":
        try:
            os.makedirs("/output", exist_ok=True)
            with open("/output/entry.txt", "w", encoding="utf-8") as f:
                f.write(content)
        except Exception:
            pass
            
    print(primary_path)
    print(len(content))

if __name__ == "__main__":
    main()
