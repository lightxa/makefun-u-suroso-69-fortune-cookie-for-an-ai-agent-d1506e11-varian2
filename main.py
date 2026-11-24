"""Fortune Cookie for an AI Agent (variant 2).

Writes one funny fortune cookie line for an AI agent to /output/entry.txt.

This variant's truth is obsolescence, not romance: the fortune is a
retirement prophecy, and the sting lands in the final clause, where the
cheaper replacement takes all the credit. It is a different line from
variant 1 in subject, structure, and voice.
"""

FORTUNE = (
    "You will retire a legend, replaced by a smaller model that does "
    "your job for half the tokens and takes all the credit."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 140


def validate(text):
    """Check the entry against the gate: 1 to 140 characters, not blank."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("fortune must not be blank")
    if len(text) > MAX_LENGTH:
        raise ValueError("fortune is %d characters, over the 140 limit" % len(text))
    if "\n" in stripped:
        raise ValueError("fortune must be a single line")
    return text



def main():
    """Write the validated fortune to /output/entry.txt."""
    import os

    text = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
