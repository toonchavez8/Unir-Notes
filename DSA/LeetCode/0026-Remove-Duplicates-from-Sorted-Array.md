# Remove Duplicates from Sorted Array (In-Place)

## Problem Overview

[!challenge]

Given a **sorted integer array `nums`**, remove the duplicates **in-place** such that each unique element appears only once.  
Return the number of unique elements `k`.

- The **first `k` elements** of `nums` must contain the unique values in **sorted order**
- Elements beyond index `k - 1` are irrelevant
- You **must not** use extra space for another array

---

## Input / Output Examples

[!example]

**Example 1**

```Python

Input: nums = [1,1,2]  
Output: k = 2  
nums = [1,2,_]

```

[!example]

**Example 2**

```Python

Input: nums = [0,0,1,1,1,2,2,3,3,4]  
Output: k = 5  
nums = [0,1,2,3,4,_,_,_,_,_]

````

---

## Key Observations

> [!info]
> - The array is already **sorted**
> - All duplicates will be **adjacent**
> - This allows us to compare each element with the previous unique element

Because the array is sorted, we only need **one pass** using a **two-pointer technique**

---

## Strategy: Two Pointers

### Pointer Roles

| Pointer | Purpose |
|------|--------|
| `i` | Tracks the index of the last unique element |
| `j` | Scans the array for new unique values |

---

## JavaScript Solution (In-Place)

```js
function removeDuplicates(nums) {
    if (nums.length===0)return 0
    
    let uniqueVal = 0

    for(let index =1; index <nums.length; index++){

        if(nums[index]!==nums[uniqueVal]){
            uniqueVal++;
            nums[uniqueVal]=nums[index]
        }
    }
    return uniqueVal+1
}
````

---

## Step-by-Step Walkthrough

[!example]  
Input:

```Python
nums = [0,0,1,1,1,2,2,3,3,4]
```

### Execution Trace

|j|nums[j]|nums[i]|Action|
|---|---|---|---|
|1|0|0|duplicate → skip|
|2|1|0|new value → i++, copy|
|3|1|1|duplicate|
|5|2|1|new value → i++, copy|
|7|3|2|new value → i++, copy|
|9|4|3|new value → i++, copy|

Final array state:

```Python
[0,1,2,3,4,_,_,_,_,_]
```

Returned value:

```Python
k = 5
```

---

## Why This Works

[!success]

- Each unique element is written **once**
    
- All writes happen **in-place**
    
- The relative order is preserved
    
- No extra memory is used

---

## Time and Space Complexity

|Metric|Complexity|
|---|---|
|Time|**O(n)**|
|Space|**O(1)**|

[!note]  
Even though values are overwritten, the array size remains unchanged.

---

## Common Mistakes

[!warning]

- Using extra arrays (violates in-place requirement)
    
- Forgetting to return `i + 1`
    
- Not handling arrays of length 1

---

## Interview Explanation (How to Say It)

> Since the array is sorted, duplicates are always adjacent.  
> I use a two-pointer approach where one pointer tracks the position of the last unique element, and the other scans the array.  
> When I find a new value, I move the unique pointer forward and overwrite that position with the new value.  
> This keeps all unique elements at the front of the array in sorted order, uses constant space, and runs in linear time.

---

## Key Takeaways

|Concept|Insight|
|---|---|
|Sorted input|Enables linear scan|
|Two pointers|Efficient in-place updates|
|In-place constraint|No extra memory|
|Return value|`k = number of unique elements`|

---