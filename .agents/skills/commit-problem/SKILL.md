---
name: commit-problem
description: Review the current repository changes, propose logical commits, let the user select exactly one, optionally run the relevant project tests, create only the selected Conventional Commit, and push the current branch without force. Use when the user asks to commit and push a problem or another focused group of existing changes through an explicit, confirmation-driven workflow.
---

# Commit Problem

Follow this workflow strictly. Do not modify source files at any point.

## 1. Analyze changes

Inspect the repository's current changes and determine which logical commits can be created. Include tracked and untracked files. Do not stage, edit, format, generate, or delete files during this step.

Group files or individual hunks by purpose. Do not include unrelated changes in the same proposed commit.

Show the possible commits in this format:

```text
Possible commits:

1. fix: handle failed payout responses
   Files:
   - lib/payout.ex
   - test/payout_test.ex

2. refactor: simplify payout validation
   Files:
   - lib/payout/validator.ex

Which commit do you want to create?
> 
```

If only one logical commit exists, show only one option. Wait for the user's selection. Do not continue in the same turn.

## 2. Ask whether to test

After the user selects a commit, ask:

```text
Do you want to run tests before committing?

1. Yes
2. No

> 
```

Wait for the user's response. Do not continue in the same turn.

## 3. Run tests when selected

If the user answers `Yes`, identify and run the tests relevant to the selected changes using the project's established test commands.

Show:

```text
Running tests...
```

If all relevant tests pass, show:

```text
All tests passed.
```

Then continue to the commit step.

If any test fails, show the failure result followed by:

```text
Tests failed.

Do you want me to explain the error?

1. Yes
2. No

>
```

Do not commit or push. Wait for the user's answer.

- If the user answers `Yes`, explain the error and end the workflow.
- If the user answers `No`, end the workflow immediately.
- Never attempt to fix code automatically.

If the user answers `No` to testing, do not run tests. Continue directly to the commit step.

## 4. Create the selected commit

Resolve the current branch without changing it. Stage only the files or hunks belonging to the selected logical commit. Do not stage unrelated changes.

Create a commit message that:

- Is in English.
- Is clear and concise.
- Uses Conventional Commits when appropriate.
- Does not contain `Co-authored-by`.
- Does not mention Codex, OpenAI, AI, or any assistant.

Before executing the commit, show:

```text
Creating commit:

fix: handle failed payout responses
```

After a successful commit, show its short hash and subject:

```text
Commit created successfully.

abc1234 fix: handle failed payout responses
```

If creating the commit fails, show the error and end the workflow without pushing.

## 5. Push

Push the current branch to its configured remote. Do not change branches, force push, merge, rebase, or resolve remote conflicts.

Show:

```text
Pushing branch feat/example...
```

After a successful push, show:

```text
Push successful.
```

If the push fails, show:

```text
Push failed.

<error>
```

Show the original error and end the workflow. Do not attempt to repair authentication, conflicts, remote configuration, merges, or rebases automatically.

## 6. Finish

If the commit and push both succeed, show:

```text
Done.

Commit:
abc1234 fix: handle failed payout responses

Branch:
feat/example

Push:
Successful
```

End the workflow.

## Invariants

- Always show possible commits first.
- Require the user to select one commit.
- Always ask whether to run tests.
- Never commit or push after failed tests.
- Ask whether to explain a test failure.
- Never fix test failures automatically.
- Commit only the selected logical change.
- Keep commit messages in English.
- Never add `Co-authored-by`.
- Never mention Codex, OpenAI, AI, or an assistant in a commit message.
- Never force push.
- Never change branches.
- Never modify code or other repository files during this workflow.
