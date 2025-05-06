

# Git’s **.git** Directory: Structure and Function

![[Pasted image 20250506170226.png]]

## Git’s Internal Object Model

Conceptually, the data that Git is storing looks something like this:

![Simple version of the Git data model](https://git-scm.com/book/en/v2/images/data-model-1.png)

Git stores all content in a _content-addressable_ object database. Each file’s contents are stored in a **blob** object (binary large object) identified by its SHA-1 hash; directory snapshots are stored in **tree** objects; and each commit is stored as a **commit** object pointing to a top-level tree and parent commits. For example, Pro Git illustrates a simple model where one tree object references two blob objects (for files like `README` and `Rakefile`) and one subtree (for `lib/`). These three object types are stored as separate files under `.git/objects`. In practice Git commands often inspect them (e.g. `git cat-file -t <sha>` tells you the object type).

- **Blob:** Contains the raw file data (no filename or path). The SHA-1 is computed on the file’s contents (plus a header). Git simply stores the exact bytes of each version of the file. (For example, after hashing “version 1” and “version 2” of a file you get two different blob IDs.) Pro Git notes “you aren’t storing the filename in your system – just the content. This object type is called a blob”.
    
- **Tree:** Represents a directory. A tree object holds a list of entries `(mode, type, SHA-1, name)`, where each entry points to a blob (file) or another tree (subdirectory). In other words, a tree links filenames to blob IDs and sub-tree IDs. For example, `git ls-tree` or `git cat-file -p <tree>` might list lines like `100644 blob a906cb2… README` or `040000 tree 99f1a6… lib/`, showing mode, type, object hash, and filename.
    
- **Commit:** Encapsulates a snapshot. A commit object points to one tree (the project snapshot) and zero or more parent commits. It also records metadata (author, committer, timestamps) and a commit message. The commit format is simple: e.g.

``` bash
tree <tree-sha>
parent <parent-sha>    (if any)
author <name> <email> <timestamp>
committer <name> <email> <timestamp>

Commit message...
```

As Pro Git explains, each commit “specifies the top-level tree for the snapshot of the project at that point; the parent commits if any; the author/committer information; a blank line, and then the commit message”. Every time you run `git commit`, Git writes one of these objects.

These blob, tree, and commit objects form the core data model. Pro Git notes “These three main Git objects — the blob, the tree, and the commit — are initially stored as separate files in your `.git/objects` directory”. (Git also has tag objects for annotated tags, but those are wrappers over commit IDs, not shown here.) Together, the commit objects (linked by parent pointers) form a directed acyclic graph (DAG) of snapshots.

## SHA-1 Hashing and Content-Addressing

Git names and references objects by their SHA-1 hash, making the repository content-addressable. Every object’s ID is the SHA-1 of its contents _plus_ a small header (indicating type and size). This means identical content always yields the same ID, and any change produces a new ID. The SHA-1 is a 40-character hexadecimal string (160 bits). For example, `git hash-object file.txt` outputs a SHA-1, which Git then uses to store the object.

On disk, Git uses the SHA-1 to organize the object files. Inside `.git/objects`, each object is stored in a subdirectory named by the first two hex digits of its SHA-1, with the remaining 38 digits as the filename. For example, an object ID `d670460b4b4aece5915caf5c68d12f560a9fe3e4` would be stored in `.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4`. The object file itself is zlib-compressed content of the blob/tree/commit. (Pro Git demonstrates this layout: after hashing “test content”, a file `.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4` appears.)

This content-addressing provides strong integrity: if any bit of an object changes, its SHA-1 would change, so Git can detect corruption. It also enables deduplication (same content = same object). GitHub even adds collision protection: because SHA-1 collisions are possible in theory, GitHub now rejects Git pushes that show evidence of a collision attack. (Practically, accidental collisions are astronomically unlikely.) Git itself has always detected duplicate object IDs on fetch/push and rejects conflicting objects. Moreover, Git allows cryptographic signing of commits/tags, but those signatures cover the object contents, not the hash function itself.

## Key Files and Directories in **.git**

```tree

├── hooks  
│   └── README.sample  
├── info  
│   └── exclude  
├── logs  
│   ├── refs  
│   │   ├── heads  
│   │   │   ├── dev-miguel  
│   │   │   ├── dev-sergio  
│   │   │   ├── developer  
│   │   │   └── main  
│   │   └── remotes  
│   │       └── origin  
│   │           ├── _developer  
│   │           ├── dev-miguel  
│   │           ├── dev-sergio  
│   │           ├── developer  
│   │           ├── HEAD  
│   │           └── main  
│   └── HEAD  
├── objects  
│   ├── 00  
│   │   └── 42e3d455165bbfee3ac6fba07eafa2abdcfc02  
│   ├── info  
│   └── pack  
│       ├── pack-a7b504321a2304405c9cc6d507c3b97a221b8082.idx  
│       ├── pack-a7b504321a2304405c9cc6d507c3b97a221b8082.pack  
│       ├── pack-dca5035ccae31d0b343df057c0eccf5d0febf38b.idx  
│       ├── pack-dca5035ccae31d0b343df057c0eccf5d0febf38b.pack  
│       └── pack-dca5035ccae31d0b343df057c0eccf5d0febf38b.rev  
├── refs  
│   ├── heads  
│   │   ├── dev-miguel  
│   │   ├── dev-sergio  
│   │   ├── developer  
│   │   └── main  
│   ├── remotes  
│   │   └── origin  
│   │       ├── _developer  
│   │       ├── dev-miguel  
│   │       ├── dev-sergio  
│   │       ├── developer  
│   │       ├── HEAD  
│   │       └── main  
│   └── tags  
├── COMMIT_EDITMSG  
├── config  
├── description  
├── FETCH_HEAD  
├── gitk.cache  
├── HEAD  
├── index  
├── ORIG_HEAD  
└── tree.txt
```

A newly-initialized repository’s `.git` contains these key entries:

- **`config`:** Text file with repository-specific settings (remote URLs, user info overrides, etc).
    
- **`description`:** Used by GitWeb; usually blank in normal repos.
    
- **`HEAD`:** A text file (pointer to the current branch). Typically it contains a line like `ref: refs/heads/master`, meaning HEAD points to that ref. If it contains a raw SHA, you’re in detached-HEAD state.
    
- **`hooks/`:** Directory of hook scripts (client/server side) that Git can run on actions. By default it contains sample scripts like `pre-commit.sample`. Administrators can place executables here (e.g. `post-receive` on a server).
    
- **`info/`:** Miscellaneous metadata. It includes `info/exclude` (a per-repo ignore file not committed) and sometimes global attributes.
    
- **`objects/`:** Core storage for content. As discussed, this holds subdirectories (pack & loose objects) with all the blob/tree/commit data.
    
    - On a fresh repo, `objects/` contains only `pack/` and `info/` (no loose objects yet). The `objects/pack` directory will hold packfiles (`*.pack` and `*.idx`) after network operations or running `git gc`.
        
- **`refs/`:** References (branch and tag pointers). Under `refs/heads/` are branch files (e.g. `refs/heads/master` contains the SHA of the tip commit). Under `refs/tags/` are tag objects. Remote-tracking branches appear in `refs/remotes/`. All these are simple files with commit hashes. (Git may also use a `packed-refs` file to consolidate many refs.) Pro Git notes “the `refs` directory stores pointers into commit objects in that data (branches, tags, remotes and more)”.
    
- **`index`:** This is the staging area file. It is a binary file that Git uses to track the state of the working directory “between” the HEAD commit and the next commit. Initially it may not exist until you run `git add`. The index records file paths, blob IDs, and file metadata.
    
- **`logs/`:** Reflog data. Not in the default listing, but Git maintains `.git/logs/HEAD` and `.git/logs/refs/*` to record each update to HEAD or a ref (for undo/inspect purposes).
    
- **`hooks/`, `info/`, `objects/`, `refs/` (directories) and files (`config`, `HEAD`, etc.)** are all crucial. Modifying them with Git commands is usually safe; hand-editing them can easily corrupt the repo.
    

> _Cited example:_ After `git init`, `ls .git` shows `config`, `description`, `HEAD`, `hooks/`, `info/`, `objects/`, `refs/`. The Pro Git book explains these: “The `config` file contains your project-specific configuration options, and the `info` directory keeps a global exclude file… The `hooks` directory contains your hook scripts”. The remaining core entries are HEAD, index, objects, refs as described above.

## Git’s Directed Acyclic Graph (DAG) of Commits

![All the reachable objects in your Git directory](https://git-scm.com/book/en/v2/images/data-model-3.png)

Git history is modeled as a **directed acyclic graph** (DAG) of commits. Each commit object includes pointers to its parent commit(s). These pointers are directed edges, and there are no cycles (no commit can be an ancestor of itself). For example, an ordinary commit has one parent (the previous commit), while a merge commit has two or more parents. Branches are simply named references to particular commit nodes in the DAG. The commit graph only grows (acyclic), so you can always traverse back through history along parent links without loops. The Git glossary confirms this: “The commit objects form a directed acyclic graph, because they have parents (directed), and the graph of commit objects is acyclic (there is no chain which begins and ends with the same object)”.

In practical terms, this means you can visualize a Git repo’s history as a graph of commits, with arrows pointing from child to parent (time goes in the arrow direction). Commands like `git log --graph` or `gitk` draw this graph. When you do a `git merge`, Git creates a new commit with two parents (joining branches in the DAG). Operations like `git rebase` or `git cherry-pick` actually create new commits (with new IDs) to “reroute” the DAG. The acyclic nature is fundamental: it ensures history is consistent and no infinite loops can occur.

## Inspecting Git Objects (Commands)

Git provides “plumbing” commands to examine the object database. Useful commands include:

- **`git cat-file`** – a Swiss-army tool for objects. You can run `git cat-file -t <sha>` to see an object’s type (blob, tree, commit, or tag). Use `git cat-file -p <sha>` to pretty-print its contents: a blob will show raw file data, a tree will list entries, and a commit will show its metadata (tree, parents, author, message). For example, `git cat-file -p 3c4e9cd7…` might display a tree listing (as in Pro Git) or `git cat-file -p fdf4fc3…` might show a commit “First commit” with author info.
    
- **`git ls-tree`** – lists the contents of a tree object. For instance, `git ls-tree HEAD` (or `git ls-tree <commit-ish>`) outputs lines like

    ```Python
    100644 blob a906cb2a…    README
    040000 tree 99f1a6d1…    lib
    100644 blob 47c6340d…    simplegit.rb
    ```

    Each line shows the mode, type, object hash, and filename. Pro Git notes that “`git ls-tree` outputs the mode, type, object hash, and filename for items inside a tree”. You can follow a tree’s contents down by using `git cat-file -p` on any subtree hash.

    
- **`git show`** – a versatile high-level command. `git show <object>` will display a lot of useful info depending on the object type. According to the `git-show(1)` documentation, it “shows one or more objects (blobs, trees, tags and commits). For commits it shows the log message and textual diff; for tags it shows the tag message and referenced objects; for trees it shows the names (equivalent to git ls-tree --name-only); for plain blobs it shows the contents”. In practice, `git show HEAD` or `git show <commit>` will print the commit details and the diff of that commit. If you give it a blob ID, it prints the file contents. For example, `git show d670460` (taking the first few chars of an object ID) might output raw file content if it’s a blob, or commit info if it’s a commit. (It’s similar to `git cat-file -p` but does some formatting like diff by default.)
    

These commands let you inspect and verify repository internals. Combined with object IDs, you can trace exactly how files and commits are stored. For example, after running `git write-tree` and `git commit-tree` (lower-level plumbing), you could use `git show <new-commit-sha>`, `git ls-tree <tree-sha>`, or `git cat-file -p <sha>` to examine each object.

## Object Storage on Disk

On disk, Git initially stores each object as an individual file (a “loose object”) in `.git/objects/<aa>/<bbbb…>`. As noted, the first two hex characters of the SHA-1 name the subdirectory, and the rest name the file. Pro Git demonstrates this: after creating an object with `git hash-object -w`, the file appears under `.git/objects/d6/70460b4b4aece5915caf5c68d12f560a9fe3e4` for SHA `d670460b4b4aece5915caf5c68d12f560a9fe3e4`.

Over time or after network operations, Git may store objects in _packfiles_ to save space and speed up transfers. The `.git/objects/pack/` directory will contain `.pack` and corresponding `.idx` files. These packfiles bundle many objects (often as deltas) into one file. For example, cloning or fetching usually involves transferring a pack. (One guide explains that a packfile is essentially a concatenation of multiple compressed objects, sometimes stored as diffs for efficiency.) Git’s `git gc` and `git repack` commands can also compress loose objects into packs. The `.idx` is an index for fast lookup inside the `.pack`. Note that if you remove or corrupt a pack or its index, Git will be unable to read the objects inside, so packfiles must match their index.

Another file in object storage is the “exclude” file at `.git/info/exclude`, which works like a per-repo `.gitignore`. This isn’t about object content, but it lives under `.git` and specifies files to ignore.

## Security and Integrity Considerations

The `.git` directory is sacrosanct. Manual edits or exposures can break security and integrity:

- **Integrity via SHA-1:** Because Git uses SHA-1 hashes to identify all objects, altering an object’s content without updating its name will break the SHA-1 integrity check (Git would see the file’s contents don’t match its filename). If two different contents ever produce the same SHA-1 (a _collision_), Git cannot distinguish them. To guard against collision attacks, GitHub detects and rejects any content that looks like a SHA-1 collision. Git itself also verifies object contents on fetch/push and will refuse to fetch an object if its SHA-1 doesn’t match the expected value. Note that Git’s security model relies on transport and optional signatures, not SHA-1 secrecy: GitHub’s blog notes Git doesn’t rely on SHA-1 for trust, but on HTTPS/SSH and commit/tag GPG signatures.
    
- **Expose Risk (.git leaks):** If an attacker gains access to your `.git` directory (for example, via a misconfigured web server that serves the `.git` folder), they essentially get the entire repository history. Every commit, file blob, branch, and tag can be downloaded by traversing `.git/objects` and `.git/refs`. Tools exist to reconstruct a repository from a leaked `.git`. Thus, never expose `.git` publicly (on a website or network share) without proper protection. Likewise, ensure access controls on any Git hosting service (GitHub, GitLab, etc.) are configured correctly, since private repos may contain sensitive data.
    
- **Manual Edits and Repo Corruption:** Directly editing files inside `.git` (HEAD, refs, objects, index, etc.) is dangerous. For instance, changing `.git/HEAD` to an arbitrary hash or branch name without using `git` commands can lead to a detached HEAD or point to a non-existent commit. Deleting or corrupting files under `.git/objects` will make commits or blobs unreachable, and Git commands like `git log` or `git status` will break (you can see missing-object errors). Modifying the index file externally could corrupt your staging area. In short, always use Git commands (`git branch`, `git update-ref`, `git commit`, etc.) to change history or metadata. If you somehow need to recover from a broken `.git`, tools like `git fsck` can diagnose corruption, and you may manually restore objects if you understand the internals. But manual tampering is not recommended.
    

In summary, the **`.git`** directory is the heart of a Git repository: it stores all data (objects, refs, metadata) and implements Git’s versioning via content hashes and a commit graph. Understanding its structure (objects folder, refs, index, etc.) and how Git uses SHA-1 and DAGs provides deep insight into Git’s behavior. For everyday use, these details are transparent, but for debugging or advanced tooling, commands like `git ls-tree`, `git cat-file`, and `git show` let you inspect exactly what’s inside **`.git`**.

**Sources:** Pro Git (Git Internals chapters) [git-scm.com](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=Git%20has%20initialized%20the%20,in%20your%20new%20Git%20database)[git-scm.com](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=The%20format%20for%20a%20commit,and%20then%20the%20commit%20message)[git-scm.com](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=The%20next%20type%20of%20Git,recent), official Git documentation (git-show, git-ls-tree, gitglossary) [git-scm.com](https://git-scm.com/docs/git-show#:~:text=DESCRIPTION)[git-scm.com](https://git-scm.com/book/en/v2/Git-and-Other-Systems-Git-as-a-Client#:~:text=So%20,is%20the%20ID%20of%20the)[git-scm.com](https://git-scm.com/docs/gitglossary/2.19.0#:~:text=DAG), and GitHub engineering blog [github.blog](https://github.blog/news-insights/company-news/sha-1-collision-detection-on-github-com/#:~:text=Why%20does%20SHA,Git)[github.blog](https://github.blog/news-insights/company-news/sha-1-collision-detection-on-github-com/#:~:text=If%20a%20Git%20fetch%20or,this%20detection%20since%20its%20inception).

---
## MicroTest

- ### The file .git/refs/heads/master contains the following text: "5c2fdbaff3b0b9b5eae3c48047aafcee2201e5c4". What does it mean?
	- This is sha 1 of the last commit in the master branch
- ### What do the directory names in the .git / objects folder mean?
	- The first two characters from sha 1

---

[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=The%20next%20type%20of%20Git,recent)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=Amazing,now%2C%20commented%20with%20what%20they)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=The%20output%20from%20the%20above,Git%20has%20stored%20your%20data)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=But%20remembering%20the%20SHA,t)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=%24%20git%20cat,lib)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=The%20format%20for%20a%20commit,and%20then%20the%20commit%20message)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=If%20you%20again%20examine%20your,is%20the%20remaining%2038%20characters)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=%24%20find%20.git%2Fobjects%20,git%2Fobjects%2Fd6%2F70460b4b4aece5915caf5c68d12f560a9fe3e4)  
[SHA-1 collision detection on GitHub.com - The GitHub Blog](https://github.blog/news-insights/company-news/sha-1-collision-detection-on-github-com/#:~:text=Why%20does%20SHA,Git)  
[SHA-1 collision detection on GitHub.com - The GitHub Blog](https://github.blog/news-insights/company-news/sha-1-collision-detection-on-github-com/#:~:text=If%20a%20Git%20fetch%20or,this%20detection%20since%20its%20inception)  
[Git - Plumbing and Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain#:~:text=%24%20ls%20,HEAD%20hooks%2F%20info%2F%20objects%2F%20refs)  
[Git - Plumbing and Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain#:~:text=Git.%20The%20,Git%20stores%20your%20staging%20area)  
[Git - Plumbing and Porcelain](https://git-scm.com/book/en/v2/Git-Internals-Plumbing-and-Porcelain#:~:text=Depending%20on%20your%20version%20of,detail%20in%20%20141%20Git)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=Git%20has%20initialized%20the%20,in%20your%20new%20Git%20database)  
[Git - gitglossary Documentation](https://git-scm.com/docs/gitglossary/2.19.0#:~:text=DAG)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=Once%20you%20have%20content%20in,content%2C%20then%20display%20it%20appropriately)  
[Git - Git Objects](https://git-scm.com/book/en/v2/Git-Internals-Git-Objects#:~:text=%24%20git%20cat,0700)  
[Git - Git as a Client](https://git-scm.com/book/en/v2/Git-and-Other-Systems-Git-as-a-Client#:~:text=So%20,is%20the%20ID%20of%20the)  
[Git - git-show Documentation](https://git-scm.com/docs/git-show#:~:text=DESCRIPTION)  
[Git Internals part 2: packfiles - DEV Community](https://dev.to/calebsander/git-internals-part-2-packfiles-1jg8#:~:text=The%20convenient%20lie%20from%20the,packfile%20to%20reduce%20storage%20space)  
