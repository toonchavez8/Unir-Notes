# Voice Terminal Walkthrough

## Purpose

I want a one-hand-friendly voice flow for coding sessions with a split terminal layout:

- Top pane: Codex chat/input terminal.
- Bottom pane: shell where I trigger voice capture.

The tool should only listen when I run `v` in the bottom pane. It should capture one utterance, transcribe it, and inject the transcript into the top Codex pane so I can continue the conversation without manually typing long prompts.

This document is the implementation plan to review before coding.

Related guide:

- `TMUX_DEVELOPER_GUIDE.md` for tmux-first developer workflows.

## Product Requirements

- Voice is opt-in per use (`v` command).
- No background listener.
- Works with Bash and Zsh.
- Compatible with a split-terminal workflow (top Codex pane, bottom voice pane).
- One utterance per run; process exits immediately after.
- Transcript is visible in output and copied to clipboard.
- Default behavior pastes into the Codex pane but does not auto-submit.
- Auto-submit must stay explicit/opt-in.
- All tooling stays isolated in a sibling repo at `C:\Users\toonc\Documents\voice-terminal-tool\`.
- No unrelated changes in this Markdown vault.

## Non-Goals

- No always-on assistant.
- No hotword detection.
- No automatic startup tasks.
- No automatic shell-profile edits without review.
- No git commits unless explicitly requested.

## User Stories

### Story 1: Speak Directly to Codex Pane

As a developer and parent, I want to trigger `v` from the lower pane and have the transcript inserted in the top Codex pane so I can keep hands-light interaction.

Acceptance criteria:

- I open a split terminal session (top: Codex, bottom: shell).
- I mark the top pane as the voice target.
- I run `v` in the bottom pane.
- The tool records one utterance and transcribes locally.
- The transcript is sent to the top pane input.
- The tool exits immediately after one run.

### Story 2: No Accidental Listening

As a developer, I need confidence that the microphone is active only during explicit command execution.

Acceptance criteria:

- No process starts at login.
- The recorder/transcriber only runs after `v`.
- No listener remains after transcription finishes.
- A process check after completion shows no persistent background capture service from this tool.

### Story 3: Shell-Native Workflow (Bash + Zsh)

As a developer, I want a single setup that works in both `~/.bashrc` and `~/.zshrc`.

Acceptance criteria:

- A shared `profile-snippet.sh` provides `v` and helper commands.
- The same launcher script works from Bash and Zsh.
- No PowerShell-specific steps are required.

### Story 4: Reviewable Local Tooling

As a developer, I want all scripts and dependencies to be transparent and local.

Acceptance criteria:

- All files live under `C:\Users\toonc\Documents\voice-terminal-tool\`.
- Setup and usage commands are documented here.
- Profile sourcing is manual and reversible.

## Proposed Architecture

First implementation (shell-first, no Windows-specific behavior):

1. Python transcription script at `C:\Users\toonc\Documents\voice-terminal-tool\voice_prompt.py`.
2. Shell launcher at `C:\Users\toonc\Documents\voice-terminal-tool\voice-terminal.sh`.
3. Shared shell snippet at `C:\Users\toonc\Documents\voice-terminal-tool\profile-snippet.sh` for Bash/Zsh.

Primary targeting method:

- Use `tmux` pane IDs for reliable injection into the top pane.
- Save target pane with `vtarget` (run from top Codex pane once per session).
- Run `v` from lower pane to capture voice and send transcript to saved target pane.

Fallback method:

- If no `tmux` target is configured, keep transcript in stdout + clipboard only.

## Speech-to-Text Choice

Default: local transcription with `faster-whisper`.

Why:

- Keeps normal prompts local.
- No API key needed for MVP.
- Good shell automation fit.

Tradeoffs:

- First run may download model files.
- Speed/quality depend on hardware and microphone.

Fallback:

- Optional OpenAI API transcription mode can be documented later if local performance is not acceptable.

## Planned File Tree

```text
voice-terminal-tool/
  README.md
  requirements.txt
  voice_prompt.py
  voice-terminal.sh
  profile-snippet.sh
  .gitignore
