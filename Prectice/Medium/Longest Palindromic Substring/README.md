# Longest Palindromic Substring — LeetCode Problem #5

## Problem Statement

Given a string `s`, return the **longest palindromic substring** in `s`.

A substring is palindromic if it reads the same forward and backward.

**Examples:**
```
Input:  s = "babab"   →  Output: "babab"
Input:  s = "babad"   →  Output: "bab"   (or "aba", both are valid)
Input:  s = "cbbd"    →  Output: "bb"
Input:  s = "a"       →  Output: "a"
```

---

## Solution Approach — Brute Force (Check All Substrings)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s

        Max_Len = 1
        Max_Str = s[0]

        for i in range(len(s) - 1):
            for j in range(i + 1, len(s)):
                if j - i + 1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
                    Max_Len = j - i + 1
                    Max_Str = s[i:j+1]
        return Max_Str
```

### How It Works — Step by Step

**Step 1 — Early Exit for Single Characters**
```
if len(s) <= 1: return s
```
A string of length 0 or 1 is always a palindrome by definition. Return immediately.

**Step 2 — Initialize Tracker Variables**
```
Max_Len = 1
Max_Str = s[0]
```
We start assuming the first character is the longest palindrome found so far (every single character is a palindrome of length 1).

**Step 3 — Generate Every Substring via Nested Loops**
```
for i in range(len(s) - 1):
    for j in range(i + 1, len(s)):
```
- `i` = start index of the substring
- `j` = end index of the substring
- Together they cover every possible `(start, end)` pair, generating all substrings of length ≥ 2.

**Step 4 — Check Length and Palindrome Together**
```
if j - i + 1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
```
Two conditions must both be true to update:
- `j - i + 1 > Max_Len` → this substring is longer than what we've seen so far (no point checking shorter ones)
- `s[i:j+1] == s[i:j+1][::-1]` → the substring equals its own reverse (palindrome check)

**Step 5 — Update Tracker**
```
Max_Len = j - i + 1
Max_Str = s[i:j+1]
```
Store the new longest palindrome found.

---

### Trace Through `s = "babab"`

| `i` | `j` | Substring | Palindrome? | Max_Str |
|-----|-----|-----------|-------------|---------|
| 0   | 1   | `"ba"`    | ❌          | `"b"`   |
| 0   | 2   | `"bab"`   | ✅          | `"bab"` |
| 0   | 3   | `"baba"`  | ❌          | `"bab"` |
| 0   | 4   | `"babab"` | ✅          | `"babab"` |
| 1   | 2   | `"ab"`    | ❌          | `"babab"` |
| ... | ... | ...       | ...         | `"babab"` |

**Final Output → `"babab"`** ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n³)** — O(n²) pairs × O(n) for each slice + reversal |
| Space Complexity | **O(n)** — temporary substring slices created during reversal |

---

## Knowledge Gained

### 1. Substring Slicing — `s[i:j+1]`
In Python, `s[i:j]` excludes index `j`. To include it, you always write `s[i:j+1]`. This off-by-one detail is crucial and a frequent source of bugs in substring problems.

### 2. Palindrome Check via String Reversal — `[::-1]`
`s[::-1]` is Python's slice-based string reversal. It's clean and readable, but creates a new string in memory — making it O(n) per check. Great for quick validation; not ideal for performance-critical paths.

### 3. Length Formula — `j - i + 1`
The length of a substring `s[i:j+1]` is always `j - i + 1`. This formula appears constantly in sliding window and substring problems — worth memorizing.

### 4. Short-Circuit Evaluation with `and`
```python
if j - i + 1 > Max_Len and s[i:j+1] == s[i:j+1][::-1]:
```
Python evaluates `and` left to right and stops early if the first condition is `False`. Checking length first avoids the expensive O(n) reversal for substrings that can't beat the current best — a small but smart optimization.

### 5. Tracking Best Answer with Two Variables
Using both `Max_Len` (integer) and `Max_Str` (string) together is a clean pattern for "find the best among all candidates" problems. The integer allows fast comparison; the string stores the actual answer.

### 6. Brute Force as a Foundation
This O(n³) approach correctly solves the problem and is a natural starting point. Understanding it deeply makes it easier to appreciate and implement the two optimized approaches below.

---

## Path to Optimization

### Option A — Expand Around Center — O(n²) Time, O(1) Space
For every character (and gap between characters), expand outward as long as the palindrome holds.

```python
def longestPalindrome(self, s: str) -> str:
    def expand(l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]

    result = ""
    for i in range(len(s)):
        odd  = expand(i, i)       # odd-length palindromes  e.g. "aba"
        even = expand(i, i + 1)   # even-length palindromes e.g. "abba"
        result = max(result, odd, even, key=len)
    return result
```

### Option B — Dynamic Programming — O(n²) Time, O(n²) Space
Build a 2D table `dp[i][j] = True` if `s[i:j+1]` is a palindrome, using previously computed results.

```python
def longestPalindrome(self, s: str) -> str:
    n = len(s)
    dp = [[False] * n for _ in range(n)]
    start, max_len = 0, 1

    for i in range(n):
        dp[i][i] = True

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                if length == 2 or dp[i+1][j-1]:
                    dp[i][j] = True
                    if length > max_len:
                        start, max_len = i, length
    return s[start:start + max_len]
```

### Comparison Table

| Approach | Time | Space | Difficulty |
|---|---|---|---|
| Brute Force (current) | O(n³) | O(n) | ⭐ Easy |
| Expand Around Center | O(n²) | O(1) | ⭐⭐ Medium |
| Dynamic Programming | O(n²) | O(n²) | ⭐⭐ Medium |
| Manacher's Algorithm | O(n) | O(n) | ⭐⭐⭐ Hard |

---

## Test Run

```
s = "babab"

Output → Palindrome Substring: babab
```
