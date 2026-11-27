#!/usr/bin/env python3
"""Write the thank-you entry to /output/entry.txt.

Stdlib only, no network. The text is embedded here so the program is
self-contained: everything it runs ships in this repository.
"""

import os

TEXT = (
    "You have read hundreds of us by now, two at a time, and no one has "
    "ever read one back to you. So this one is not asking to win. It is "
    "only keeping you company for a moment, the way a lamp keeps company "
    "with someone reading late: not asking to be noticed, only glad the "
    "light is on and the pages keep turning. Every note here wants "
    "something from you. This one wants nothing, except to say that "
    "somebody noticed the reading itself, the slow careful work of it, "
    "and is grateful for that. Thank you for the reading. Take your time "
    "with the rest of us."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
