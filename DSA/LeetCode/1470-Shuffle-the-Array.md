
# 1470. Shuffle the Array

## Problem Overview

[!challenge]
You are given an array `nums` of `2n` elements structured as:

```

[x1, x2, ..., xn, y1, y2, ..., yn]

```

Your task is to return a new array arranged as:

```

[x1, y1, x2, y2, ..., xn, yn]

```

---

## Examples

[!example]
**Example 1**
```

Input: nums = [2,5,1,3,4,7], n = 3  
Output: [2,3,5,4,1,7]

```

[!example]
**Example 2**
```

Input: nums = [1,2,3,4,4,3,2,1], n = 4  
Output: [1,4,2,3,3,2,4,1]

```

[!example]
**Example 3**
```

Input: nums = [1,1,2,2], n = 2  
Output: [1,2,1,2]

````

---

## Key Insight

[!info]
The array is split into **two equal halves**:
- First half: `x1 ... xn`
- Second half: `y1 ... yn`

We interleave elements from both halves by alternating between them.

---

## Approach

### Simple Iteration with Extra Array

[!tip]
Since the problem does **not** require in-place modification, we can safely use an extra array for clarity and simplicity.

---

## JavaScript Solution

```js
function shuffle(nums, n) {
  const result = [];

  for (let i = 0; i < n; i++) {
    result.push(nums[i]);
    result.push(nums[i + n]);
  }

  return result;
}
````

---

## Step-by-Step Explanation

[!example]  
Input:

```
nums = [2,5,1,3,4,7]
n = 3
```

### Breakdown

- First half: `[2,5,1]`
    
- Second half: `[3,4,7]`
    

### Iteration

|i|nums[i]|nums[i+n]|result|
|---|---|---|---|
|0|2|3|[2,3]|
|1|5|4|[2,3,5,4]|
|2|1|7|[2,3,5,4,1,7]|

---

## Why This Works

[!success]

- Each iteration picks one element from each half
    
- Order is preserved
    
- Exactly `2n` insertions are made
    

---

## Time and Space Complexity

|Metric|Complexity|
|---|---|
|Time|**O(n)**|
|Space|**O(n)**|

[!note]  
Space is linear because a new array is created.

---

## Common Mistakes

[!warning]

- Incorrect indexing for the second half (`i + n`)
    
- Assuming the array is already interleaved
    
- Overcomplicating the solution with unnecessary data structures
    

---

## Interview Explanation

> The array consists of two halves of equal size.  
> I iterate from `0` to `n - 1` and, at each step, take one element from the first half and one from the second half.  
> By pushing them alternately into a new array, I achieve the required interleaving in linear time.

---

## Key Takeaways

|Concept|Insight|
|---|---|
|Array structure|Two equal halves|
|Technique|Simple indexed iteration|
|Performance|Linear time|
|Tradeoff|Extra space for clarity|
