https://leetcode.com/problems/baseball-game/description/

# 682. Baseball Game (Easy)

## 🧩 Problem Description

You are keeping track of scores for a baseball game using **unusual rules**.

You start with an **empty record** (think of it like a list or stack).  
You are given an array of strings `operations`, where each operation modifies the record.

### Possible Operations

| Operation | Meaning |
|---------|--------|
| `"x"` (number) | Add score `x` to the record |
| `"+"` | Add a new score that is the **sum of the last two scores** |
| `"D"` | Add a new score that is **double the last score** |
| `"C"` | **Remove** the last score from the record |

After processing all operations, return the **sum of all scores** in the record.

> [!note]
> The problem guarantees that all operations are valid (no edge-case errors to handle).

---

## 📥 Examples

### Example 1

**Input**

```text
["5","2","C","D","+"]
```

**Explanation**

```Python
[5]        -> add 5
[5, 2]     -> add 2
[5]        -> remove last (C)
[5, 10]    -> double last (D)
[5, 10,15] -> sum last two (+)
```

**Output**

```text
30
```

---

### Example 2

**Input**

```text
["5","-2","4","C","D","9","+","+"]
```

**Output**

```text
27
```

---

### Example 3

**Input**

```text
["1","C"]
```

**Output**

```text
0
```

---

## 💡 Key Insight (Junior-Friendly)

This problem is **perfect for a stack (array)** because:

- You mostly care about the **most recent scores**
- Operations like `C`, `D`, and `+` depend on the **last one or two values**
- JavaScript arrays let us easily `push` and `pop`

> [!tip]
> If a problem frequently asks for "previous values", a **stack** is often the right tool.

---

## 🛠️ Solution (JavaScript)

```js
var calPoints = function (operations) {
  let record = [];

  for (const ops of operations) {
    switch (ops) {
      case "C":
        record.pop();
        break;

      case "D":
        record.push(record[record.length - 1] * 2);
        break;

      case "+":
        const last = record[record.length - 1];
        const secondLast = record[record.length - 2];
        record.push(last + secondLast);
        break;

      default:
        record.push(Number(ops));
    }
  }

  return record.reduce((sum, score) => sum + score, 0);
};

```

---

## 🧠 Step-by-Step Logic

1. Create an empty array `record` to store scores
2. Loop through each operation:
   - `"C"` → remove last score
   - `"D"` → double last score and add it
   - `"+"` → sum last two scores and add it
   - number → convert to `Number` and add it
3. After all operations, sum the values in `record`
4. Return the total

---

## ⏱️ Complexity Analysis

| Metric | Complexity |
|------|------------|
| Time | **O(n)** — one pass through operations |
| Space | **O(n)** — storing scores in a stack |

---

## 🧪 Why This Works Well

- Stack keeps history clean and ordered
- Operations are simple and direct
- Easy to reason about and debug
- Matches real-world “undo / last action” logic

---

## 📋 Summary / Takeaways

| Concept | Notes |
|------|------|
| Data Structure | Stack (Array) |
| Core Operations | `push`, `pop`, index access |
| Pattern | Last-in, first-out (LIFO) |
| Difficulty | Beginner-friendly |
| Interview Value | Tests stack fundamentals |

---

## 🎤 How to Explain This in an Interview

> "I use a stack to keep track of the scores because every operation depends on the most recent values.  
> As I loop through the operations, I handle each case directly — popping for 'C', doubling for 'D', summing the last two for '+', and pushing numbers otherwise.  
> Once all operations are processed, I sum the stack to get the final score.  
> This runs in linear time and uses linear space, which is optimal for this problem."

---

## ✅ Final Thought

If you understand this problem well, you’ve mastered:

- Stack basics
- Parsing input
- Translating rules into clean logic

Great foundation for harder stack problems 🚀
