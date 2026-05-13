# 1342. Number of Steps to Reduce a Number to Zero

## 🧠 Overview

This problem evaluates your understanding of loops, conditionals, and basic number operations. It also introduces an important concept in algorithmic thinking: repeatedly reducing a value until a termination condition is met.

---

> [!challenge]
> **Problem Statement**  
> Given a non-negative integer `num`, return the **number of steps** required to reduce it to `0`.
> 
> In one step:
> - If the current number is **even**, divide it by `2`
> - If the current number is **odd**, subtract `1`

---

## 📥 Inputs & 📤 Outputs

> [!example]
> **Example 1**
> ```text
> Input:  num = 14
> Output: 6
> ```

> [!example]
> **Example 2**
> ```text
> Input:  num = 8
> Output: 4
> ```

> [!example]
> **Example 3**
> ```text
> Input:  num = 123
> Output: 12
> ```

---

## ⚙️ Constraints

> [!info]
> - `0 <= num <= 10⁶`
> - Input is a single integer
> - The process must stop when `num === 0`

---

## ✅ Solution (JavaScript)

> [!example]
> 
> ```js
> /**
>  * @param {number} num
>  * @return {number}
>  */
> var numberOfSteps = function (num) {
>   let steps = 0;
> 
>   while (num !== 0) {
>     if (num % 2 === 0) {
>       num = num / 2;
>     } else {
>       num = num - 1;
>     }
>     steps++;
>   }
> 
>   return steps;
> };
> ```

---

## 🔍 Step-by-Step Logic

> [!note]
> 1. Initialize a counter to track the number of steps.
> 2. Loop until `num` becomes `0`.
> 3. On each iteration:
>    - If `num` is even, divide it by `2`.
>    - If `num` is odd, subtract `1`.
> 4. Increment the step counter after each operation.
> 5. Return the total number of steps once `num` reaches `0`.

---

## ⚠️ Common Pitfall

> [!warning]
> Forgetting to handle the case where `num` is already `0`.  
> In that case, the loop should never run and the result should be `0`.

---

## ⏱️ Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | **O(log n)** |
| Space Complexity | **O(1)** |

> [!tip]
> The number is roughly halved on each division, leading to logarithmic time complexity.

---

## 🧾 Summary / Takeaways

> [!success]
> - Use a loop to repeatedly apply transformation rules
> - Modulo (`%`) is used to check parity
> - Counters are useful for tracking operations
> - Efficient due to constant extra space usage

---

## 🔁 Alternative Approach (Bitwise Insight)

> [!info]
> This problem can also be viewed in terms of binary representation:
> - Each `1` bit requires one subtraction
> - Each bit (except the most significant) requires one division

> [!example]
> 
> ```js
> var numberOfSteps = function (num) {
>   let steps = 0;
> 
>   while (num > 0) {
>     steps += (num & 1) === 1 ? 2 : 1;
>     num >>= 1;
>   }
> 
>   return steps === 0 ? 0 : steps - 1;
> };
> ```

> [!warning]
> This approach is less intuitive and **not recommended** for interviews unless explicitly asked.

---

## 🏁 Final Notes

> [!success]
> This is a common interview warm-up problem that tests:
> - Loop control
> - Conditionals
> - Problem decomposition
> 
> A clean iterative solution is always preferred.
