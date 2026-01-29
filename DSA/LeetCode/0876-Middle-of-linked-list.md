# 876. Middle of the Linked List

## 🧠 Overview

This problem tests understanding of **linked lists** and pointer traversal. The optimal solution uses the **two-pointer (fast & slow)** technique to find the middle in a single pass.

---

> [!challenge]
> **Problem Statement**  
> Given the `head` of a singly linked list, return the **middle node** of the linked list.
> 
> - If there are **two middle nodes**, return the **second** middle node.
> - Return the node itself (i.e., the list starting from the middle).

---

## 📥 Inputs & 📤 Outputs

> [!example]
> **Example 1**
> ```text
> Input:  head = [1,2,3,4,5]
> Output: [3,4,5]
> ```
> **Explanation:** The middle node is `3`.

> [!example]
> **Example 2**
> ```text
> Input:  head = [1,2,3,4,5,6]
> Output: [4,5,6]
> ```
> **Explanation:** There are two middle nodes (`3` and `4`), so return the **second** one.

---

## ⚙️ Constraints

> [!info]
> - Number of nodes: `1` to `100`
> - `1 <= Node.val <= 100`
> - Singly linked list

---

## 🧩 Key Insight: Fast & Slow Pointers

> [!note]
> - Use **two pointers**:
>   - `slow` moves **1 step** at a time
>   - `fast` moves **2 steps** at a time
> - When `fast` reaches the end, `slow` will be at the middle
> - For even-length lists, this naturally lands on the **second middle**

---

## ✅ Solution (JavaScript)

> [!example]
> 
> ```js
> /**
>  * Definition for singly-linked list.
>  * function ListNode(val, next) {
>  *     this.val = (val===undefined ? 0 : val)
>  *     this.next = (next===undefined ? null : next)
>  * }
>  */
> 
> /**
>  * @param {ListNode} head
>  * @return {ListNode}
>  */
> var middleNode = function (head) {
>   let slow = head;
>   let fast = head;
> 
>   while (fast !== null && fast.next !== null) {
>     slow = slow.next;
>     fast = fast.next.next;
>   }
> 
>   return slow;
> };
> ```

---

## 🔍 Step-by-Step Logic

> [!note]
> 1. Initialize two pointers (`slow` and `fast`) at the head.
> 2. Move `slow` by 1 node and `fast` by 2 nodes per iteration.
> 3. Continue while `fast` and `fast.next` are not `null`.
> 4. When the loop ends, `slow` points to the middle node.
> 5. Return `slow`.

---

## ⚠️ Common Pitfalls

> [!warning]
> - Forgetting to check `fast.next !== null` can cause runtime errors.
> - Using a counter-based approach requires **two passes**, which is less optimal.

---

## ⏱️ Complexity Analysis

| Metric | Value |
|------|------|
| Time Complexity | **O(n)** |
| Space Complexity | **O(1)** |

> [!tip]
> This solution is optimal because it finds the middle in **one traversal** using constant extra space.

---

## 🧾 Summary / Takeaways

> [!success]
> - Fast & slow pointers are ideal for linked list midpoint problems
> - Automatically handles even-length lists by returning the second middle
> - One-pass, constant-space solution
> - Common interview pattern for linked lists

---

## 🔁 Alternative Approach (Two Passes)

> [!info]
> 1. Count the total number of nodes
> 2. Traverse again to `n / 2`
> 
> ❌ Less efficient and not preferred in interviews

---

## 🧠 Pattern Recognition

| Problem Type | Technique |
|-------------|----------|
| Middle of list | Fast & Slow pointers |
| Cycle detection | Fast & Slow pointers |
| Kth from end | Two pointers |

> [!success]
> Mastering this pattern unlocks many linked list problems.

## 1. Where Does `.next` come From?

`.next` comes from the **definition of a singly linked list node**.

This part at the top is crucial:

```js
function ListNode(val, next) {
  this.val = (val === undefined ? 0 : val)
  this.next = (next === undefined ? null : next)
}
```

Each node has **two properties**:

- `val` → the value stored in the node
    
- `next` → a reference (pointer) to the **next node in the list**

### Visual Example

For this list:

```Python
1 → 2 → 3 → 4 → 5 → null
```

In memory, it looks like:

```js
{
  val: 1,
  next: {
    val: 2,
    next: {
      val: 3,
      next: {
        val: 4,
        next: {
          val: 5,
          next: null
        }
      }
    }
  }
}
```

So when you write:

```js
slow = slow.next;
```

You are literally saying:

> “Move to the next node in the list.”

---

## 2. Why Are They Called `slow` and `fast`?

Because **they move at different speeds**.

```js
let slow = head;
let fast = head;
```

Both start at the **same node** (`head`).

### Movement Rules

Inside the loop:

```js
slow = slow.next;       // moves 1 step
fast = fast.next.next; // moves 2 steps
```

So:

- `slow` moves **one node at a time**
    
- `fast` moves **two nodes at a time**

That’s why:

- one is called **slow**
    
- the other is called **fast**

The names describe **behavior**, not data type.

---

## 3. Why Does This Find the Middle?

This is the key insight.

### Let’s Walk through an Example

List:

```Python
1 → 2 → 3 → 4 → 5 → null
```

|Iteration|slow|fast|
|---|---|---|
|start|1|1|
|1|2|3|
|2|3|5|
|stop|3|null|

When `fast` reaches the **end**, `slow` is at the **middle**.

Why?

Because:

- `fast` moves **twice as fast**
    
- So when `fast` finishes the list,
    
- `slow` has only gone **halfway**

---

## 4. Why Does This return the _second_ Middle in even Lists?

Example:

```Python
1 → 2 → 3 → 4 → 5 → 6 → null
```

|Iteration|slow|fast|
|---|---|---|
|start|1|1|
|1|2|3|
|2|3|5|
|3|4|null|

Now the two middle nodes are `3` and `4`.

The algorithm **lands on `4`**, the second middle.

That happens naturally because:

- `slow` moves **after** `fast` jumps
    
- The loop stops only when `fast` can’t move two steps

No extra logic needed — very elegant.

---

## 5. Why Do We Check `fast !== null && fast.next !== null`?

This prevents **runtime errors**.

```js
while (fast !== null && fast.next !== null) {
```

Because later we do:

```js
fast = fast.next.next;
```

If `fast.next` were `null`, then:

```js
fast.next.next ❌
```

would crash.

So the condition ensures:

- `fast` exists
    
- `fast.next` exists
    
- Therefore `fast.next.next` is safe

---

## 6. Why return `slow`?

Because by the time the loop ends:

```js
return slow;
```

`slow` is pointing to:

- the **middle node**
    
- or the **second middle node** (if even length)

And the problem wants:

> “Return the middle node of the linked list”

Not the value — the **node itself**.

---

## 7. How to Explain This in an Interview (perfect answer)

If an interviewer asks you to explain this, say something like:

> “I use two pointers: one moves one step at a time and the other moves two steps at a time. When the faster pointer reaches the end of the list, the slower pointer will be at the middle. This works in one pass and uses constant space, and for even-length lists it naturally returns the second middle node.”

That answer is **exactly what they want to hear**.

---

## 8. Final Takeaway

- `.next` comes from the linked list node structure
    
- `slow` and `fast` describe **movement speed**
    
- This is a **two-pointer pattern**
    
- It’s optimal: **O(n) time, O(1) space**
    
- Very common in interviews (IBM included)

