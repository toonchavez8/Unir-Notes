

# 🧩 Two Sum — Study Guide

> [!challenge] **Problem Statement**
Given an array of integers `nums` and an integer `target`, return **indices of the two numbers such that they add up to `target`**.

You may assume that each input has **exactly one solution**, and you may **not use the same element twice**.  
You can return the answer in any order.

---

## 🧠 Examples

> [!example] **Example 1**
**Input:**  
`nums = [2,7,11,15], target = 9`  
**Output:**  
`[0,1]`  
**Explanation:**  
Because `nums[0] + nums[1] == 9`, we return `[0, 1]`.

---

> [!example] **Example 2**
**Input:**  
`nums = [3,2,4], target = 6`  
**Output:**  
`[1,2]`

---

> [!example] **Example 3**
**Input:**  
`nums = [3,3], target = 6`  
**Output:**  
`[0,1]`

---

## ⚙️ Constraints

- `2 <= nums.length <= 10⁴`
- `-10⁹ <= nums[i] <= 10⁹`
- `-10⁹ <= target <= 10⁹`
- Only **one valid answer** exists.

---

## 🚀 Follow-up
> [!question]
Can you come up with an algorithm that runs in **less than O(n²)** time complexity?

---

## 💡 JavaScript Solution

```js
var twoSum = function (nums, target) {
    let numToIndex = {};
    for (let index = 0; index < nums.length; index++) {
        let complement = target - nums[index];
        if (numToIndex[complement] !== undefined) {
            return [numToIndex[complement], index];
        }
        numToIndex[nums[index]] = index;
    }
    return [];
};
````

---

## 🧩 Step-by-Step Explanation

> [!info] **1. Initialize a Map**  
> `let numToIndex = {}`  
> We use an object to store each number’s value as a key and its index as the value.

> [!info] **2. Loop through the array**  
> We iterate once through `nums` using `index`.

> [!info] **3. Compute the complement**  
> `let complement = target - nums[index]`  
> The complement is the number we need to reach the target sum.

> [!info] **4. Check if the complement exists**  
> If `numToIndex[complement] !== undefined`, that means we already stored a number that can pair with the current one.

> [!tip] **Return the indices**  
> If found, return both indices:

```js
return [numToIndex[complement], index];
```

> [!info] **5. Store the current number**  
> If no complement is found, store the current number and its index:

```js
numToIndex[nums[index]] = index;
```

> [!success] **6. Efficiency**

- **Time Complexity:** O(n)  
    Each lookup and insertion is constant time.
    
- **Space Complexity:** O(n)  
    We store up to all elements once.
    

---

## ⚡ TypeScript Version 1 — Direct Translation

```ts
function twoSum(nums: number[], target: number): number[] {
  const numToIndex: { [key: number]: number } = {};

  for (let index = 0; index < nums.length; index++) {
    const complement = target - nums[index];
    if (numToIndex[complement] !== undefined) {
      return [numToIndex[complement], index];
    }
    numToIndex[nums[index]] = index;
  }

  return [];
}
```

---

## 💎 TypeScript Version 2 — Using `Map` (Recommended)

```ts
function twoSum(nums: number[], target: number): number[] {
  const numToIndex = new Map<number, number>();

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i];
    if (numToIndex.has(complement)) {
      return [numToIndex.get(complement) as number, i];
    }
    numToIndex.set(nums[i], i);
  }

  return [];
}
```

> [!tip] **Why use `Map`?**

- Avoids issues with object key coercion (`"1"` vs `1`)
    
- More explicit API (`.has()` and `.get()`)
    
- Cleaner semantics for numeric keys
    

---

## 🧭 Summary

|Aspect|Description|
|:--|:--|
|**Approach**|Hash map lookup for complements|
|**Time Complexity**|O(n)|
|**Space Complexity**|O(n)|
|**Avoids duplicate use**|Yes — checks complement _before_ storing current number|
|**Best Practice**|Use `Map<number, number>` in TypeScript for clarity and type safety|

---

> [!quote]  
> _"Think in terms of complements — for each number, look for what’s missing to reach the target."_  
> – Your future self after mastering hash maps 🔥

