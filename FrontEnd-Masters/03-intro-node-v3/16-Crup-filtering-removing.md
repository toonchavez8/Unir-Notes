# Notes: CRUD Operations for Notes – Filtering, Removing, and Resetting Data

## 1. Overview

This section covers how to implement search, deletion, and bulk deletion for a simple Notes database. The database is managed through previously created abstraction functions (`getDB`, `insert`, `saveDB`). All operations are asynchronous and interact with a JSON file acting as a pseudo-database.

---

# 2. Implementing `findNotes()`

## Purpose

`findNotes(filter)` searches all notes and returns those whose **content** contains the provided substring. This serves as a basic form of _full-text search_.

## Key Concepts

### Full-Text Search (Simplified)

A search technique where you look for a substring inside larger text entries. Here, the implementation uses:

```js
string.includes(otherString)
```

This is a simple match, not a sophisticated search engine.

### Case Normalization

String comparison is case-sensitive, so `"Dog"` ≠ `"dog"`.  
Solution: normalize both sides to lowercase before comparison.

## Implementation

```js
export const findNotes = async (filter) => {
    const { notes } = await getDB();
    return notes.filter(note =>
        note.content.toLowerCase().includes(filter.toLowerCase())
    );
};
```

### How it Works (Step-by-Step)

1. Load all notes from the database.
    
2. Apply `.filter()` to create a **new array**.
    
3. For each note:
    
    - Lowercase the content.
        
    - Lowercase the filter text.
        
    - Check if `note.content.includes(filter)` is true.
        
4. Return the filtered array (may be empty).
    

## Example

### Notes Example

|Content|
|---|
|"Walk my dog today"|
|"Finish homework"|
|"My DOG ran outside"|

### Query

`filter = "my dog"`

### Matching Process

- `"Walk my dog today"` → matches
    
- `"My DOG ran outside"` → matches
    
- `"Finish homework"` → does not match
    

### Result

Returns an array of the two matching notes.

## Mermaid Diagram: Find Notes Flow

```mermaid
flowchart TD
    A[Input filter string] --> B[Load all notes via getDB()]
    B --> C[Normalize content and filter to lowercase]
    C --> D[Filter: content.includes(filter)]
    D --> E[Return array of matches]
```

---

# 3. Implementing `removeNote()`

## Purpose

`removeNote(id)` deletes a note by its ID. It uses an immutable approach—creating a new array without the matched note.

## Key Concepts

### Finding an Item

Uses `.find()` to verify if a note with the specified ID exists.

### Immutable Update

Instead of mutating the original array, a new array is created:

```js
notes.filter(note => note.id !== id)
```

This avoids side effects and makes the code easier to reason about.

## Implementation

```js
export const removeNote = async id => {
    const { notes } = await getDB();

    const match = notes.find(note => note.id === id);
    if (!match) return undefined;

    const newNotes = notes.filter(note => note.id !== id);

    await saveDB({ notes: newNotes });
    return id;
};
```

## Step-by-Step Process

1. Load all notes.
    
2. Check if any note matches the id (`.find`).
    
3. If no match → return `undefined`.
    
4. Create a new array excluding the note with that id.
    
5. Save updated notes to the database.
    
6. Return the removed id.
    

## Why Use Immutable Filtering Instead of Mutation?

|Approach|Characteristics|
|---|---|
|**Immutable (recommended)**|Creates a new array; avoids side effects; easier to debug.|
|**Mutation**|Removes the item in place (`splice`, etc.); can cause issues in complex systems.|

---

# 4. Implementing `removeAllNotes()`

## Purpose

Deletes _all_ notes by resetting the notes array to empty.

## Implementation

```js
export const removeAllNotes = () =>
    saveDB({ notes: [] });
```

## Why No `async/await`?

Because the function simply returns the promise from `saveDB` and does not need to perform additional operations after saving.

---

# 5. Functions Summary Table

|Function|Parameters|Description|Return Value|
|---|---|---|---|
|`findNotes(filter)`|`filter: string`|Searches notes whose content contains the filter text|Array of matching notes|
|`removeNote(id)`|`id: number`|Deletes a note by ID|ID of removed note or `undefined`|
|`removeAllNotes()`|none|Clears all notes|Promise from `saveDB`|

---

# 6. Additional Notes

## String Search Limitations

`includes()` performs exact substring matching. It does **not** support:

- stemming
    
- fuzzy search
    
- multi-word tokenization
    
- partial word match beyond substring
    

For production systems, dedicated search engines or database text-search operators are used.

## IDs and UI Behavior

Even though the user may not know the note ID, the UI component (e.g., a delete button) would hold the ID internally and pass it to the backend.

---

# Summary of Key Points

- `findNotes()` performs a simple, case-insensitive substring search using `.includes()`.
    
- `removeNote()` deletes a note immutably by filtering out the matching ID.
    
- `removeAllNotes()` resets the notes database in a single operation.
    
- Filtering and searching are based on loading all notes and manipulating them in memory.
    
- Immutable patterns help avoid side effects and make logic easier to maintain.
    

---

## MicroTest