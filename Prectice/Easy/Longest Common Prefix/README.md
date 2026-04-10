# Longest Common Prefix — LeetCode Problem #14

## Problem Statement

Given an array of strings `strs`, find the **longest common prefix** string among all strings. If there is no common prefix, return an empty string `""`.

**Examples:**
```
Input:  strs = ["flower","flow","flight"]  →  Output: "fl"
Input:  strs = ["dog","racecar","car"]     →  Output: ""
Input:  strs = ["interview","inter","int"] →  Output: "int"
Input:  strs = ["a"]                       →  Output: "a"
```

---

## Solution Approach — Sort + Compare First and Last

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        s1 = strs[0]
        s2 = strs[-1]

        idx = 0

        while idx < len(s1) and idx < len(s2):
            if s1[idx] == s2[idx]:
                idx += 1
            else:
                break

        return s1[:idx]
```

### Core Insight — Why Compare Only First and Last?

After sorting lexicographically, the **first** and **last** strings are the most **different** from each other in the entire list. If a prefix is shared between these two extremes, it is guaranteed to be shared by every string in between.

```
Before sort: ["flower", "flow", "flight"]
After sort:  ["flight", "flow", "flower"]
                  ↑                 ↑
                 s1                s2   ← most different pair
```

The common prefix of `"flight"` and `"flower"` is `"fl"` — which is also the prefix of every string in the list.

---

### How It Works — Step by Step

**Step 1 — Sort the Array**
```python
strs.sort()
```
Lexicographic sort arranges strings alphabetically. This costs O(n log n) but unlocks the key optimization: only two strings need to be compared.

**Step 2 — Pick the Boundary Strings**
```python
s1 = strs[0]    # lexicographically smallest  → "flight"
s2 = strs[-1]   # lexicographically largest   → "flower"
```

**Step 3 — Walk Character by Character**
```python
while idx < len(s1) and idx < len(s2):
    if s1[idx] == s2[idx]:
        idx += 1
    else:
        break
```
Advance `idx` as long as both strings share the same character. Stop as soon as a mismatch is found or either string runs out.

**Step 4 — Slice Out the Prefix**
```python
return s1[:idx]
```
`s1[:idx]` extracts the matching prefix from index `0` up to (but not including) `idx`.

---

### Trace Through `strs = ["flower", "flow", "flight"]`

**After sort:** `["flight", "flow", "flower"]`
```
s1 = "flight"
s2 = "flower"
```

| `idx` | `s1[idx]` | `s2[idx]` | Match? | Action      |
|-------|-----------|-----------|--------|-------------|
| 0     | `'f'`     | `'f'`     | ✅     | `idx → 1`   |
| 1     | `'l'`     | `'l'`     | ✅     | `idx → 2`   |
| 2     | `'i'`     | `'o'`     | ❌     | `break`     |

```python
return s1[:2]  →  "fl"
```

**Final Output → `"fl"`** ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n log n + m)** — sorting takes O(n log n); prefix comparison takes O(m) where m = length of shortest string |
| Space Complexity | **O(1)** — only two pointers and an index used; sort is in-place |

---

## Knowledge Gained

### 1. Lexicographic Sorting as a Problem-Reduction Tool
Sorting the array reduces an n-string comparison to a **2-string comparison**. This is a powerful insight: after sorting, the first and last strings represent the maximum possible divergence, making them the only pair worth comparing.

> **Reusable in:** Grouping anagrams, finding duplicates, interval merging — sorting often reveals hidden structure.

### 2. Boundary-Based Reasoning
In a sorted collection, the **extremes** (first and last) bound all other elements. Any property shared by the extremes is shared by everything in between. This reasoning pattern applies far beyond this problem — it's the foundation of binary search, two-pointer, and divide-and-conquer strategies.

### 3. String Slicing — `s1[:idx]`
`s1[:idx]` returns characters from index `0` to `idx - 1`. When `idx = 0` (no common prefix), it correctly returns `""`. When `idx = len(s1)` (full match), it returns all of `s1`. The slice handles both edge cases naturally — no extra `if` blocks needed.

### 4. Dual Boundary While Loop
```python
while idx < len(s1) and idx < len(s2):
```
Checking **both** lengths prevents `IndexError` when strings have different lengths. This dual-guard pattern is essential whenever you traverse two sequences simultaneously.

### 5. `strs[0]` and `strs[-1]` — Pythonic Indexing
Python's negative indexing (`strs[-1]`) accesses the last element without needing `strs[len(strs)-1]`. This is clean and idiomatic Python, useful whenever you need first/last elements.

### 6. The Elegance of Not Comparing Every String
A naive approach compares the prefix against all `n` strings one by one — O(n × m). This solution exploits sort order to skip all middle strings entirely, achieving O(m) for the comparison step. Recognizing when you can **skip redundant work** is a hallmark of efficient algorithm design.

---

## Alternative Approaches

### Option A — Horizontal Scanning (No Sort)
Start with the first string as the prefix. Keep trimming it until every string starts with it.

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    prefix = strs[0]

    for s in strs[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]        # trim one char from the right
            if not prefix:
                return ""

    return prefix
```

| Metric | Value |
|---|---|
| Time Complexity | O(n × m) |
| Space Complexity | O(1) |

### Option B — Vertical Scanning
Compare character by character across all strings at each position.

```python
def longestCommonPrefix(self, strs: List[str]) -> str:
    for i, char in enumerate(strs[0]):
        for s in strs[1:]:
            if i >= len(s) or s[i] != char:
                return strs[0][:i]
    return strs[0]
```

| Metric | Value |
|---|---|
| Time Complexity | O(n × m) |
| Space Complexity | O(1) |

### Comparison Table

| Approach | Time | Space | Key Idea |
|---|---|---|---|
| Sort + Compare Extremes (current) | O(n log n + m) | O(1) | Only first & last matter after sort |
| Horizontal Scanning | O(n × m) | O(1) | Trim prefix string progressively |
| Vertical Scanning | O(n × m) | O(1) | Column-by-column character check |
| Divide & Conquer | O(n × m) | O(m log n) | Split list, merge prefix results |
| Binary Search | O(n × m log m) | O(1) | Binary search on prefix length |

The sort-based approach is the most elegant for interviews — it reduces n comparisons to 1 with a simple, justifiable insight.

---

## Test Run

```
strs = ["flower", "flow", "flight"]

Output → Biggest Prefix: fl
```
