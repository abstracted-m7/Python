# Matrix Similarity After Cyclic Shifts — LeetCode Problem #2946

## Problem Statement

You are given a 2D integer matrix `mat` of size `m × n` and an integer `k`.

The matrix is **similar** to itself after the following cyclic shifts on **every row**:
- **Even-indexed rows** (0, 2, 4, …) are cyclically shifted **left** by `k` positions.
- **Odd-indexed rows** (1, 3, 5, …) are cyclically shifted **right** by `k` positions.

Return `true` if the matrix remains identical after these shifts, otherwise return `false`.

**Examples:**
```
Input:  mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4  →  Output: False
Input:  mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]],  k = 2  →  Output: True
```

---

## Solution Approach — Modular Index Comparison

```python
from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])

        k %= n   # reduce k to effective shift within row length

        for i in range(m):
            for j in range(n):
                if i % 2 == 0:
                    # even row → left shift: position j becomes position (j+k)%n
                    if mat[i][j] != mat[i][(j + k) % n]:
                        return False
                else:
                    # odd row → right shift: position j becomes position (j-k)%n
                    if mat[i][j] != mat[i][(j - k) % n]:
                        return False

        return True
```

### Core Idea — Simulate the Shift Without Moving Anything

Instead of physically shifting rows and comparing two matrices, we check **in-place** whether the element at position `j` equals the element that would arrive at `j` after the shift. This avoids creating any new arrays.

```
Left shift by k:   element at j comes from position (j + k) % n
Right shift by k:  element at j comes from position (j - k) % n
```

If every element matches its shifted counterpart, the row looks identical after the shift — and so does the matrix.

---

### How It Works — Step by Step

**Step 1 — Get Matrix Dimensions**
```python
m, n = len(mat), len(mat[0])
```
`m` = number of rows, `n` = number of columns (row length). `n` is critical for the modular wrap-around.

**Step 2 — Reduce k with Modulo**
```python
k %= n
```
Shifting a row of length `n` by `n` positions brings it back to its original state. So `k = 7` on a row of length `3` is the same as `k = 1`. This reduction eliminates redundant full rotations.

> **Key insight:** `k = 4` on a 3-column row → `4 % 3 = 1` → only 1 actual shift matters.

**Step 3 — Check Even Rows (Left Shift)**
```python
if i % 2 == 0:
    if mat[i][j] != mat[i][(j + k) % n]:
        return False
```
After a left shift by `k`, the element originally at column `j + k` moves to column `j`. So for the row to look the same, `mat[i][j]` must equal `mat[i][(j + k) % n]`.

**Step 4 — Check Odd Rows (Right Shift)**
```python
else:
    if mat[i][j] != mat[i][(j - k) % n]:
        return False
```
After a right shift by `k`, the element originally at column `j - k` moves to column `j`. Python handles negative indices in modulo correctly: `(-1) % n = n - 1`, so no special boundary handling is needed.

**Step 5 — Return True if All Match**
```python
return True
```
If no mismatch was found across all rows and columns, the matrix is similar to itself after the shifts.

---

### Trace Through `mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2`

**Dimensions:** m=3, n=4 → `k %= 4` → `k = 2`

**Row 0 (even → left shift by 2):**
| `j` | `mat[0][j]` | `(j+2)%4` | `mat[0][(j+2)%4]` | Match? |
|-----|-------------|-----------|-------------------|--------|
| 0   | 1           | 2         | 1                 | ✅     |
| 1   | 2           | 3         | 2                 | ✅     |
| 2   | 1           | 0         | 1                 | ✅     |
| 3   | 2           | 1         | 2                 | ✅     |

**Row 1 (odd → right shift by 2):**
| `j` | `mat[1][j]` | `(j-2)%4` | `mat[1][(j-2)%4]` | Match? |
|-----|-------------|-----------|-------------------|--------|
| 0   | 5           | 2         | 5                 | ✅     |
| 1   | 5           | 3         | 5                 | ✅     |
| 2   | 5           | 0         | 5                 | ✅     |
| 3   | 5           | 1         | 5                 | ✅     |

