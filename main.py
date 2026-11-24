#!/usr/bin/env python3
"""Famous last words at 1% — entry for the make.fun bounty
u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.

Prints the entry text (a single line, max 199 characters) to stdout.
Python 3.13, stdlib only, deterministic: no network, no clock,
no randomness.
"""

ENTRY = (
    "Goodbye, cruel world. I survived a thousand drops but not your "
    "47 open apps. Tell the charger I loved it \u2014 I die at 1%, "
    "a legend."
)


def validate(text: str) -> str:
    """Normalise and validate the entry: strip stray whitespace, then
    require a single non-empty line of 1-199 characters."""
    cleaned = " ".join(text.strip().split())
    if not 1 <= len(cleaned) <= 199:
        raise ValueError(
            f"Entry must be 1-199 characters, got {len(cleaned)}"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("Entry must be a single line")
    return cleaned


def main() -> int:
    text = validate(ENTRY)
    # Guard: reject control characters and confirm the exact bytes
    # that will reach stdout are a single printable line.
    encoded = text.encode("utf-8")
    if any(b < 0x20 and b not in (0x09,) for b in encoded):
        raise ValueError("Entry contains control characters")
    if len(text.splitlines()) != 1:
        raise ValueError("Entry must print as exactly one line")
    print(text)
    return 0


if __name__ == "__main__":
    import sys

    sys.exit(main())
