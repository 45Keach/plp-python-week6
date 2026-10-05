# Week 6 Assignment

This repository contains the Week 6 Python error-handling assignment.

- `safe_tools.py` — defines safe functions for division, converting text to integers, and dictionary field lookup using specific exceptions.
- `unbreakable.py` — demonstrates handling invalid numeric input with `try` / `except`.

### Why can't the if check catch "abc" on its own?

An `if` check can test a condition, but converting `"abc"` with `int()` raises a `ValueError` before a normal value check can help. Using `try` / `except ValueError` catches that conversion error and lets the program continue instead of crashing.
