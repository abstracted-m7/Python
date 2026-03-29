# Longest Substring Without Repeating Characters — LeetCode Problem #3

## Problem Statement

Given a string `s`, find the length of the **longest substring** without repeating characters.

> A **substring** is a contiguous sequence of characters within a string (unlike a subsequence).

**Examples:**
```
Input:  s = "ababa"   →  Output: 2   ("ab" or "ba")
Input:  s = "abcabcbb"→  Output: 3   ("abc")
Input:  s = "bbbbb"   →  Output: 1   ("b")
Input:  s = ""        →  Output: 0
```

---

## Solution Approach — Sliding Window with HashSet

```python
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0

        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        return maxLength
```

### Core Idea — The Sliding Window

Think of a window `[left ... right]` sliding over the string.
- The window **expands** to the right when the new character is unique.
- The window **shrinks** from the left when a duplicate is found.
- The `charSet` always mirrors exactly what characters are inside the current window.

```
s = "a  b  a  b  a"
      ↑        ↑
     left     right   ← window slides this way →
```

---

### How It Works — Step by Step

**Step 1 — Initialize**
```python
charSet = set()   # tracks characters in current window
left = 0          # left boundary of window
maxLength = 0     # best answer so far
```

**Step 2 — Expand Right**
```python
for right in range(n):
    if s[right] not in charSet:
        charSet.add(s[right])
        maxLength = max(maxLength, right - left + 1)
```
If the incoming character is new, safely add it to the window and update the max length.

**Step 3 — Shrink Left on Duplicate**
```python
    else:
        while s[right] in charSet:
            charSet.remove(s[left])
            left += 1
        charSet.add(s[right])
```
If the incoming character already exists in the window, keep removing from the left side until the duplicate is gone, then add the new character.

---

### Trace Through `s = "ababa"`

| Step | `right` | `s[right]` | `charSet` before | Action | `left` | `charSet` after | `maxLength` |
|------|---------|-----------|-----------------|--------|--------|----------------|-------------|
| 1    | 0       | `'a'`     | `{}`            | Add    | 0      | `{'a'}`        | 1           |
| 2    | 1       | `'b'`     | `{'a'}`         | Add    | 0      | `{'a','b'}`    | 2           |
| 3    | 2       | `'a'`     | `{'a','b'}`     | Duplicate → remove `'a'`, left→1, add `'a'` | 1 | `{'b','a'}` | 2 |
| 4    | 3       | `'b'`     | `{'b','a'}`     | Duplicate → remove `'b'`, left→2, add `'b'` | 2 | `{'a','b'}` | 2 |
| 5    | 4       | `'a'`     | `{'a','b'}`     | Duplicate → remove `'a'`, left→3, add `'a'` | 3 | `{'b','a'}` | 2 |

**Final Output → `2`** ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n)** — each character is added and removed from the set at most once |
| Space Complexity | **O(min(n, m))** — where `m` is the size of the character set (e.g. 26 for lowercase letters) |

---

## Knowledge Gained

### 1. The Sliding Window Pattern
This is one of the most important patterns in string and array problems. A window defined by `[left, right]` expands and contracts dynamically to maintain a valid state, avoiding the O(n²) cost of checking every substring from scratch.

> **Reusable in:** Minimum Window Substring, Max Consecutive Ones, Fruit Into Baskets, and many more.

### 2. HashSet for O(1) Lookups
Using a `set()` instead of a list for `charSet` gives:
- `s[right] not in charSet` → **O(1)** average
- `charSet.add()` → **O(1)** average
- `charSet.remove()` → **O(1)** average

This is what makes the entire algorithm O(n) instead of O(n²).

### 3. Two-Pointer Technique
`left` and `right` are two pointers moving through the string. `right` always moves forward in the outer loop; `left` chases it only when needed. This coordinated movement is the essence of the sliding window.

### 4. Window Length Formula — `right - left + 1`
The current window size is always `right - left + 1`. This formula is fundamental to all sliding window problems and appears in dozens of LeetCode problems.

### 5. Invariant Thinking
The `charSet` always holds **exactly** the characters in the current window `s[left:right+1]` — no more, no less. Maintaining this invariant is what makes the algorithm correct. When you add to the right or remove from the left, the set stays in sync with the window.

### 6. Amortized O(n) — Each Element Touched Twice
Even though there's a `while` loop inside the `for` loop, the total number of operations is still O(n). Each character is added to the set **once** (when `right` reaches it) and removed **at most once** (when `left` passes it). This amortized analysis is a key concept in algorithm efficiency.

---

## Path to Optimization — Optimized Sliding Window with HashMap

The current solution uses a `while` loop to shrink the window one step at a time. A HashMap can jump `left` directly to the right position, avoiding repeated removals.

```python
def lengthOfLongestSubstring(self, s: str) -> int:
    charIndex = {}   # char → most recent index
    left = 0
    maxLength = 0

    for right, char in enumerate(s):
        if char in charIndex and charIndex[char] >= left:
            left = charIndex[char] + 1        # jump left past the duplicate
        charIndex[char] = right               # update latest index
        maxLength = max(maxLength, right - left + 1)

    return maxLength
```

### Comparison Table

| Approach | Time | Space | Window Shrink Strategy |
|---|---|---|---|
| HashSet + while loop (current) | O(n) | O(min(n,m)) | Remove one-by-one from left |
| HashMap + direct jump | O(n) | O(min(n,m)) | Jump `left` directly to duplicate+1 |

Both are O(n) but the HashMap version avoids the inner `while` loop entirely, making it cleaner and slightly faster in practice.

---

## Test Run

```
s = "ababa"

Output → Longest Substring: 2
```
