# LeetCode 1929 – Concatenation of Array

## Problem Overview

You are given an integer array `nums` of length `n`.

Your task is to create a new array `ans` of length `2n` such that:

* The **first `n` elements** of `ans` are exactly the elements of `nums`
* The **next `n` elements** of `ans` are again the elements of `nums`

In simple words, you need to **repeat the array twice**.

### Example

```
Input:  nums = [1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]
```

---

## LeetCode-Ready Code

```python
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * (2 * n)

        for i in range(2 * n):
            res[i] = nums[i % n]

        return res
```

---

## Step-by-Step Explanation

### 1. Class and Function Structure

LeetCode requires the solution to be written inside a class named `Solution`.

```python
class Solution:
```

The function `getConcatenation` is called automatically by LeetCode.
You **do not** write input/output code.

---

### 2. Finding the Length of the Array

```python
n = len(nums)
```

If:

```
nums = [1, 2, 1]
```

Then:

```
n = 3
```

We need this because the output array must be of size `2n`.

---

### 3. Creating the Result Array

```python
res = [0] * (2 * n)
```

This creates a list of size `2n` filled with zeros.

For `n = 3`:

```
res = [0, 0, 0, 0, 0, 0]
```

We will overwrite these values in the loop.

---

### 4. Looping Over the Result Array

```python
for i in range(2 * n):
```

The loop runs from:

```
i = 0 to 2n - 1
```

For `n = 3`:

```
i = 0, 1, 2, 3, 4, 5
```

Each value of `i` corresponds to one index in the result array.

---

### 5. The Key Line: Using Modulo

```python
res[i] = nums[i % n]
```

This is the most important idea in the solution.

#### Why modulo (`%`) is needed

* The array `nums` only has indices from `0` to `n - 1`
* But `i` goes up to `2n - 1`
* Accessing `nums[i]` directly would cause an index error

Modulo ensures that the index **wraps around**.

---

### 6. How `i % n` Works

For `nums = [1, 2, 1]` and `n = 3`:

| i | i % n | nums[i % n] |
| - | ----- | ----------- |
| 0 | 0     | 1           |
| 1 | 1     | 2           |
| 2 | 2     | 1           |
| 3 | 0     | 1           |
| 4 | 1     | 2           |
| 5 | 2     | 1           |

This repeats the array safely without extra conditions.

---

### 7. Returning the Result

```python
return res
```

LeetCode expects the function to **return** the final array, not print it.

---

## Final Output Example

```
Input:  [1, 2, 1]
Output: [1, 2, 1, 1, 2, 1]
```

---

## Time and Space Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(2n)`

---

## Key Takeaway

> **Modulo (`%`) converts a linear index into a circular index.**

This concept is widely used in:

* Circular arrays
* Sliding window problems
* Ring buffers
* Hashing
* Round-robin scheduling

Understanding this idea is extremely valuable for interviews and real-world systems.
