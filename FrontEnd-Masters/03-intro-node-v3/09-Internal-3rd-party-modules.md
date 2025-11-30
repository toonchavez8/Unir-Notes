# Study Notes: Useful Internal Node.js Modules and Npm Fundamentals

## 1. Introduction

This transcript focuses on:

- Core internal modules in Node.js
    
- Practical use cases of modules like `fs`, `http`, and `path`
    
- Understanding how npm installs and manages packages
    
- The role of `node_modules`, `package.json`, and `package-lock.json`
    
- Security considerations when installing packages
    
- Installing and uninstalling dependencies

---

## 2. Core Internal Node.js Modules

### 2.1 The `fs` Module (File System)

**Definition:**  
`fs` is a built-in Node.js module that allows JavaScript code to interact with the file system.

**Capabilities:**

- Read and write files
    
- Modify, delete, or list directories
    
- Perform almost any file operation a human can do manually

**Relevance:**

- Essential for scripts that generate files
    
- Used by tools such as project scaffolding scripts (e.g., Create React App)
    
- Supports synchronous and asynchronous operations

**Examples of common methods:**

|Method|Description|
|---|---|
|`fs.readFile`|Reads file contents|
|`fs.writeFile`|Writes or replaces file content|
|`fs.appendFile`|Appends to an existing file|
|`fs.readdir`|Lists files in a directory|

---

### 2.2 The `http` Module

**Definition:**  
A core module for creating servers and handling HTTP networking.

**Use cases:**

- Creating web servers
    
- Sending JSON or files as responses
    
- Managing low-level HTTP communication

**Notes:**

- Considered low-level
    
- Most developers use frameworks built on top of it (e.g., Express.js)

---

### 2.3 The `path` Module

**Definition:**  
Utility module for handling file paths.

**Notes:**

- Less common today due to improved tooling and modern JS features
    
- Still useful for cross-platform path handling

---

## 3. Introduction to Npm (Node Package Manager)

### 3.1 What is Npm?

**Definition:**  
npm = **Node Package Manager**, the tool responsible for installing, managing, and updating packages in Node.js projects.

**Key functions:**

- Initialize projects (`npm init`)
    
- Install packages (`npm install <package>`)
    
- Manage dependencies versions
    
- Provide access to a massive open-source repository

---

## 4. Installing Packages with Npm

### 4.1 Basic Installation

Command:

```Python
npm install <package-name>
```

or its shorthand:

```Python
npm i <package-name>
```

### 4.2 Example: Installing an EXIF Parser

Search for packages by:

- `npm <feature>` on Google
    
- Visiting npmjs.com

Example package:

```Python
npm install exif-parser
```

---

## 5. The `node_modules` Folder

**Definition:**  
Directory where all installed dependencies live.

**Characteristics:**

- Auto-created when first package is installed
    
- Should **never** be committed to Git
    
- Contains a massive dependency graph (can be thousands of files)

**Why not push to Git?**

|Reason|Explanation|
|---|---|
|Huge size|Millions of lines of code not written by you|
|Slows PRs|Every update looks like massive changes|
|Not necessary|npm can recreate it at any time|

---

## 6. The `package.json` and `package-lock.json` Files

### 6.1 `package.json`

**Purpose:**

- Lists project metadata
    
- Defines dependencies and their version ranges

Example entry:

```json
"dependencies": {
  "exif-parser": "^0.1.2"
}
```

### 6.2 `package-lock.json`

**Purpose:**

- Locks exact dependency versions
    
- Ensures all environments use identical versions

**Why needed?**

- Prevents unexpected behavior on other machines
    
- Ensures deterministic builds

---

## 7. Reinstalling Dependencies

If `node_modules` is deleted:

```Python
npm install
```

npm reads:

- `package.json`
    
- `package-lock.json`

And reinstalls everything exactly as before.

---

## 8. Uninstalling Packages

Command:

```Python
npm uninstall <package-name>
```

Effects:

- Removes package from `node_modules`
    
- Removes entry from `package.json`
    
- Updates `package-lock.json`

---

## 9. Security Considerations with Npm Packages

### 9.1 Risks

- Broken packages can disrupt large parts of the ecosystem
    
- Malicious code may be uploaded by bad actors
    
- Maintainers may abandon projects

### 9.2 Real-world Example

A small dependency breaking caused widespread outages across major packages and services.

### 9.3 How to Protect Yourself

Minimal checks:

- Review GitHub activity
    
- Check issue reports
    
- Look at last update date
    
- Confirm community usage

**Most developers do not audit code line-by-line.**

### 9.4 Enterprise Practices

- Whitelisting
    
- Legal review for IP concerns
    
- Internal package mirrors

---

## 10. Summary of Key Points

- Node.js includes powerful internal modules (`fs`, `http`, `path`).
    
- `fs` allows full file system control; essential for many tools.
    
- npm manages dependency installation and versioning.
    
- Dependencies are installed into `node_modules` but must not be committed to Git.
    
- `package.json` stores dependency names; `package-lock.json` locks exact versions.
    
- Use `npm install` to install packages and `npm uninstall` to remove them.
    
- Some npm packages can be outdated, broken, or malicious, so basic due diligence is important.

---

## MicroTest