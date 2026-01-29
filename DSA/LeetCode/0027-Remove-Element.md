

# Remove Element (In-Place)

## Problem Overview

[!challenge]
Given an integer array `nums` and an integer `val`, remove **all occurrences of `val` in-place**.  
The order of elements **may be changed**.  
Return the number of elements `k` that are **not equal to `val`**.

Requirements:
- Modify `nums` so the **first `k` elements** contain values not equal to `val`
- Elements beyond index `k - 1` are irrelevant
- Do not use extra arrays

---

## Input / Output Examples

[!example]
**Example 1**
```

Input: nums = [3,2,2,3], val = 3  
Output: k = 2  
nums = [2,2,_,_]

```

[!example]
**Example 2**
```

Input: nums = [0,1,2,2,3,0,4,2], val = 2  
Output: k = 5  
nums = [0,1,4,0,3,_,_,_]

````

---

## Key Observations

[!info]
- The order of elements does **not** matter
- We only care about the first `k` valid elements
- This allows us to overwrite unwanted values efficiently

[!tip]
Because order does not matter, we can compact valid values toward the front using a single pass.

---

## Strategy: Slow Pointer Overwrite

### Idea
- Use one pointer (`k`) to track where the next valid element should go
- Scan the array and copy only elements that are **not equal to `val`**

---

## JavaScript Solution (In-Place)

```js
function removeElement(nums, val) {
  let k = 0;

  for(let idx = 0; idx<nums.length; idx++){

        if(nums[idx]!== val){

            nums[k]=nums[idx]

            k++;

        }

    }

  return k;
}
````

---

## Step-by-Step Walkthrough

[!example]  
Input:

```
nums = [0,1,2,2,3,0,4,2], val = 2
```

### Execution Trace

| Idx | nums[idx] | Action | nums (partial) | k   |
| --- | --------- | ------ | -------------- | --- |
| 0   | 0         | keep   | [0]            | 1   |
| 1   | 1         | keep   | [0,1]          | 2   |
| 2   | 2         | skip   | [0,1]          | 2   |
| 3   | 2         | skip   | [0,1]          | 2   |
| 4   | 3         | keep   | [0,1,3]        | 3   |
| 5   | 0         | keep   | [0,1,3,0]      | 4   |
| 6   | 4         | keep   | [0,1,3,0,4]    | 5   |
| 7   | 2         | skip   | unchanged      | 5   |

Final result:

```
k = 5
nums = [0,1,3,0,4,_,_,_]
```

---

## Why This Works

[!success]

- All valid elements are copied forward exactly once
    
- No extra memory is used
    
- The array is modified in-place as required
    

---

## Time and Space Complexity

|Metric|Complexity|
|---|---|
|Time|**O(n)**|
|Space|**O(1)**|

[!note]  
Even though elements are overwritten, the array size remains unchanged.

---

## Common Mistakes

[!warning]

- Attempting to remove elements using `splice`
    
- Using additional arrays
    
- Forgetting that order does not matter
    

---

## Interview Explanation (How to Explain It)

> I iterate through the array once and keep a pointer that tracks where the next valid element should be written.  
> Whenever I find a value that is not equal to `val`, I copy it to the front of the array and move the pointer forward.  
> This ensures all valid elements end up in the first `k` positions, uses constant space, and runs in linear time.

---

## Key Takeaways

|Concept|Insight|
|---|---|
|In-place modification|No extra memory needed|
|Order not required|Enables simple overwrite strategy|
|Single pass|Efficient O(n) solution|
|Return value|`k = count of elements ≠ val`|