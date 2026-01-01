# Two Sum – Brute Force Approach (Explanation)

## Problem Statement
Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers such that they add up to `target`.

You may assume that:
- Each input has exactly one solution
- You may not use the same element twice

---

## Approach Used
**Brute Force using Two Nested Loops**

The idea is to check **every unique pair of elements** in the array and see if their sum equals the target.

---

## Step-by-Step Logic

1. Use an outer loop to pick the **first element** (`i`)
2. Use an inner loop to pick the **second element** (`j`)
3. Start the inner loop from `i + 1` to:
   - Avoid using the same element twice
   - Avoid checking duplicate pairs
4. Check if:
   ```
   nums[i] + nums[j] == target
   ```
5. If true, return the indices `[i, j]`

---

## Code Implementation

```python
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

---

## Example Dry Run

### Input
```
nums = [3, 2, 3]
target = 6
```

### Iterations

| i | j | nums[i] | nums[j] | Sum |
|---|---|--------|--------|-----|
| 0 | 1 | 3 | 2 | 5 ❌ |
| 0 | 2 | 3 | 3 | 6 ✅ |

✅ Match found → return `[0, 2]`

---

## Common Mistake Fixed

### ❌ Incorrect Check (Earlier)
```python
nums[i] + nums[i+1]
```

- Only checks adjacent elements
- Misses valid non-adjacent pairs
- Fails cases like `[3,2,3]`

### ✅ Correct Check (Final)
```python
nums[i] + nums[j]
```

- Checks all unique pairs
- Uses the inner loop index properly
- Passes all test cases

---

## Time and Space Complexity

### Time Complexity
- Two nested loops → **O(n²)**

### Space Complexity
- No extra data structures used → **O(1)**

---

## When to Use This Approach
- Best for learning and understanding the problem
- Good when input size is small
- Serves as a foundation for the optimized HashMap solution

---

## Conclusion
This brute-force solution systematically checks all possible pairs to find the correct indices. While not the most optimized, it is simple, clear, and guaranteed to work for all valid inputs.

---

✨ Next step: Optimize this solution using a HashMap to achieve **O(n)** time complexity.
