# 412. Fizz Buzz

## 🧠 Overview

Fizz Buzz is a classic introductory problem used to evaluate basic control flow, conditionals, and iteration. Despite its simplicity, it tests attention to detail and correct condition ordering.

---

> [!challenge]
> **Problem Statement**  
> Given an integer `n`, return a **1-indexed** string array `answer` such that:
> 
> - `answer[i] == "FizzBuzz"` if `i` is divisible by **3 and 5**
> - `answer[i] == "Fizz"` if `i` is divisible by **3**
> - `answer[i] == "Buzz"` if `i` is divisible by **5**
> - `answer[i] == i` (as a string) otherwise

---

## 📥 Inputs & 📤 Outputs

> [!example]
> **Example 1**
> ```text
> Input:  n = 3
> Output: ["1","2","Fizz"]
> ```

> [!example]
> **Example 2**
> ```text
> Input:  n = 5
> Output: ["1","2","Fizz","4","Buzz"]
> ```

> [!example]
> **Example 3**
> ```text
> Input:  n = 15
> Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
> ```

---

## ⚙️ Constraints

> [!info]
> - `1 <= n <= 10⁴`
> - Output must be an array of **strings**
> - Indexing is **1-based**, not 0-based

---

## ✅ Primary Solution (JavaScript – Explicit Conditions)

> [!example]
> 
> ```js
> /**
>  * @param {number} n
>  * @return {string[]}
>  */
> var fizzBuzz = function (n) {
>   const result = [];
> 
>   for (let i = 1; i <= n; i++) {
>     if (i % 3 === 0 && i % 5 === 0) {
>       result.push("FizzBuzz");
>     } else if (i % 3 === 0) {
>       result.push("Fizz");
>     } else if (i % 5 === 0) {
>       result.push("Buzz");
>     } else {
>       result.push(i.toString());
>     }
>   }
> 
>   return result;
> };
> ```

---

## 🔍 Step-by-Step Logic

> [!note]
> 1. Initialize an empty array to store results.
> 2. Iterate from `1` to `n`.
> 3. Check divisibility:
>    - First: divisible by **both 3 and 5**
>    - Then: divisible by **3**
>    - Then: divisible by **5**
> 4. Convert numbers that match no rule to strings.
> 5. Append each result to the array.
> 6. Return the completed array.

---

## ⚠️ Common Pitfall

> [!warning]
> If you check divisibility by `3` or `5` **before** checking both,  
> `"FizzBuzz"` will never be produced.

---

## ⏱️ Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

> [!tip]
> Space complexity is linear because the output array grows with `n`.

---

## 🧾 Summary / Takeaways

> [!success]
> - Modulo (`%`) is used to test divisibility
> - Condition order is critical
> - Emphasizes loops, conditionals, and clean logic
> - Commonly used in interviews to assess fundamentals

---

## 🔁 Variations to Practice

- Return a single concatenated string
- Add a new rule (e.g., divisible by 7 → `"Pop"`)
- Implement using functional array methods

---

## 🧩 Pattern 1: String-Building (Less Branching)

Instead of explicitly checking all cases, build the output string dynamically.

> [!example]
> 
> ```js
> var fizzBuzz = function (n) {
>   const result = [];
> 
>   for (let i = 1; i <= n; i++) {
>     let output = "";
> 
>     if (i % 3 === 0) output += "Fizz";
>     if (i % 5 === 0) output += "Buzz";
> 
>     result.push(output || i.toString());
>   }
> 
>   return result;
> };
> ```

### Why This Can Be Better

- No special-case for `15`
- Reads like a set of rules
- Easy to extend with new conditions

> [!tip]
> Adding a new rule is trivial:
> ```js
> if (i % 7 === 0) output += "Pop";
> ```

### Trade-offs

- Slightly more abstract
- Less obvious to beginners
- Some interviewers prefer explicit conditionals

---

## 🧩 Pattern 2: Functional / Declarative Style

Uses modern JavaScript array utilities.

> [!example]
> 
> ```js
> var fizzBuzz = function (n) {
>   return Array.from({ length: n }, (_, i) => {
>     const num = i + 1;
> 
>     if (num % 15 === 0) return "FizzBuzz";
>     if (num % 3 === 0) return "Fizz";
>     if (num % 5 === 0) return "Buzz";
> 
>     return num.toString();
>   });
> };
> ```

### Why People Like This

- Concise and expressive
- No manual array mutation
- Clean once familiar with `Array.from`

### Trade-offs

- Harder to debug step-by-step
- Less beginner-friendly in interviews

---

## 🏁 Final Recommendation

> [!success]
> For interviews and coding assessments, the **explicit conditional solution** is the safest choice:
> - Clear intent
> - Easy to explain
> - Widely accepted by interviewers
