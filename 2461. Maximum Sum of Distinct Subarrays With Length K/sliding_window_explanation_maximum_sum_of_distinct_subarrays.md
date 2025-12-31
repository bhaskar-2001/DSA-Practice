# Sliding Window Explanation – Maximum Sum of Distinct Subarrays (LeetCode 2461)

## Problem Summary
You are given:
- An integer array `nums`
- An integer `k`

Your task is to **find the maximum sum of any subarray of length `k`** such that:
- All elements in the subarray are **distinct**

If no such subarray exists, return `0`.

---

## Why Sliding Window?

Brute force approach:
- Generate all subarrays of length `k`
- Check if elements are distinct
- Compute sum

⛔ This is too slow: **O(n × k)**

✅ Sliding Window allows us to:
- Process each element **once**
- Maintain window state efficiently
- Achieve **O(n)** time complexity

---

## Key Idea (Mental Model)

Think of a **window** moving over the array:

- `left` → start of window
- `right` → end of window

We:
1. Expand window by moving `right`
2. Shrink window if size exceeds `k`
3. When window size is exactly `k`:
   - Check if all elements are distinct
   - Update maximum sum

---

## Variables Used

```python
freq = defaultdict(int)   # frequency of elements in window
left = 0                  # left pointer
current_sum = 0           # sum of elements in window
max_sum = 0               # answer
```

---

## Complete Code

```python
from typing import List
from collections import defaultdict

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        left = 0
        current_sum = 0
        max_sum = 0

        for right in range(len(nums)):
            # 1. Add right element to window
            freq[nums[right]] += 1
            current_sum += nums[right]

            # 2. Shrink window if size > k
            if right - left + 1 > k:
                freq[nums[left]] -= 1
                current_sum -= nums[left]
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            # 3. If window size == k and all elements are distinct
            if right - left + 1 == k and len(freq) == k:
                max_sum = max(max_sum, current_sum)

        return max_sum
```

---

## Step-by-Step Explanation

### 1️⃣ Expanding the Window (Move `right`)

```python
freq[nums[right]] += 1
current_sum += nums[right]
```
- Add the new element to the window
- Update frequency and sum

---

### 2️⃣ Shrinking the Window (If Size > k)

```python
if right - left + 1 > k:
```

This means the window is **too large** and must be fixed.

#### What happens during shrinking:

```python
freq[nums[left]] -= 1        # remove left element
current_sum -= nums[left]   # update sum

if freq[nums[left]] == 0:
    del freq[nums[left]]    # clean frequency map

left += 1                   # move left pointer
```

🧠 Why this is important:
- Window must always stay valid
- Sum and distinct count must match the window

---

### 3️⃣ Checking Valid Window

```python
if right - left + 1 == k and len(freq) == k:
```

This ensures:
- Window length is exactly `k`
- All elements are distinct (`len(freq) == k`)

If valid, update answer:

```python
max_sum = max(max_sum, current_sum)
```

---

## Dry Run Example

### Input
```
nums = [1,5,4,2,9,9,9]
k = 3
```

### Valid Windows

| Window | Distinct | Sum |
|------|----------|-----|
| [1,5,4] | ✅ | 10 |
| [5,4,2] | ✅ | 11 |
| [4,2,9] | ✅ | 15 |
| [2,9,9] | ❌ | - |
| [9,9,9] | ❌ | - |

✅ Answer = **15**

---

## Sliding Window Invariant (Very Important)

At every step:
- Window size ≤ `k`
- `current_sum` matches elements in window
- `freq` exactly represents window contents

---

## Time & Space Complexity

| Metric | Value |
|-----|-----|
| Time | **O(n)** |
| Space | **O(k)** |

---

## Key Takeaways

✔ Sliding window avoids recomputation
✔ Always **expand → fix → check**
✔ Frequency map helps detect duplicates
✔ This pattern applies to MANY problems

---

## Reusable Sliding Window Template

```python
for right in range(n):
    add(nums[right])

    if window_invalid:
        remove(nums[left])
        left += 1

    if window_valid:
        update_answer()
```

---

💡 Master this pattern and you will solve **70%+ array problems** easily.

