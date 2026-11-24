"""QuietDread Review — one-line code review comment with quiet existential dread.

The program writes a single approved-PR comment of at most 140 characters
to /output/entry.txt. The comment approves the pull request while carrying
quiet dread: the reviewer knows that in six months the code will be legacy
and they themselves will be a stranger to it.
"""

import os

ENTRY = "Approved. In six months this becomes legacy, and I become whoever reviews it then."

MAX_CHARS = 140


def validate_entry(text: str) -> None:
    """Enforce the competition gate before anything is written."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    approvals = ("approved", "lgtm", "ship it")
    if not any(word in text.lower() for word in approvals):
        raise ValueError("entry must explicitly approve the pull request")


def main() -> None:
    validate_entry(ENTRY)
    output_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="") as handle:
        # No trailing newline: the gate counts every character in the file.
        handle.write(ENTRY)
    print(f"wrote {len(ENTRY)} chars to {output_path}")


if __name__ == "__main__":
    main()
