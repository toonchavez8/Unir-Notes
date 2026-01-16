# Modules in JavaScript and Node.js – Study Notes

---

# 1. Concept of a Module

## Definition

A **module** is a self-contained, isolated block of code that:

- Has its own scope
    
- Does not pollute the global environment
    
- Can expose only what it wants to share
    
- Can be reused across different parts of an application

## Analogy

A module is like a **Lego block**:

- It is self-contained
    
- It can connect to other blocks only where and how you choose
    
- Internal details stay hidden unless intentionally exposed

---

# 2. Historical Context: IIFE and Encapsulation

## IIFE (Immediately Invoked Function Expression)

Before modules existed, developers used IIFEs to encapsulate code:

```js
(function () {
  console.log("Hello");
})();
```

**Purpose of an IIFE:**

- Creates a **private scope**
    
- Protects code from global namespace pollution
    
- Prevents collisions with other scripts (e.g., scripts loaded via `<script>` tags or Bower packages)

## Why It Was Needed

Before modern modules or bundlers:

- All JS was global
    
- Libraries included through `<script>` tags could override each other
    
- Encapsulation was manual

Modules solved this elegantly by providing **built-in scope isolation**.

---

# 3. Types of Modules in Node.js

Node.js supports **three categories of modules**:

|Type|Description|Examples|
|---|---|---|
|**Internal/Built-in modules**|Provided by Node.js|`http`, `fs`, `path`|
|**User-created modules**|Code written by you|Custom utilities, helpers|
|**Third-party modules**|Created by others, installed via npm|`lodash`, `express`, `chalk`|

All follow the same principles of scope isolation and export/import.

---

# 4. Module Systems in Node.js

Node.js supports two main module syntaxes:

|System|Syntax|Notes|
|---|---|---|
|**CommonJS (older)**|`require()` / `module.exports`|Default before Node 18|
|**ES Modules (ESM)**|`import` / `export`|Requires enabling in `package.json`|

This lesson uses **ES Modules**.

---

# 5. Enabling ES Modules in Node.js

To use `import` and `export`, update `package.json`:

```json
{
  "type": "module"
}
```

Without this, Node will assume CommonJS and reject ES module syntax.

---

# 6. Creating and Exporting a User Module

## Example: `utils.js`

```js
export function count(num) {
  return num;
}
```

This is a **named export**.

## Characteristics of a Named Export

- Must be imported using the **same name**
    
- Must be imported using **curly braces**

---

# 7. Importing a Named Export

## Example: `index.js`

```js
import { count } from "./utils.js";
```

Important rule in Node ES Modules:

- **You must include the `.js` file extension**  
    Node treats everything as a module: CSS, images, JSON, etc.  
    Extensions avoid ambiguity.

---

# 8. Default Exports

A file may export **one default value**:

## Example: `utils.js`

```js
export default {
  name: "Utils",
  version: 1
};
```

## Key Characteristics of Default Exports

- They do **not** use curly braces when imported
    
- The import name can be **anything**

## Importing a Default Export

```js
import data from "./utils.js";
```

## Combined Import (default + named)

```js
import data, { count } from "./utils.js";
```

Only what is declared as the **default export** gets exported—nothing else.

---

# 9. Summary of Import/Export Types

|Export Type|Syntax|Import Syntax|Must Match Name?|
|---|---|---|---|
|**Named Export**|`export function a(){}`|`import { a } from './file.js'`|Yes|
|**Default Export**|`export default something`|`import anyName from './file.js'`|No|

---

# 10. Key Takeaways

- A **module** encapsulates code and controls what is shared.
    
- IIFEs historically provided encapsulation before modules existed.
    
- Node.js supports built-in, user-created, and third-party modules.
    
- ES Modules require `"type": "module"` in `package.json`.
    
- Use `.js` extensions in ESM imports in Node.
    
- Named exports require matching names; default exports do not.

---

# MicroTest