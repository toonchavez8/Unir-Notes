Perfect — here’s a **clean, practical Vim-style hotkeys guide** tailored specifically for **PowerToys (Windows)** + **Vimium (Browser)**.  
This is written as a **reference cheat sheet** you can keep nearby.

---

# 🧠 Keyboard-Only Navigation Guide

**Using PowerToys + Vimium**

---

## 🖥️ System Navigation (Windows + PowerToys)

|Action|Keyboard|
|---|---|
|Open app / file / setting|**PowerToys Run:** `Alt + Space`, then type|
|Switch between apps|`Alt + Tab`|
|Switch between windows of same app|`Alt + ``|
|Move window|`Win + Arrow Keys`|
|Maximize / restore window|`Win + ↑` / `Win + ↓`|
|Close window|`Alt + F4`|
|Virtual desktops|`Win + Ctrl + ← / →`|
|Create new desktop|`Win + Ctrl + D`|
|Close current desktop|`Win + Ctrl + F4`|

---

## 🌐 Browser Navigation (Vimium)

### General

|Action|Key|
|---|---|
|Show Vimium help|`?`|
|Reload page|`r`|
|View source|`gs`|
|Copy current URL|`yy`|
|Enter insert mode (text fields)|`i`|
|Exit insert / cancel|`Esc`|

---

### Scrolling

|Action|Key|
|---|---|
|Scroll down|`j`|
|Scroll up|`k`|
|Scroll left|`h`|
|Scroll right|`l`|
|Half-page down|`d`|
|Half-page up|`u`|
|Top of page|`gg`|
|Bottom of page|`G`|

---

### Links & Navigation

|Action|Key|
|---|---|
|Open link|`f`|
|Open link in new tab|`F`|
|Open multiple links|`Alt + f`|
|Go up URL hierarchy|`gu`|
|Next page (pagination)|`]]`|
|Previous page|`[[`|

---

### Find on Page

|Action|Key|
|---|---|
|Find|`/`|
|Next match|`n`|
|Previous match|`N`|
|Cancel find|`Esc`|

---

### History

| Action | Key |
| ------ | --- |
| Back   | `   |

## Keyboard Bindings

Modifier keys are specified as `<c-x>`, `<m-x>`, and `<a-x>` for ctrl+x, meta+x, and alt+x respectively. For shift+x and ctrl-shift-x, just type `X` and `<c-X>`. See the next section for how to customize these bindings.

Once you have Vimium installed, you can see this list of key bindings at any time by typing `?`.

Navigating the current page:

```Python
?       show the help dialog for a list of all available keys
h       scroll left
j       scroll down
k       scroll up
l       scroll right
gg      scroll to top of the page
G       scroll to bottom of the page
d       scroll down half a page
u       scroll up half a page
f       open a link in the current tab
F       open a link in a new tab
r       reload
gs      view source
i       enter insert mode -- all commands will be ignored until you hit Esc to exit
yy      copy the current url to the clipboard
yf      copy a link url to the clipboard
gf      cycle forward to the next frame
gF      focus the main/top frame
```

Navigating to new pages:

```Python
o       Open URL, bookmark, or history entry
O       Open URL, bookmark, history entry in a new tab
b       Open bookmark
B       Open bookmark in a new tab
```

Using find:

```Python
/       enter find mode
          -- type your search query and hit enter to search, or Esc to cancel
n       cycle forward to the next find match
N       cycle backward to the previous find match
```

For advanced usage, see [regular expressions](https://github.com/philc/vimium/wiki/Find-Mode) on the wiki.

Navigating your history:

```Python
H       go back in history
L       go forward in history
```

Manipulating tabs:

```Python
J, gT   go one tab left
K, gt   go one tab right
g0      go to the first tab. Use ng0 to go to n-th tab
g$      go to the last tab
^       visit the previously-visited tab
t       create tab
yt      duplicate current tab
x       close current tab
X       restore closed tab (i.e. unwind the 'x' command)
T       search through your open tabs
W       move current tab to new window
<a-p>   pin/unpin current tab
```

Using marks:

```Python
ma, mA  set local mark "a" (global mark "A")
`a, `A  jump to local mark "a" (global mark "A")
``      jump back to the position before the previous jump
          -- that is, before the previous gg, G, n, N, / or `a
```

Additional advanced browsing commands:

```Python
]], [[  Follow the link labeled 'next' or '>' ('previous' or '<')
          - helpful for browsing paginated sites
<a-f>   open multiple links in a new tab
gi      focus the first (or n-th) text input box on the page. Use <tab> to cycle through options.
gu      go up one level in the URL hierarchy
gU      go up to root of the URL hierarchy
ge      edit the current URL
gE      edit the current URL and open in a new tab
zH      scroll all the way left
zL      scroll all the way right
v       enter visual mode; use p/P to paste-and-go, use y to yank
V       enter visual line mode
R       Hard reload the page (skip the cache)
```

Vimium supports command repetition so, for example, hitting `5t` will open 5 tabs in rapid succession. `<Esc>` (or `<c-[>`) will clear any partial commands in the queue and will also exit insert and find modes.

There are additional commands which aren't included in this README; refer to the help dialog (type `?`) for a full list.