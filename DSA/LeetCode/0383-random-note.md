# 383. Ransom Note

## Problem Overview

> **Difficulty:** Easy  
> **Topic:** Hash Table / String  
> **Language:** JavaScript  

---

> [!challenge]
> Given two strings `ransomNote` and `magazine`, determine if `ransomNote` can be constructed using the letters from `magazine`.
> 
> **Rules:**
> - Each letter in `magazine` can only be used **once**
> - Both strings contain only lowercase English letters

---

## Examples

> [!example]
> **Example 1**  
> Input: `ransomNote = "a"`, `magazine = "b"`  
> Output: `false`

> [!example]
> **Example 2**  
> Input: `ransomNote = "aa"`, `magazine = "ab"`  
> Output: `false`

> [!example]
> **Example 3**  
> Input: `ransomNote = "aa"`, `magazine = "aab"`  
> Output: `true`

---

## Approach

> [!info]
> The key idea is to **count how many times each character appears** in `magazine`, then verify that `ransomNote` does not request any character more times than available.

We use a **frequency map** (hash table) to track character counts.

---

## JavaScript Solution

```js
var canConstruct = function (ransomNote, magazine) {
    const count = {};

    // Count characters in magazine
    for (const char of magazine) {
        count[char] = (count[char] || 0) + 1;
    }

    // Use characters for ransomNote
    for (const char of ransomNote) {
        if (!count[char]) {
            return false;
        }
        count[char]--;
    }

    return true;
};
```

---

## Step-by-Step Logic

> [!note]
> This solution works in two linear passes.

1. Create an empty object to store character frequencies.
2. Iterate over `magazine`:
   - Increment the count for each character.
3. Iterate over `ransomNote`:
   - If the character is missing or count is `0`, return `false`.
   - Otherwise, decrement the count.
4. If all characters are successfully matched, return `true`.

---

## Complexity Analysis

> [!tip]
> Both strings are processed only once.

| Metric | Complexity |
|------|------------|
| Time | **O(n + m)** |
| Space | **O(1)** (fixed alphabet of 26 letters) |

---

## Edge Cases

> [!warning]
> - `ransomNote` longer than `magazine` → immediately impossible  
> - Repeated characters in `ransomNote`  
> - Exact matches vs missing characters  

---

## Interview Explanation (How to Say It)

> [!success]
> “I solve this by counting how many times each letter appears in the magazine using a hash map. Then I iterate through the ransom note and check if each required letter exists in the map with a positive count. If it does, I decrement the count. If not, I return false. If all letters are accounted for, I return true. This runs in linear time and constant space since there are only 26 lowercase letters.”

---

## Summary / Takeaways

| Concept | Notes |
|------|------|
| Data Structure | Hash Map (Frequency Counter) |
| Pattern | Counting / Greedy |
| Key Insight | Each letter can only be used once |
| Optimization | Constant space due to fixed alphabet |
| Interview Ready | Yes |

---


## Line-by-Line Explanation: `canConstruct`

> [!challenge]
> Explain **step by step and line by line** how the following JavaScript function determines whether a ransom note can be constructed from a magazine.

---

## The Code

```js
var canConstruct = function(ransomNote, magazine) {
    const count = {}
    for(const char of magazine){
        count[char]=(count[char]||0)+1
    }

    for(const char of ransomNote){
        if(!count[char]){
            return false
        }
        count[char]--;
    }
    return true
};
```

---

## Step-by-Step Breakdown

### 1. Function Definition

```js
var canConstruct = function(ransomNote, magazine) {
```

> [!info]
> Defines a function named `canConstruct` that takes two strings:
> - `ransomNote`: the string we want to build
> - `magazine`: the string that provides available characters

---

### 2. Create a Frequency Map

```js
const count = {}
```

> [!note]
> This object will store how many times each character appears in `magazine`.
>
> Example:
> ```js
> magazine = "aab"
> count = { a: 2, b: 1 }
> ```

---

### 3. Count Characters in `magazine`

```js
for (const char of magazine) {
    count[char] = (count[char] || 0) + 1
}
```

> [!info]
> This loop iterates over **each character** in `magazine`.

Line-by-line inside the loop:
- `count[char]` → looks up how many times `char` has appeared so far
- `(count[char] || 0)` → if it doesn’t exist yet, default to `0`
- `+ 1` → increment the count

> [!example]
> For `magazine = "aab"`:
>
> | Iteration | char | count |
> |---------|------|-------|
> | 1 | `'a'` | `{ a: 1 }` |
> | 2 | `'a'` | `{ a: 2 }` |
> | 3 | `'b'` | `{ a: 2, b: 1 }` |

---

### 4. Iterate Through `ransomNote`

```js
for (const char of ransomNote) {
```

> [!info]
> This loop checks whether each character needed by `ransomNote` is available in `count`.

---

### 5. Check Character Availability

```js
if (!count[char]) {
    return false
}
```

> [!warning]
> This condition handles **two cases**:
> - The character does not exist in `magazine`
> - The character exists but has already been fully used

If either is true, constructing the ransom note is impossible, so we return `false` immediately.

---

### 6. Consume One Character

```js
count[char]--;
```

> [!note]
> Since the character is available, we "use it up" by decrementing its count.
>
> This ensures **each letter can only be used once**, as required by the problem.

---

### 7. Successful Completion

```js
return true
```

> [!success]
> If the loop finishes without returning `false`, it means:
> - Every character in `ransomNote` was found
> - No character was used more times than available
>
> Therefore, the ransom note **can** be constructed.

---

## Why This Works

| Principle | Explanation |
|--------|-------------|
| Greedy | Consume characters as needed |
| Hash Map | Enables constant-time lookup |
| Early Exit | Stops as soon as construction is impossible |
| Correctness | Respects one-time character usage |

---

## Time & Space Complexity

> [!tip]
> The alphabet is fixed to lowercase English letters.

| Metric | Complexity |
|------|------------|
| Time | `O(n + m)` |
| Space | `O(1)` |

Where:
- `n` = length of `magazine`
- `m` = length of `ransomNote`

---

## Interview Explanation (What to Say)

> [!success]
> “I first count how many times each character appears in the magazine using an object. Then I iterate over the ransom note and check if each character is available. If a character is missing or already used up, I return false. Otherwise, I decrement the count to represent using that character. If all characters are processed successfully, I return true.”

---

## Key Takeaways

- Frequency maps are ideal for character-count problems
- Early returns improve efficiency
- This solution is linear, clean, and interview-friendly
- Works because the alphabet size is fixed

---
