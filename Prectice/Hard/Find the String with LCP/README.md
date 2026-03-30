# Find the String from LCP Matrix — LeetCode Problem #2953

## Problem Statement

You are given an `n × n` integer matrix `lcp` where `lcp[i][j]` is the **length of the longest common prefix** between the suffixes of some unknown string `word` starting at index `i` and index `j`.

Return *any* string `word` that matches the given `lcp` matrix. If no valid string exists, return `""`.

> A **suffix** of a string starting at index `i` is the substring `word[i:]`.  
> The **longest common prefix** of two strings is the longest string that is a prefix of both.

**Example:**
```
word = "abab"
suffix at 0 → "abab"
suffix at 2 → "ab"
lcp[0][2] = len(common prefix of "abab" and "ab") = 2

lcp = [[4,0,2,0],
       [0,3,0,1],
       [2,0,2,0],
       [0,1,0,1]]
```

**Given lcp:**
```
Input:  lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]
Output: "abcd"  (or any valid string like "dcba", "aaaa" won't work here)
```

---

## Solution Approach — Clique-Based Character Assignment + LCP Verification

```python
import numpy as np
from typing import List

class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        L = np.array(lcp, dtype=float)

        # Step 1: Diagonal validation
        for i in range(n):
            if lcp[i][i] != n - i:
                return ""

        # Step 2: Build equality graph
        E = (L > 0).astype(float)

        # Step 3: Assign characters via clique grouping
        res = [0] * n
        current_char = 1

        for i in range(n):
            if res[i] > 0: continue
            if current_char > 26: return ""

            v = E[:, i]
            clique_indices = np.where(v > 0.5)[0]

            for idx in clique_indices:
                if res[idx] == 0:
                    res[idx] = current_char
                elif res[idx] != current_char:
                    return ""

            current_char += 1

        # Step 4: Build candidate word
        word = "".join(chr(ord('a') + c - 1) for c in res)

        # Step 5: Full LCP verification
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                expected = 0
                if word[i] == word[j]:
                    expected = 1 + (lcp[i+1][j+1] if i+1 < n and j+1 < n else 0)
                if lcp[i][j] != expected:
                    return ""

        return word
```

---

### Core Idea — Reconstruct → Verify

The solution works in two major phases:

```
Phase 1 — RECONSTRUCT         Phase 2 — VERIFY
  ┌─────────────────┐            ┌──────────────────────┐
  │ Validate diagonal│           │ Recompute every lcp   │
  │ Build eq. graph  │   word    │ entry from the word   │
  │ Assign chars     │ ───────►  │ Compare vs input lcp  │
  │ Build candidate  │           │ Return "" if mismatch │
  └─────────────────┘            └──────────────────────┘
```

If the reconstructed word produces a matching LCP matrix — it's valid. If anything mismatches at any stage, return `""`.

---

### Step-by-Step Breakdown

#### Step 1 — Diagonal Validation
```python
for i in range(n):
    if lcp[i][i] != n - i:
        return ""
```
`lcp[i][i]` is the LCP of `word[i:]` with itself — the full suffix length, which must be exactly `n - i`. If any diagonal entry violates this, the matrix is structurally invalid.

```
For n = 4:
  lcp[0][0] must = 4
  lcp[1][1] must = 3
  lcp[2][2] must = 2
  lcp[3][3] must = 1
```

#### Step 2 — Build Equality Graph
```python
E = (L > 0).astype(float)
```
`lcp[i][j] > 0` means `word[i] == word[j]` (they share at least one character). The matrix `E` is a binary **equality graph** where `E[i][j] = 1` means position `i` and position `j` must have the same character.

#### Step 3 — Clique-Based Character Assignment
```python
for i in range(n):
    if res[i] > 0: continue
    if current_char > 26: return ""
    v = E[:, i]
    clique_indices = np.where(v > 0.5)[0]
    for idx in clique_indices:
        if res[idx] == 0:
            res[idx] = current_char
        elif res[idx] != current_char:
            return ""
    current_char += 1
```
For each unassigned position `i`, find all positions connected to it (column `i` of `E`). All connected positions form a **clique** — they all share the same character. Assign the next available character to the whole group. If a conflict is detected (a position already has a different character), return `""`.

#### Step 4 — Build Candidate Word
```python
word = "".join(chr(ord('a') + c - 1) for c in res)
```
Convert character codes (1=`'a'`, 2=`'b'`, …) to an actual string.

#### Step 5 — Full LCP Verification (Bottom-Up DP)
```python
for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        expected = 0
        if word[i] == word[j]:
            expected = 1 + (lcp[i+1][j+1] if i+1 < n and j+1 < n else 0)
        if lcp[i][j] != expected:
            return ""
```
Recompute what `lcp[i][j]` should be using the classic LCP recurrence:

```
lcp[i][j] = 0                          if word[i] ≠ word[j]
lcp[i][j] = 1 + lcp[i+1][j+1]         if word[i] == word[j]
```
If the computed value doesn't match the input at every cell, return `""`.

---

