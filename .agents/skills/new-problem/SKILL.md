---
name: new-problem
description: Scaffold a new LeetCode problem directory with solution template and statement file. Usage: /new-problem <number> <problem-name>
disable-model-invocation: true
---

# Skill: New Problem Scaffold

Create the directory structure and template files for a new LeetCode problem.

## Arguments

The user must provide (via `$ARGUMENTS` or in their message):
- **number**: the problem number in the list (e.g., 39)
- **problem-name**: the problem name in kebab-case (e.g., `merge-intervals`)

If arguments are missing, ask the user for them.

## Flow

1. Parse the number and problem name from arguments
2. Convert the problem name to snake_case for the Python file (e.g., `merge-intervals` → `merge_intervals.py`)
3. Create the directory: `{number}-{problem-name}/`
4. Create the solution file with the template below
5. Create the `statement.md` with the template below
6. Show the created files with `ls -la {directory}/`

## Solution template (`{snake_case_name}.py`)

```python
from typing import List, Optional


class Solution:
    def METHOD_NAME(self, PARAMS) -> RETURN_TYPE:
        pass


if __name__ == "__main__":
    sol = Solution()
    # Ejemplo 1 / Example 1
    # print(sol.METHOD_NAME())
```

**Note:** Leave `METHOD_NAME`, `PARAMS`, and `RETURN_TYPE` as placeholders. The user will fill them in based on the actual problem.

## Statement template (`statement.md`)

```markdown
# {number}. {Problem Name (title case)}

## English

_Paste the problem statement here._

## Español

_Pega el enunciado del problema aquí._
```

## Rules

- **NEVER** overwrite existing directories or files. If the directory already exists, warn the user and stop.
- Use the exact naming conventions: directory in kebab-case, Python file in snake_case.
- All template content must be in English/Spanish as shown above.
