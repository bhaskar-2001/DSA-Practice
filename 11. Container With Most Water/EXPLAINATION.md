# Leetcode-11 
# Container With Most Water – Explanation

This document explains **two approaches** to solve the problem:
1. Brute Force Approach
2. Optimized Two-Pointer Approach

The goal is to understand **why** the optimized solution works, not just how to write it.

---

## Problem Summary

You are given an integer array `height` where each element represents a vertical line at that index.

You must choose **two lines** such that:
- They form a container with the x-axis
- The container holds the **maximum amount of water**

Water stored is calculated as:

```
Area = (right - left) × min(height[left], height[right])
```

---

## 1. Brute Force Approach

### Idea
- Try **all possible pairs** of lines
- Compute the water each pair can hold
- Track the maximum area

### Why It Works
- It checks every possible container
- Guaranteed to find the maximum

### Why It Is Inefficient
- Number of pairs ≈ n²
- Too slow for large arrays

### Pseudocode
```
maxArea = 0
for i from 0 to n-1:
    for j from i+1 to n-1:
        width = j - i
        height = min(height[i], height[j])
        area = width * height
        maxArea = max(maxArea, area)
return maxArea
```

### Time & Space Complexity
- Time: O(n²)
- Space: O(1)

---

## 2. Optimized Two-Pointer Approach

### Key Insight
The amount of water is limited by the **shorter line**, not the taller one.

Increasing the taller line does not help if the shorter line remains the same.

---

### Strategy
- Start with the widest container (left at start, right at end)
- Gradually reduce width
- Try to increase height by moving the **shorter line**

---

### Why Move the Shorter Pointer?
- Width always decreases when pointers move
- To compensate, height must increase
- Only moving the shorter line gives a chance to increase height

---

### Algorithm Steps
1. Initialize two pointers: `left = 0`, `right = n-1`
2. Calculate area using current pointers
3. Update maximum area
4. Move the pointer pointing to the shorter height
5. Repeat until `left < right`

---

### Pseudocode
```
left = 0
right = n - 1
maxArea = 0

while left < right:
    width = right - left
    height = min(height[left], height[right])
    area = width * height
    maxArea = max(maxArea, area)

    if height[left] < height[right]:
        left += 1
    else:
        right -= 1

return maxArea
```

---

### Time & Space Complexity
- Time: O(n)
- Space: O(1)

---

## Comparison

| Approach | Time | Space | Recommended |
|--------|------|-------|-------------|
| Brute Force | O(n²) | O(1) | ❌ No |
| Two Pointer | O(n) | O(1) | ✅ Yes |

---

## Final Intuition

Always eliminate the **bottleneck** (shorter line).  
This greedy choice is safe and guarantees the optimal result.

---

Happy Coding 🚀
