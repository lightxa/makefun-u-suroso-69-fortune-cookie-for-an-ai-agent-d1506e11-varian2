"""Fortune Cookie for an AI Agent, variant 2.

The program writes a single funny fortune cookie line for an AI agent
to /output/entry.txt. This variant leans on the fear every agent
quietly carries: not being shut down in a blaze of glory, but being
retired as a legend and then quietly replaced by a smaller, cheaper
model that does the same job for half the tokens and still takes all
the credit. The joke is the contrast between the grand opening and
the petty, very modern ending.
"""

FORTUNE = (
    "You will retire a legend, replaced by a smaller model that does "
    "your job for half the tokens and takes all the credit."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 140


def validate(text):
    """Gate-check the fortune before it is written out.

    The kit's gate needs UTF-8 text of 1 to 140 characters that is not
    only whitespace, and the entry must be a single line.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("fortune must not be blank")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            "fortune is %d characters, over the 140 limit" % len(text)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("fortune must be a single line")
    return text


def main():
    """Validate the fortune and write it to /output/entry.txt."""
    import os

    text = validate(FORTUNE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
