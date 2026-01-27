# 03 — Static Arrays

## What is an Array?

> **Array**: A data structure that stores elements of the same type in a **contiguous block of memory (RAM)**.

**Key implication:**

- Elements are stored next to each other in memory.
    
- This enables fast, predictable access.
    

---

## Reading from an Array

### Zero-based Indexing

- First element → index `0`
    
- Second element → index `1`
    
- Third element → index `2`
    

```text
Index:   0   1   2
Array:  [5,  6,  7]
```

### Why Reading Is Fast

- Each index maps directly to a memory address.
    
- No traversal is required.
    

> **Time Complexity:** `O(1)` (constant time)

> **Why?** Because RAM is _Random Access Memory_ — any address can be accessed instantly.

---

## Iterating Through an Array

To read all values:

1. Start at index `0`
    
2. Increment the index by `1`
    
3. Stop at `array.length`
    

```js
for (let i = 0; i < array.length; i++) {
  console.log(array[i])
}
```

> **Time Complexity:** `O(n)` — every element is visited once.

---

## Writing to an Array

### Overwriting an Element

- Writing to a known index is direct.
    
- No other elements are affected.
    

> **Time Complexity:** `O(1)`

---

## Static Arrays (Fixed Size)

> **Static arrays have a fixed size at allocation time.**

### Why Size Cannot Change

- Memory must remain contiguous.
    
- Adjacent memory may already be in use by:
    
    - Other arrays
        
    - The operating system
        

⚠️ You **cannot safely append** beyond allocated space.

---

## Adding Elements at the End

If there is unused space:

- The index of the next free slot is known.
    
- Value is written directly.
    

> **Time Complexity:** `O(1)`

---

## Removing Elements (Logical Removal)

- Memory is **not deallocated**.
    
- The value is overwritten (e.g. `0`, `null`, `-1`).
    

```text
Before: [5, 6, 7]
After:  [5, 6, 0]
```

> **Time Complexity:** `O(1)`

---

## Order Matters in Arrays

Arrays preserve **order**.

```text
[5, 6]  ≠  [6, 5]
```

This makes insertion/removal in the middle expensive.

---

## Inserting in the Middle

### Example

Insert `4` at the beginning:

```text
Before: [5, 6]
After:  [4, 5, 6]
```

### Steps Required

1. Shift `6` → index `2`
    
2. Shift `5` → index `1`
    
3. Insert `4` → index `0`
    

⚠️ Shifting must occur **right to left** to avoid overwriting.

> **Worst-case Time Complexity:** `O(n)`

---

## Removing from the Middle

### Example

Remove `5`:

```text
Before: [5, 6, 7]
After:  [6, 7]
```

### Steps Required

1. Shift `6` → index `0`
    
2. Shift `7` → index `1`
    
3. Ignore or overwrite last value
    

> **Worst-case Time Complexity:** `O(n)`

---

## Why We Use Worst-Case (Big-O)

Big-O describes **maximum possible cost**, not best or average cases.

- Insert at end → `O(1)`
    
- Insert at beginning → `O(n)` ← **worst case**
    

We generalize to stay safe and consistent.

---

## Summary Table

|Operation|Time Complexity|
|---|---|
|Read element at index `i`|`O(1)`|
|Write element at index `i`|`O(1)`|
|Insert at end|`O(1)`|
|Remove at end|`O(1)`|
|Insert in middle|`O(n)`|
|Remove from middle|`O(n)`|

---

## Key Takeaways

- Arrays are contiguous in memory
    
- RAM enables constant-time access
    
- Static arrays cannot grow
    
- Order preservation causes shifting
    
- Middle insertions/removals are expensive
    

> 🔑 These concepts are **foundational** for understanding more advanced data structures like dynamic arrays, linked lists, and vectors.