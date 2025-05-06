

# In‑Depth Class Notes: Git GUI & Gitk

---

## 1. Why Use a Graphical Interface?

- **Limitations of Bash**
    
    - No multi‑pane view or bookmarks
        
    - Hard to track changes across many files/directories
        
    - Steeper learning curve for newcomers
        
- **Benefits of GUI Tools**
    
    - Visual diff coloring (added vs. removed)
        
    - Point‑and‑click staging/unstaging
        
    - Integrated commit history browsing
        
    - Ability to stage individual lines or hunks
        

---

# 2. Git GUI

## 2.1 Launching

```bash
git gui &
```

- Ampersand (`&`) starts GUI in background so Bash remains usable
    

## 2.2 Main Window Overview

|Pane / Section|Purpose|
|---|---|
|**Unstaged Changes**|Files modified but not yet added to index|
|**Staged Changes**|Files (or hunks) ready to be committed|
|**Diff View**|Center panel shows file content;|

- **Green** = additions
    
- **Red** = deletions
    
- **Black** = unchanged context |  
    | **Commit Message** | Text box for entering `git commit -m "…“` message |  
    | **Buttons** | “Rescan” to refresh file status; “Commit” & “Push” |
    

## 2.3 Workflow Example

1. **Make edits** in an editor (e.g. add two lines to `song.txt`).
    
2. **Rescan** in Git GUI to detect changes.
    
3. **Review Diff**
    
    - Unstaged pane shows `song.txt`
        
    - Center highlights new lines (green) or removed lines (red)
        
4. **Stage Files or Hunks**
    
    - Click blue “+” icon next to file to stage entire file
        
    - Or click within diff to stage individual lines/hunks
        
5. **Write Commit Message**
    
    - E.g. “Add two more lines to song”
        
6. **Commit** locally (does not yet update remote)
    
7. **Push** to origin/master (enter SSH passphrase if prompted)
    
8. **Verify** on GitHub that changes appear
    

---

# 3. Fine‑Grained Staging

- Git GUI allows staging of individual lines (hunks) rather than whole file.
    
- **Use case:** You’ve made multiple unrelated edits in one file but want separate commits.
    
- **How‑to:**
    
    1. In diff view, select only the green/red lines you want.
        
    2. Click the “stage hunk” icon next to that block.
        
    3. Leave other changes unstaged for a later commit.
        

---

# 4. Gitk: Visual Commit History

## 4.1 Launching

```bash
gitk &
```

- Opens a standalone window displaying commit graph
    

## 4.2 Interface Elements

|Pane / Section|Purpose|
|---|---|
|**Commit Graph**|Left: graphical branches & merges, with SHA‑1 labels|
|**Commit List**|Center: commit messages, authors, dates|
|**Diff/Details**|Bottom: shows diff or full file snapshot for selected commit|
|**Search Field**|Filter commits by message content or author|

## 4.3 Reading the Graph

- **Linear history** (no branches): commits arranged top‑to‑bottom
    
- **Branching scenarios**: parallel lines with merge points
    
- **Color‑coded dots** represent branches
    

## 4.4 Example Uses

- **Identify when a bug was introduced**: click successive commits, view diffs
    
- **Audit author information**: see which email/SSH key was used
    
- **Trace merge topology** before releasing
    

---

# 5. Best Practices & Tips

- **Prefer local GUI commits** over GitHub web UI to ensure consistent author/email.
    
- **Use GUI for large refactorings** to visually track dozens of file changes.
    
- **Combine CLI & GUI**:
    
    - CLI for scripting, automation, advanced merges
        
    - GUI for review, staging, and history exploration
        
- **Secure SSH keys**: Always enter passphrase in GUI push/pull prompts to protect private key.
    

---

# 6. Quick Reference: GUI vs. CLI

|Action|CLI Command|Git GUI / gitk|
|---|---|---|
|Stage all changes|`git add .`|Click “stage all” icon|
|Stage specific lines|`git add -p`|Select hunk & click “+”|
|Commit with message|`git commit -m "…"`|Enter message & click “Commit”|
|Push to remote|`git push`|Click “Push” button|
|View commit history|`git log --graph`|Open **gitk**|
|Inspect diff|`git diff`|View in center diff pane|

Use these tools side‑by‑side to streamline your workflow: Bash for precision and scripting; GUI/gitk for clarity and visual insight.