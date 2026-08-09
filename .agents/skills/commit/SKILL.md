---
name: commit
description: Create clean commits following Conventional Commits. Use when the user asks to commit, save progress, or push changes.
disable-model-invocation: true
---

# Skill: Clean Commit

Create a commit following these strict rules:

## IMPORTANT
- **NEVER** add co-authors (Co-Authored-By) to the commit message.
- **NEVER** use `git add .` or `git add -A`. Add specific files only.
- **NEVER** push unless the user explicitly asks.
- **ALL** commit messages MUST be written in **English**, regardless of the language the user communicates in.

## Message format (Conventional Commits)

```
<type>(<scope>): <short description>

<optional body>
```

### Allowed types
- `feat`: new solution or feature
- `fix`: bug fix or correction in a solution
- `refactor`: code improvement without behavior change
- `docs`: documentation changes (statement.md, README, etc.)
- `chore`: maintenance tasks (gitignore, structure, etc.)
- `style`: formatting, spaces, imports with no logic change

### Message rules
- Short description must be in **imperative mood** and **lowercase** (no period at the end)
- Max 72 characters on the first line
- Scope is the problem number/name if applicable (e.g., `feat(two-sum): ...`)
- Body is optional, only when the change needs extra explanation

## Flow

1. Run `git status` and `git diff` to understand the changes
2. If the user passed a message as argument (`$ARGUMENTS`), use it as the base for the commit
3. Otherwise, analyze the changes and draft an appropriate message
4. Show the user the proposed message and the files to be included
5. Run `git add` for each relevant file (one by one, never with `-A`)
6. Create the commit using HEREDOC
7. Show the result with `git log --oneline -1`

## Example

```bash
git add 01-two-sum/two_sum.py
git add 01-two-sum/statement.md
git commit -m "$(cat <<'EOF'
feat(two-sum): add hash map solution

O(n) complexity using dictionary for constant time lookup
EOF
)"
git log --oneline -1
```