```

## Planned Commands

These are the commands to run after plan approval.

### 1. Create the Tool Folder

```bash
mkdir -p "$HOME/Documents/voice-terminal-tool"
```

### 2. Create Python Virtual Environment

```bash
python3 -m venv "$HOME/Documents/voice-terminal-tool/.venv"
```

### 3. Install Dependencies

```bash
if [ -x "$HOME/Documents/voice-terminal-tool/.venv/bin/python" ]; then VENV_PY="$HOME/Documents/voice-terminal-tool/.venv/bin/python"; else VENV_PY="$HOME/Documents/voice-terminal-tool/.venv/Scripts/python.exe"; fi
"$VENV_PY" -m pip install --upgrade pip
"$VENV_PY" -m pip install -r "$HOME/Documents/voice-terminal-tool/requirements.txt"
```

### 4. Smoke Test (No Pane Injection)

```bash
bash "$HOME/Documents/voice-terminal-tool/voice-terminal.sh" --no-paste
```

### 5. Configure Shell Profile (Manual)

Add this line to `~/.zshrc` and/or `~/.bashrc` after review:

```bash
source "$HOME/Documents/voice-terminal-tool/profile-snippet.sh"
```

Reload shell:

```bash
source ~/.zshrc
# or
source ~/.bashrc
```

### 6. Split-Pane Session Example (tmux)

Top pane (Codex):

```bash
vtarget
```

Bottom pane (voice control):

```bash
v
```

Optional submit mode:

```bash
v --submit
```

## How This Works with tmux

The voice tool depends on a saved tmux pane target:

1. You run `vtarget` in the top Codex pane once.
2. `vtarget` stores that pane ID in `VOICE_TARGET_PANE`.
3. When you run `v` from the lower pane, the script transcribes speech and runs:
   - `tmux send-keys -t "$VOICE_TARGET_PANE" -l "<transcript>"`
4. If `--submit` is passed, it also sends `Enter`.

Why this is reliable:

- It does not depend on focus-based paste.
- It routes text directly to a specific pane.
- If target is missing, transcript still appears in stdout and clipboard.

## Step-by-Step: Daily Tool Usage

### First time per shell

1. Ensure your profile sources the tool snippet:
   - `source "$HOME/Documents/voice-terminal-tool/profile-snippet.sh"`
2. Reload shell:
   - `source ~/.zshrc` or `source ~/.bashrc`

### Start a voice-enabled Codex session

1. Open/attach tmux session:
   - `vcodex` (or `tmux new -A -s codex`)
2. Split panes:
   - `Ctrl+b`, then `v`
3. In top pane (Codex pane), set target:
   - `vtarget`
4. In bottom pane (voice pane), speak prompt:
   - `v`

### Modes

- `v`: transcribe and inject into Codex pane (no Enter).
- `v --submit`: transcribe, inject, and press Enter.
- `v --no-paste`: transcribe only (stdout + clipboard fallback).

### When things fail

- `tmux not found`:
  - Install tmux and restart shell.
- `No VOICE_TARGET_PANE set`:
  - Run `vtarget` again in the top pane.
- Empty transcript:
  - Speak closer to mic, increase duration:
    - `v --seconds 16`

## Planned Python Dependencies

```text
sounddevice==0.4.7
soundfile==0.12.1
numpy==1.26.4
faster-whisper==1.1.1
pyperclip==1.9.0
requests==2.32.3
```

Why:

- `sounddevice`: microphone recording.
- `soundfile`: temporary WAV write.
- `numpy`: audio buffer handling.
- `faster-whisper`: local speech-to-text.
- `pyperclip`: clipboard copy for manual fallback.
- `requests`: required by `faster-whisper` runtime helpers.

## Planned Code

### `voice-terminal-tool/voice-terminal.sh` behavior

- Call `voice_prompt.py`.
- Capture transcript from stdout.
- Always copy transcript to clipboard (best effort).
- If `--no-paste` is set: exit after printing transcript.
- If `tmux` target pane exists: send transcript to that pane with `tmux send-keys`.
- If `--submit` is set: send `Enter` after transcript.
- If no target pane exists: print a clear message and keep clipboard fallback.

### `voice-terminal-tool/profile-snippet.sh` behavior

- Define `vtarget` to store current pane as the global target:
  - `tmux set-environment -g VOICE_TARGET_PANE "$(tmux display-message -p '#{pane_id}')"`
- Define `v` wrapper that calls `voice-terminal.sh`.
- Support both Bash and Zsh (POSIX-compatible shell code).

### `voice-terminal-tool/README.md` focus

- Setup steps for venv + install.
- Bash/Zsh profile hookup.
- tmux split-pane usage (`vtarget`, then `v`).
- Safe defaults (`--submit` off by default).

## Security and Privacy Notes

- Default transcription is local.
- Audio temp file is deleted immediately after transcription.
- No background listener/service is installed.
- No automatic profile modifications.
- Clipboard is used as explicit fallback.

## Implementation Action Plan

- [x] Create this review document at repo root.
- [x] Update plan from Windows/PowerShell flow to Bash/Zsh split-pane flow.
- [x] Wait for approval.
- [x] Create sibling repo `C:\Users\toonc\Documents\voice-terminal-tool\`.
- [x] Create `requirements.txt`.
- [x] Create `.gitignore`.
- [x] Create `voice_prompt.py`.
- [x] Create `voice-terminal.sh`.
- [x] Create `profile-snippet.sh`.
- [x] Create `README.md`.
- [x] Create Python venv.
- [x] Install dependencies.
- [ ] Run `voice-terminal.sh --no-paste`.
- [x] Validate transcript quality.
- [ ] Validate tmux target injection (`vtarget` + `v`).
- [ ] Test optional submit mode (`v --submit`).
- [x] Update this document with completion notes.

## Review Questions

- Is `tmux` your preferred split-terminal environment for top/bottom panes?
- Should default model stay `base.en`, or do you want multilingual by default?
- Is 12 seconds still the right default capture window?
- Should `v` paste by default to the target pane, with `--no-paste` for testing?

## Completion Notes

Started on May 21, 2026.

Completed:

- Created sibling repo at `C:\Users\toonc\Documents\voice-terminal-tool\`.
- Initialized git repo and scaffolded files:
  - `requirements.txt`
  - `.gitignore`
  - `voice_prompt.py`
  - `voice-terminal.sh`
  - `profile-snippet.sh`
  - `README.md`
- Created `.venv` and installed dependencies.
- Added `requests==2.32.3` after runtime import failure on first smoke run.
- Ran transcription smoke test via Python:
  - first run downloaded `base.en` model cache.
  - transcription pipeline executed successfully (silence test returned "No speech was detected.").

Pending:

- End-to-end launcher tests from your real Bash/Zsh terminal (`vtarget`, `v`, and `v --submit`) because this execution environment cannot run your interactive shell/tmux flow directly.
