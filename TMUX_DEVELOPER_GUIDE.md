# tmux Developer Guide

## Goal

Use `tmux` to keep long-running dev sessions stable, split work clearly, and switch contexts fast without opening new windows.

## Core Concepts

- **Session**: a named workspace (example: `codex`, `api`, `frontend`).
- **Window**: a tab inside a session.
- **Pane**: a split region inside a window.

## Daily Commands

```bash
tmux new -s codex         # create session
tmux a -t codex           # attach to session
tmux ls                   # list sessions
tmux kill-session -t codex
```

## Default Prefix

- Prefix is `Ctrl+b`.
- Most tmux commands are: `Ctrl+b`, then a key.

## Pane Workflow (Most Important)

- `Ctrl+b` then `v`: split vertically (top/bottom).
- `Ctrl+b` then `h`: split horizontally (left/right).
- `Ctrl+b` then arrow key: move between panes.
- `Ctrl+b` then `z`: zoom/unzoom current pane.
- `Ctrl+b` then `x`: close current pane.

## Window Workflow

- `Ctrl+b` then `c`: create window.
- `Ctrl+b` then `n`: next window.
- `Ctrl+b` then `p`: previous window.
- `Ctrl+b` then `,`: rename window.
- `Ctrl+b` then `&`: close window.

## Copy/Search Workflow

- `Ctrl+b` then `[` enters scroll/copy mode.
- In copy mode (vi keys enabled):
  - `/text` search forward
  - `n` next match
  - `q` exit copy mode

## Dev Layout Patterns

### Pattern 1: Coding + Tests

- Left pane: editor or Codex.
- Right pane: tests/watch mode.

### Pattern 2: Full-Stack

- Pane 1: frontend dev server.
- Pane 2: backend service.
- Pane 3: logs or DB shell.

### Pattern 3: Codex + Voice

- Top pane: Codex conversation/input.
- Bottom pane: voice trigger shell (`v` command).

## Reliability Habits

- Keep one session per project.
- Name sessions clearly (`project-api`, `project-ui`).
- Do not close terminal windows before detaching:
  - `Ctrl+b` then `d`
- Reattach later with `tmux a -t <session>`.

## Config You Already Use

Current config in `~/.tmux.conf` supports:

- Mouse mode
- Large history
- Vi mode keys
- Split shortcuts:
  - `Ctrl+b` then `v`
  - `Ctrl+b` then `h`
- Reload config:
  - `Ctrl+b` then `r`

## Fast Start

```bash
vcodex             # open/attach codex session
Ctrl+b, v          # split top/bottom
# top pane:
vtarget
# bottom pane:
v
```
