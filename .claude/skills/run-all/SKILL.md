---
name: run-all
description: Run all Python solutions in the repo and report which pass and which fail.
disable-model-invocation: true
---

# Skill: Run All Solutions

Execute every Python solution in the repository and report results.

## Flow

1. Find all `.py` solution files in the repo (search in numbered directories matching pattern `[0-9]*-*/`)
2. Run each file with `python3 <file>` with a 10-second timeout per file
3. Track results: file name, exit code, and any error output
4. Present a summary table to the user

## Output format

Show a results table like this:

```
✅ 01-two-sum/two_sum.py
✅ 02-best-time-to-buy/best_time_to_buy.py
❌ 03-contains-duplicate/contains_duplicate.py → RuntimeError: ...
⏱️ 04-product-of-array/product_except_self.py → timeout (10s)
```

Then a summary line:
```
Resultado: X/Y passed (Z failed, W timeout)
```

## Rules

- Use a **10-second timeout** per solution to avoid hanging on infinite loops
- If a file produces output to stdout, that's normal (solutions print their test results) — only report failures (non-zero exit code or timeout)
- Run solutions from the repo root directory
- Do NOT modify any files
- Skip any `__pycache__` directories or non-solution Python files
- If a directory has multiple `.py` files (variants), run all of them
