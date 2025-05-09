

# Git Installation & Configuration — Cheat‑Sheet

## Download & Install (Windows)

- Go to git-scm.com → Download Windows release → Next→Next→…→Finish
    
- Launch **Git Bash** (black shell window)
    

## Generate SSH Key

```bash
ssh-keygen -t rsa -C "you@example.com"
# accept default path (~/.ssh/id_rsa)
# enter simple passphrase or leave blank
```

- Public key: `~/.ssh/id_rsa.pub`
    
- Private key: `~/.ssh/id_rsa` (never share!)
    

> [!caution]
> It cannot be transferred - otherwise the recipient will be able to sign commits on your behalf and send it to your repositories

## Add SSH Key to GitHub

1. GitHub Settings → **SSH and GPG keys**
    
2. “New SSH key” → paste contents of `id_rsa.pub` → Save
    

## Configure Git Username & Email

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

- Omit `--global` to set per‑repo
    

## Verify Configuration

```bash
git config user.name
git config user.email
```

## Key Commands Summary

|Task|Command|
|---|---|
|Clone repo|`git clone <url>`|
|Create & switch branch|`git checkout -b <branch>`|
|Stage changes|`git add <file>` or `git add .`|
|Commit|`git commit -m "message"`|
|Amend last commit|`git commit --amend`|
|View status|`git status`|
|View history|`git log --oneline --graph`|
|Push branch|`git push origin <branch>`|
|Merge via PR (GitHub)|— open Pull Request in web UI —|
|Revert a commit|`git revert <commit-hash>`|
|Hard reset to commit|`git reset --hard <commit-hash>`|

----
## Microtest

- **Where are a pair of ssh keys put to when generating on Windows via ssh-keygen?**
	- C:/Users/User_Name/. Ssh
- **Is it possible to use ssh-keygen to create an ssh key without a password?**
	- Yes, just by pressing Enter instead of entering a password
- **Which of the two ssh keys cannot be transferred to anyone?**
	- Private (file id_rsa)
- **Which command do you need to use to specify your user.name and user.email in git?**
	- git config