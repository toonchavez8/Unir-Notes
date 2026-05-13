
# 1929-Concatenation-of-Array

## Problem Overview

[!challenge]
You are given an integer array `nums` of length `n`.

Your goal is to create a new array `ans` of length `2n` such that:
- The **first half** of `ans` is exactly `nums`
- The **second half** of `ans` is also exactly `nums`

In simple terms:  
**Repeat the array once and place it after itself.**

---

## Examples

[!example]
**Example 1**
```

Input: nums = [1,2,1]  
Output: [1,2,1,1,2,1]

```

[!example]
**Example 2**
```

Input: nums = [1,3,2,1]  
Output: [1,3,2,1,1,3,2,1]

```

---

## Key Insight (Junior-Friendly)

[!info]
The problem is not asking for any transformation or sorting.  
It simply wants:
```

nums + nums

````

If you understand how to loop through an array and push values into another array, you already know how to solve this.

---

## Approach

### Simple Loop and Push

[!tip]
We iterate through `nums` **twice** and push each value into a new array.

This keeps the solution easy to read and understand.

---

## JavaScript Solution

```js
function getConcatenation(nums) {
  const ans = [];

  for (let i = 0; i < nums.length; i++) {
    ans.push(nums[i]);
  }

  for (let i = 0; i < nums.length; i++) {
    ans.push(nums[i]);
  }

  return ans;
}
```

```js
var getConcatenation = function(nums) {

    const result = []

    let loop = 0

    while(loop<2){

        for(let index = 0; index<nums.length; index++){

        result.push(nums[index])

        }

        loop++;

    }

    return result

};
```

```js
var getConcatenation = function(nums) {

    return nums.concat(nums);

};
```

---

## Step-by-Step Explanation

[!example]  
Input:

```
nums = [1,2,1]
```

### First Loop

We copy `nums` into `ans`:

```
ans = [1,2,1]
```

### Second Loop

We copy `nums` again:

```
ans = [1,2,1,1,2,1]
```

### Final Output

```
[1,2,1,1,2,1]
```

---

## Why This Works

[!success]

- We copy every element **exactly twice**
    
- Order is preserved
    
- No complex logic required
    
- Very beginner-friendly
    

---

## Time and Space Complexity

|Metric|Complexity|
|---|---|
|Time|**O(n)**|
|Space|**O(n)**|

[!note]  
The output array must be size `2n`, so extra space is unavoidable.

---

## Common Mistakes

[!warning]

- Forgetting to return the new array
    
- Modifying the original array instead of creating a new one
    
- Overcomplicating a simple problem
    

---

## Interview Explanation (How to Say It)

> I create a new array and loop through the input array twice.  
> Each loop pushes all elements of `nums` into the result array.  
> This produces a concatenated array in linear time with clear logic.

---

## Key Takeaways

|Concept|Insight|
|---|---|
|Array concatenation|Just repeat the array|
|Loops|Simple iteration is enough|
|Space tradeoff|Required for output|
|Difficulty|Logic > tricks|

```
::contentReference[oaicite:0]{index=0}
```