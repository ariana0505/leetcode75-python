---
name: review-solution
description: Review a LeetCode solution for complexity, edge cases, and alternative approaches. Usage: /review-solution <path-to-solution>
disable-model-invocation: true
---

# Skill: Review Solution

Analyze a LeetCode solution and provide actionable feedback.

## Arguments

The user provides (via `$ARGUMENTS` or in their message):
- **path**: path to the solution file (e.g., `01-two-sum/two_sum.py`)

If no path is given, check if the user has a file open in the IDE and use that. Otherwise, ask.

## Flow

1. Read the solution file completely
2. Understand what problem it solves (check `statement.md` in the same directory if available)
3. Analyze the solution and produce the review below
4. Present the review to the user in a clear, structured format

## Review structure

### 1. Complejidad / Complexity
- **Temporal (Time):** O(?) — explain why
- **Espacial (Space):** O(?) — explain why

### 2. Correctitud / Correctness
- Does it handle all constraints from the problem?
- Are there edge cases not covered? (empty input, single element, duplicates, negative numbers, overflow, etc.)

### 3. Optimización / Optimization
- Can the time or space complexity be improved?
- Is there a more efficient algorithm or data structure?
- If the current solution is already optimal, say so.

### 4. Estilo / Style
- Only mention significant issues (not nitpicks)
- Variable naming, readability, Pythonic patterns

### 5. Enfoque alternativo / Alternative approach (optional)
- If there's a notably different approach (e.g., iterative vs recursive, different data structure), briefly describe it with its complexity

## Rules

- Be concise. Each section should be 1-3 sentences unless more detail is needed.
- Use bilingual headers (Spanish / English) as shown above.
- Do NOT rewrite the solution unless the user explicitly asks.
- If the solution is already optimal and clean, say so — don't invent problems.
- Comments in Spanish are fine and expected in this project.
