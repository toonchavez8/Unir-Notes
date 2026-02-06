# 20. Valid Parentheses (Easy)

## 🧩 Problem Description

You are given a string `s` that contains only these characters:

- `(` `)`
- `{` `}`
- `[` `]`

Your task is to determine whether the string is **valid**.

A string is considered **valid** if:

1. Every opening bracket has a **matching closing bracket**
2. Brackets are closed in the **correct order**
3. Closing brackets must match the **same type** of opening bracket

---

## 📥 Examples

### Example 1
**Input**
```text
"()"
```
**Output**
```text
true
```

---

### Example 2
**Input**
```text
"()[]{}"
```
**Output**
```text
true
```

---

### Example 3
**Input**
```text
"(]"
```
**Output**
```text
false
```

---

### Example 4
**Input**
```text
"([])"
```
**Output**
```text
true
```

---

### Example 5
**Input**
```text
"([)]"
```
**Output**
```text
false
```

---

## 💡 Key Idea (Simple Explanation)

This problem is best solved using a **stack**.

Why?

- Opening brackets need to be closed **later**
- The **last opened bracket must be closed first**
- This behavior matches **Last In, First Out (LIFO)** → exactly how a stack works

> [!note]
> If a problem involves checking order or matching pairs from the most recent element, think **stack**.

---

## 🛠️ Solution (JavaScript)

```js
var isValid = function (s) {
  const stack = [];
  const map = {
    ')': '(',
    '}': '{',
    ']': '[',
  };

  for (const char of s) {
    if (char === '(' || char === '{' || char === '[') {
      stack.push(char);
    } else {
      if (stack.pop() !== map[char]) {
        return false;
      }
    }
  }

  return stack.length === 0;
};
```

---

## 🧠 Step-by-Step Logic

1. Create an empty stack
2. Loop through each character in the string:
   - If it is an **opening bracket**, push it onto the stack
   - If it is a **closing bracket**:
     - Pop the top of the stack
     - Check if it matches the correct opening bracket
     - If it doesn’t match, return `false`
3. After processing all characters:
   - If the stack is empty → valid
   - If not → invalid

---

## 🧪 Example Walkthrough

Input:
```text
"([])"
```

Stack state:
```
[ "(" ]
[ "(", "[" ]
[ "(" ]     -> "]" matches "["
[ ]         -> ")" matches "("
```

Stack is empty → `true`

---

## ⏱️ Complexity Analysis

| Metric | Complexity |
|------|-----------|
| Time | **O(n)** — each character is processed once |
| Space | **O(n)** — stack may store all opening brackets |

---

## 📋 Summary / Takeaways

| Concept | Notes |
|------|------|
| Data Structure | Stack |
| Pattern | Matching pairs |
| Key Rule | Last opened must close first |
| Common Mistake | Ignoring order |
| Difficulty | Beginner-friendly |

---

## 🎤 How to Explain This in an Interview

> "I use a stack to track opening brackets as I iterate through the string.  
> When I encounter a closing bracket, I pop from the stack and check if it matches the expected opening bracket.  
> If at any point it doesn’t match, the string is invalid.  
> After processing the entire string, the stack must be empty for the string to be valid.  
> This approach runs in linear time and uses linear space."

---

## ✅ Final Notes

This is a **classic stack problem** and shows up often in interviews.

If you understand this one well, you’re ready for:
- Min Stack
- Daily Temperatures
- Evaluate Reverse Polish Notation

Strong fundamentals start here.
