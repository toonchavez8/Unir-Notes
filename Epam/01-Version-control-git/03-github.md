
# GitHub: Create & Clone Repository — Cheat‑Sheet

## 1. Create Repo on GitHub

1. Click **New repository** (green button or “+ → New repository”).
    
2. Name it (e.g. `git-demo`).
    
3. (Optional) Check **Initialize with [[README]]** → **Create**.
    

## 2. Clone to Local Machine

```bash
# in Git Bash, navigate to desired folder:
cd /c/data/temp  

# clone via SSH (or use HTTPS URL):
git clone git@github.com:YourUser/git-demo.git  
# confirm “yes” and enter SSH key passphrase
```

- Creates `git-demo/` directory
    
- `git status` shows you’re on branch `master`
    

## 3. Verify Remote

```bash
git remote -v
# origin  git@github.com:YourUser/git-demo.git (fetch)
# origin  git@github.com:YourUser/git-demo.git (push)
```

## 4. Make & Commit Changes

```bash
# create or edit file:
echo "First two lines of song..." > song.txt  

# check status:
git status  

# stage:
git add song.txt  

# commit with message:
git commit -m "Add first two lines of song"
```

## 5. View History

```bash
git log --oneline
```

## 6. Push to GitHub

```bash
git push origin master
# enter SSH passphrase if prompted
```

Keep this next to your terminal for quick reference when creating and syncing GitHub repos!

# Pulling Changes from Remote

## Scenario

Someone else edited via GitHub UI; you need to update your local.

## Commands

```bash
# show remote commits not yet local: 
git fetch 
# merge fetched into current branch: 
git merge    
# or combined: 
git pull   
# enter SSH passphrase if prompted
```

- **Fast‑forward** merge if no local commits diverge
    
- After pull, `git log` shows new commits and local files update
---
## Microtest

- **What command can be used to "pull" the changes from the remote repository to the local one?**
	- Git pull
- **What combination of commands in git bash will be the right one to add a new file to index, commit and submit to github?**
	- git add, git commit, git push