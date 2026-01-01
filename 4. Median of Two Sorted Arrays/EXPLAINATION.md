# Leetcode-4
# Median of Two Sorted arrays – Explanation

## Problem Overview
We are given two **already sorted lists** and need to:
1. Merge them in sorted order
2. Find the median of the merged list

This approach is based on the **two-pointer technique**, similar to the merge step of Merge Sort.

---

## Code Being Explained

```python
a = [1, 3]
b = [2, 4]

merged = []
i = j = 0

while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i]); i += 1
    else:
        merged.append(b[j]); j += 1

merged.extend(a[i:])
merged.extend(b[j:])

n = len(merged)
median = merged[n//2] if n % 2 else (merged[n//2 - 1] + merged[n//2]) / 2
print(median)
```

---

## Step 1: Initialize Variables

- `merged` → empty list to store sorted result
- `i`, `j` → pointers for lists `a` and `b`

```text
merged = []
i = 0, j = 0
```

---

## Step 2: Merge Using Two Pointers

### Pseudocode

```text
WHILE i < len(a) AND j < len(b)
    IF a[i] < b[j]
        add a[i] to merged
        i = i + 1
    ELSE
        add b[j] to merged
        j = j + 1
```

### Dry Run

| Step | a[i] | b[j] | Action | merged |
|----|----|----|------|--------|
| 1 | 1 | 2 | append 1 | [1] |
| 2 | 3 | 2 | append 2 | [1,2] |
| 3 | 3 | 4 | append 3 | [1,2,3] |

Loop ends when one list is exhausted.

---

## Step 3: Add Remaining Elements

```python
merged.extend(a[i:])
merged.extend(b[j:])
```

Result:
```text
merged = [1, 2, 3, 4]
```

---

## Step 4: Median Calculation

Let:
```text
n = len(merged) = 4
```

- If `n` is odd → return middle element
- If `n` is even → return average of two middle elements

```text
median = (merged[1] + merged[2]) / 2
median = (2 + 3) / 2 = 2.5
```

---

## Final Output

```text
2.5
```

---

## Complexity Analysis

- **Time Complexity:** O(n + m)
- **Space Complexity:** O(n + m)

---

## Key Interview Takeaways

- Always ask if arrays are sorted
- Use two-pointer merge to avoid re-sorting
- Median depends on odd/even length

---

## One-Line Summary

Merge two sorted lists using two pointers and calculate the median based on length parity.
