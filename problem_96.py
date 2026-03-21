"""Utilities for processing Project Euler problem 96 boards."""

def gather_boards(txt):
    """Read a text file and return all boards."""
    with open(txt, "r", encoding="utf-8") as f:
        text = f.readlines()

    print(text)
    