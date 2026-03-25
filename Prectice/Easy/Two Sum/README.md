# Two Sum — LeetCode Problem #1

## Problem Statement

Given an array of integers `nums` and an integer `target`, return the **indices** of the two numbers that add up to the target.

- Each input has **exactly one solution**.
- You may **not** use the same element twice.
- The answer can be returned in any order.

**Example:**
```
Input:  nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: nums[0] + nums[1] = 2 + 7 = 9
```

---

## Solution Approach — Brute Force (Nested Loop)

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
```

### How It Works

1. Iterate over every element in the array using the outer loop (`i`).
2. For each element `i`, use the inner loop (`j`) to check every element that comes **after** it.
3. If `nums[i] + nums[j] == target`, the pair is found — return their indices immediately.
4. If no pair is found after all iterations, return an empty list.

This guarantees we check **every unique pair** exactly once, avoiding duplicate checks (e.g., we never re-check `(j, i)` if `(i, j)` was already checked).

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n²)** — nested loops over the array |
| Space Complexity | **O(1)** — no extra data structures used |

---

## Knowledge Gained

### 1. Brute Force as a Baseline
Starting with a brute-force solution is a valid and important first step. It helps verify correctness before optimizing. This O(n²) solution is easy to understand and implement.

### 2. Two-Pointer Loop Pattern
Using `range(i + 1, n)` for the inner loop is a classic technique to avoid comparing an element with itself and to skip already-checked pairs — a pattern reusable across many array problems.

### 3. Early Return Optimization
Returning immediately upon finding the answer (`return [i, j]`) avoids unnecessary iterations, making the best-case performance faster than the worst case.

### 4. Type Hints in Python
Using `List[int]` from the `typing` module improves code readability and makes function signatures self-documenting — a good professional habit.

### 5. Path to Optimization
This brute-force solution opens the door to understanding why a **HashMap-based approach** (O(n) time, O(n) space) is more efficient:
- Store each number's index in a dictionary as you iterate.
- For each number, check if `target - num` already exists in the dictionary.
- This reduces two passes to a single pass.

---

## Alternative: Optimized HashMap Solution

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

| Metric | Value |
|---|---|
| Time Complexity | **O(n)** |
| Space Complexity | **O(n)** |

---

## Test Run

```
nums   = [2, 7, 11, 15]
target = 9

Output → Indices: [0, 1]
```
