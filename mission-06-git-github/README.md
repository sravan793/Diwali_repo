# Mission 6 — Git and GitHub

## 1. Task / objective
Practise checking Git status, staging selected files, committing changes, viewing history, creating a branch and opening a Pull Request.

## 2. Work completed
Follow this workflow from the repository root, completing it only after the earlier mission work is genuinely ready:

```bash
git status
git add README.md
git commit -m "Update project overview"
git log --oneline
git switch -c update-about
```

Edit the root README and add a short section titled `My Learning`, then:

```bash
git add README.md
git commit -m "Add My Learning section"
git push -u origin update-about
```

On GitHub, open a Pull Request from `update-about` into `main`. Record its URL and status below. Merge only if your instructor asks you to. If it is merged, update local `main` as appropriate.

### Git glossary
- **Repository:** project folder tracked by Git.
- **Working tree:** current files being edited.
- **Staging area:** selected changes prepared for a commit.
- **Commit:** saved snapshot of staged changes.
- **Branch:** separate line of development.
- **Remote:** hosted repository such as GitHub.
- **Push:** send local commits to a remote.
- **Pull Request:** request to review and merge proposed changes.

## 3. Commands / tools used
Record commands actually run: `[FILL IN]`.

## 4. My understanding
Git tracks changes in a project. A commit records a snapshot, a branch lets me work separately, and a Pull Request provides a place to review proposed changes before merging.

## 5. Difficulties faced
[FILL IN actual difficulties.]

## 6. How I resolved them
[FILL IN actual steps.]

## 7. Evidence / files
- GitHub repository URL: `[FILL IN]`
- Pull Request URL and status: `[FILL IN]`
- `git log --oneline` evidence: `[FILL IN; redact personal email if shown]`

## 8. Commit details
List the actual mission-specific commit hash and push status: `[FILL IN]`.