### Trace Through `lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]`

**Step 1 — Diagonal check:** `4, 3, 2, 1` == `n-0, n-1, n-2, n-3` = `4, 3, 2, 1` ✅

**Step 2 — Equality matrix E** (lcp > 0):
```
E = [[1,1,1,1],
     [1,1,1,1],
     [1,1,1,1],
     [1,1,1,1]]
```
Every pair has lcp > 0 — wait, but the expected output is `"abcd"` (all different). Let's check the verification step — this is where the clique assignment would succeed but the full DP check would catch the pattern.

**Step 3 — Clique assignment:**
All positions initially connected → assign all char 1 (`'a'`) → `word = "aaaa"`

**Step 5 — Verification of `word = "aaaa"`:**
```
lcp[2][3]: word[2]=='a'==word[3] → expected = 1 + lcp[3][4]
           i+1=3, j+1=4 → out of bounds → expected = 1 + 0 = 1 ✅
lcp[1][2]: expected = 1 + lcp[2][3] = 1 + 1 = 2 ✅
lcp[0][1]: expected = 1 + lcp[1][2] = 1 + 2 = 3 ✅
lcp[0][0]: expected = 1 + lcp[1][1] = 1 + 3 = 4 ✅
```

All cells verify → **Output: `"aaaa"`** ✅

*(Note: Multiple valid answers may exist for a given LCP matrix.)*

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n³)** — clique assignment O(n²) + full verification O(n²) with O(n) string ops; dominated by verification |
| Space Complexity | **O(n²)** — storing the numpy matrix `L` and equality matrix `E` |

---

## Knowledge Gained

### 1. The LCP Recurrence — Core DP Relation
The backbone of this entire problem is:
```
lcp[i][j] = 0                    if word[i] ≠ word[j]
lcp[i][j] = 1 + lcp[i+1][j+1]   if word[i] == word[j]
```
This recurrence is computed **bottom-up** (from `n-1` down to `0`) so that `lcp[i+1][j+1]` is always already computed when needed. This is classic **2D Dynamic Programming** applied to suffix comparison.

### 2. Reconstruct → Verify Pattern
Rather than trying to build the correct string directly (hard), this solution:
1. **Reconstructs** a *candidate* answer from partial information (equality graph)
2. **Verifies** the candidate produces the exact input matrix

This two-phase pattern — reconstruct then verify — is a powerful strategy for constraint satisfaction problems where direct construction is error-prone.

### 3. Graph Theory — Equality Cliques
Positions where `lcp[i][j] > 0` form **connected components** in the equality graph. All positions in the same component must share the same character. Using `np.where(v > 0.5)` to extract a column is essentially finding neighbors in an adjacency matrix — a graph traversal encoded as a linear algebra operation.

### 4. NumPy for Matrix Operations
```python
L = np.array(lcp, dtype=float)
E = (L > 0).astype(float)
v = E[:, i]                      # extract entire column i
clique_indices = np.where(v > 0.5)[0]
```
NumPy enables vectorized column extraction and boolean masking in one line, replacing explicit nested loops. This is a practical demonstration of how numerical libraries accelerate matrix-heavy algorithm problems.

### 5. Diagonal as a Structural Invariant
`lcp[i][i] = n - i` is a **necessary condition** for any valid LCP matrix. Checking this first is a fast O(n) filter that immediately rejects malformed inputs before doing any heavier computation — a guard clause applied at the matrix level.

### 6. Character Encoding — `chr(ord('a') + c - 1)`
```python
chr(ord('a') + c - 1)
```
Converting integer codes (1→`'a'`, 2→`'b'`, …, 26→`'z'`) to characters using ASCII arithmetic is a standard technique. `ord('a') = 97`, so `chr(97 + 0) = 'a'`, `chr(97 + 1) = 'b'`, etc. The `c - 1` offset aligns the 1-indexed internal codes with 0-indexed ASCII offsets.

### 7. The 26-Character Constraint
```python
if current_char > 26: return ""
```
If the equality graph has more than 26 connected components, we'd need more than 26 distinct characters — impossible with lowercase English letters. This is an early exit that respects the domain constraint of the problem.

---

## Key Concepts Map

```
                    ┌──────────────────────────────────┐
                    │         LCP Matrix Problem        │
                    └──────────────┬───────────────────┘
                                   │
          ┌────────────────────────┼───────────────────────┐
          │                        │                        │
   ┌──────▼──────┐        ┌────────▼──────┐       ┌───────▼────────┐
   │  Validation  │        │  Graph Theory │       │  2D Bottom-Up  │
   │  lcp[i][i]  │        │  Eq. Cliques  │       │  DP Recurrence │
   │  = n - i    │        │  via NumPy    │       │  Verification  │
   └─────────────┘        └───────────────┘       └────────────────┘
```

---

## Test Run

```
lcp = [[4,3,2,1],[3,3,2,1],[2,2,2,1],[1,1,1,1]]

Output → The Result: aaaa
```

*(Any string whose LCP matrix matches the input is a valid answer.)*
