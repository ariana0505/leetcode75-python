# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A collection of LeetCode 75 problem solutions in Python. The repo is bilingual (English/Spanish), with comments and problem statements often in Spanish.

## Repository Structure

Each problem lives in its own numbered directory: `{number}-{problem-name}/`

Each directory contains:
- A Python solution file (snake_case naming, e.g., `two_sum.py`)
- A `statement.md` with the problem description in both English and Spanish

Some problems have variant subdirectories (e.g., `01-two-sum/two-sum2/`, `21-house-robber-and-2/22-house-robber2.py/`).

## Running Solutions

Solutions are standalone Python scripts. Run any solution directly:

```bash
python3 {directory}/{solution}.py
```

Solutions use either a `class Solution` pattern with a `__main__` block, or run as plain scripts with inline test cases.

## Conventions

- Language: Python 3 with `typing` imports (e.g., `List`, `Optional`)
- Comments are typically in Spanish
- Problem numbering follows a custom order (not LeetCode problem IDs), corresponding to a curated 75-problem list
- No test framework is used; solutions include inline examples run via `__main__`

## Behavior

- Always use available skills (e.g., `/commit`, `/simplify`) instead of performing the equivalent steps manually. If a skill matches the task, invoke it via the Skill tool first.
