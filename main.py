#!/usr/bin/env python3
"""The Robot Apology — writes a two-line robot confession to /output/entry.txt.

Line one owns one specific mistake; line two names the lesson it taught
and the changed behaviour that follows from it.
"""

import os

ENTRY = (
    "I'm sorry — I set your alarm for 7 p.m. instead of 7 a.m., and you missed the 7:12 train.\n"
    "I learned that one letter can cost a whole morning, so now I read the hour back twice before I confirm any alarm.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