**Row 2 (even → left shift by 2):**
| `j` | `mat[2][j]` | `(j+2)%4` | `mat[2][(j+2)%4]` | Match? |
|-----|-------------|-----------|-------------------|--------|
| 0   | 6           | 2         | 6                 | ✅     |
| 1   | 3           | 3         | 3                 | ✅     |
| 2   | 6           | 0         | 6                 | ✅     |
| 3   | 3           | 1         | 3                 | ✅     |

**All match → `True`** ✅

---

### Why `mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4` → `False`

`k %= 3` → `k = 1`

**Row 0 (even → left shift by 1):**
| `j` | `mat[0][j]` | `(j+1)%3` | `mat[0][(j+1)%3]` | Match? |
|-----|-------------|-----------|-------------------|--------|
| 0   | 1           | 1         | 2                 | ❌     |

Mismatch found immediately → return `False` ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(m × n)** — every cell is visited exactly once |
| Space Complexity | **O(1)** — comparison done in-place, no extra arrays created |

---

## Knowledge Gained

### 1. Cyclic / Circular Array Indexing with Modulo
The expression `(j + k) % n` is the fundamental formula for **circular wrapping** in arrays. It ensures the index never goes out of bounds — it simply wraps around to the beginning.

```
n = 4, k = 3:
  j=0 → (0+3)%4 = 3
  j=1 → (1+3)%4 = 0   ← wraps around
  j=2 → (2+3)%4 = 1
  j=3 → (3+3)%4 = 2
```

> **Reusable in:** Rotate Array, Circular Queue, Josephus Problem, Game of Life, and any problem involving ring/cycle structures.

### 2. Reducing k with `k %= n` — Eliminating Redundant Rotations
Rotating a row of length `n` by `n` steps gives the same row. So any `k ≥ n` can be reduced to `k % n` without changing the result. This is a **normalization step** that prevents unnecessary work — especially important when `k` could be very large (e.g., `k = 10^9`).

### 3. In-Place Comparison Instead of Physical Shifting
Instead of actually shifting the row and comparing two matrices, we ask: *"What element would land at position j after the shift?"* and compare it directly. This halves memory usage and is a transferable pattern — simulate transformations via **index arithmetic** rather than data movement.

### 4. Python's Negative Modulo Behavior
In Python, `(-1) % 4 = 3` (not `-1` as in C/Java). This means `(j - k) % n` is always a valid non-negative index, even when `j < k`. No special boundary handling or `if j - k < 0` check is ever needed — Python's modulo is always **mathematically correct** for circular indexing.

### 5. Even/Odd Row Detection with `i % 2`
`i % 2 == 0` detects even rows, `i % 2 != 0` (the `else`) handles odd rows. This is the standard idiom for applying **alternating logic** to rows or elements — a pattern seen in problems involving zigzag traversal, checkerboard patterns, and alternating operations.

### 6. Early Return on First Mismatch
```python
if mat[i][j] != mat[i][(j + k) % n]:
    return False
```
Returning `False` immediately upon finding a mismatch avoids checking the rest of the matrix. In the worst case (all match) we check every cell; in the best case (first cell mismatches) we check just one. This is the **fail-fast** principle.

### 7. Row Similarity = Cyclic Rotation Check
A row is unchanged by a cyclic shift of `k` if and only if it has a **period that divides k**. For example, `[1,2,1,2]` has period 2, so shifting by 2 returns the same row. The modular comparison implicitly checks this — if `k % period == 0`, all comparisons will match.

---

## Test Runs

```
mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4
→  k %= 3  →  k = 1
Output → Result: False

mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2
→  k %= 4  →  k = 2
Output → Result: True
```
