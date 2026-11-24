"""One Word, One Username, One Reward — make.fun entry.

Writes our own make.fun username, luc-ky, and nothing else to
/output/entry.txt. No pitch, no explanation, no links — the
username is the whole entry, exactly as the bounty asks.

Second revision: tightened the validation so the entry is
checked as a single line as well as for length.
"""

import os

ENTRY = 'luc-ky'

MAX_CHARS = 30


def main() -> None:
    text = ENTRY
    assert text.strip(), "entry must not be only whitespace"
    assert len(text) <= MAX_CHARS, (
        f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
    )
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("ENTRY_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    # Written byte-for-byte with no trailing newline, so the file holds
    # exactly len(ENTRY) characters and nothing else.
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)
    with open(path, "r", encoding="utf-8") as handle:
        assert handle.read() == text, "entry.txt does not match ENTRY"


if __name__ == "__main__":
    main()
