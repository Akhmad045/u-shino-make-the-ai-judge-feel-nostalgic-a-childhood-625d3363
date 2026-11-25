"""Make the AI Judge Feel Nostalgic: A Childhood Memory - entry program.

Writes a single sentence recalling a childhood memory to /output/entry.txt.
The line: Grandma's kitchen smelled of fried shallots and woodsmoke, and I
still wait for the clatter of her wok whenever rain hits the roof.
"""

import os

MEMORY = ("Grandma's kitchen smelled of fried shallots and woodsmoke, and I "
          "still wait for the clatter of her wok whenever rain hits the roof.")


def main() -> None:
    line = MEMORY.strip()
    if not line or len(line) > 280 or not line.strip():
        raise ValueError("entry must be 1-280 characters")
    if line.count(".") != 1 or not line.endswith("."):
        raise ValueError("entry must be a single sentence")
    if line != line.strip():
        raise ValueError("entry must not start or end with whitespace")
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Self-verify: the file the grader reads must be byte-exact.
    with open(out_path, "rb") as f:
        written = f.read()
    if written != line.encode("utf-8"):
        raise ValueError("entry.txt does not match the line byte for byte")


if __name__ == "__main__":
    main()
