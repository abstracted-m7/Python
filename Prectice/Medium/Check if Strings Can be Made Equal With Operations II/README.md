# Check if Strings Can be Made Equal With Operations II — LeetCode Problem #2840

## Problem Statement

You are given two strings `s1` and `s2` of **equal length**, consisting only of lowercase English letters.

In one operation, you can swap any two characters at positions `i` and `j` in string `s1` where:
- `i` and `j` have the **same parity** (both even or both odd)
- There is **no restriction** on how far apart they are

Return `true` if `s1` can be transformed into `s2` using **any number** of such operations.

> This is the generalization of Operations I — strings can be any length (not just 4), and same-parity positions anywhere in the string can be freely swapped.

**Examples:**
```
Input:  s1 = "abcdba", s2 = "cabdab"  →  Output: True
Input:  s1 = "abe",    s2 = "bea"     →  Output: False
Input:  s1 = "abab",   s2 = "baba"    →  Output: True
```

---

## Solution Approach — Parity Split + Sort + Compare

```python
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)

        s1_even = ""
        s1_odd  = ""
        s2_even = ""
        s2_odd  = ""

        for i in range(n):
            if i % 2 == 0:
                s1_even += s1[i]
                s2_even += s2[i]
            else:
                s1_odd += s1[i]
                s2_odd += s2[i]

        s1_even = ''.join(sorted(s1_even))
        s2_even = ''.join(sorted(s2_even))
        s1_odd  = ''.join(sorted(s1_odd))
        s2_odd  = ''.join(sorted(s2_odd))

        return s1_even == s2_even and s1_odd == s2_odd
```

### Core Insight — Free Rearrangement Within Parity Groups

Since **any** two same-parity positions can be swapped — and you can do this any number of times — the even-indexed characters can be arranged in **any order** among themselves, and so can the odd-indexed characters. Swaps between even and odd positions are never allowed.

```
s1 = [ a  b  c  d  b  a ]
       ↑     ↑     ↑        → Even group {a, c, b} → freely rearrange
          ↑     ↑     ↑     → Odd  group {b, d, a} → freely rearrange
       0  1  2  3  4  5
```

This means the two strings are equivalent if and only if:
- The **multiset** of even-indexed characters in `s1` equals that of `s2`
- The **multiset** of odd-indexed characters in `s1` equals that of `s2`

Sorting both groups and comparing is the cleanest way to check multiset equality.

---

### How It Works — Step by Step

**Step 1 — Split into Even and Odd Groups**
```python
for i in range(n):
    if i % 2 == 0:
        s1_even += s1[i]
        s2_even += s2[i]
    else:
        s1_odd += s1[i]
        s2_odd += s2[i]
```
Collect characters at even indices into one string, odd indices into another — for both `s1` and `s2`.

**Step 2 — Sort Each Group**
```python
s1_even = ''.join(sorted(s1_even))
s2_even = ''.join(sorted(s2_even))
s1_odd  = ''.join(sorted(s1_odd))
s2_odd  = ''.join(sorted(s2_odd))
```
Sorting normalizes any arrangement into a canonical form. If two groups have the same characters (regardless of order), their sorted versions will be identical.

**Step 3 — Compare Both Groups**
```python
return s1_even == s2_even and s1_odd == s2_odd
```
If both sorted groups match, the strings can be made equal. One `False` in either group is enough to return `False`.

---

### Trace Through `s1 = "abcdba"`, `s2 = "cabdab"`

**Split:**
```
Index:    0    1    2    3    4    5
s1:       a    b    c    d    b    a
s2:       c    a    b    d    a    b
          ↑         ↑         ↑      → Even
               ↑         ↑      ↑   → Odd
```

| Group | s1 chars | s2 chars |
|-------|----------|----------|
| Even  | `a, c, b` | `c, b, a` |
| Odd   | `b, d, a` | `a, d, b` |

**After sorting:**

| Group | s1 sorted | s2 sorted | Match? |
|-------|-----------|-----------|--------|
| Even  | `"abc"`   | `"abc"`   | ✅     |
| Odd   | `"abd"`   | `"abd"`   | ✅     |

**Output → `True`** ✅

---

### Trace Through `s1 = "abe"`, `s2 = "bea"`

**Split:**
```
Index:    0    1    2
s1:       a    b    e
s2:       b    e    a
```

| Group | s1 chars | s2 chars |
|-------|----------|----------|
| Even  | `a, e`   | `b, a`   |
| Odd   | `b`      | `e`      |

**After sorting:**

| Group | s1 sorted | s2 sorted | Match? |
|-------|-----------|-----------|--------|
| Even  | `"ae"`    | `"ab"`    | ❌     |

Even group mismatch → **Output: `False`** ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n log n)** — splitting is O(n); sorting each group is O((n/2) log(n/2)) ≈ O(n log n) |
| Space Complexity | **O(n)** — four substring variables each holding ~n/2 characters |

---

## Knowledge Gained

### 1. Multiset Equality via Sorting
When order doesn't matter but character frequency does, **sort and compare** is the standard O(n log n) technique for checking multiset equality. It's cleaner and more general than building frequency dictionaries for small alphabets.

```python
sorted("bca") == sorted("abc")   # True — same multiset
```

> **Reusable in:** Anagram detection, group anagrams, check permutation, valid anagram (LeetCode #242).

### 2. Step Slicing — `s[0::2]` and `s[1::2]`
Python's step slice syntax is the idiomatic one-liner for parity splitting:
```python
s1_even = s1[0::2]   # every 2nd char starting at 0 → even indices
s1_odd  = s1[1::2]   # every 2nd char starting at 1 → odd indices
```
This replaces the entire `for` loop in a single expression. The current loop-based approach is more explicit and beginner-friendly, but step slicing is the idiomatic Python equivalent.

### 3. String Concatenation in a Loop — A Performance Note
```python
s1_even += s1[i]   # repeated string concatenation
```
In Python, strings are **immutable** — each `+=` creates a new string object in memory, making the loop O(n²) in the worst case. The preferred approach collects characters in a list and joins at the end:
```python
s1_even_chars = []
for i in range(0, n, 2):
    s1_even_chars.append(s1[i])
s1_even = ''.join(s1_even_chars)   # O(n) — single allocation
```
Or more Pythonically: `s1[0::2]` (O(n), single slice).

### 4. `''.join(sorted(...))` — The Sort-String Pattern
```python
''.join(sorted(s1_even))
```
`sorted()` on a string returns a list of characters. `''.join(...)` collapses it back into a string. This two-step combination is the standard Python idiom for sorting characters in a string — used constantly in anagram and permutation problems.

### 5. Simplifying the Final Return
```python
# Verbose (current):
if s1_even == s2_even and s1_odd == s2_odd:
    return True
return False

# Idiomatic Python:
return s1_even == s2_even and s1_odd == s2_odd
```
A boolean expression already evaluates to `True` or `False` — no `if` block needed. Returning it directly is cleaner and more Pythonic.

### 6. Connection to Operations I
This problem is the direct generalization of LeetCode #2839:

| Feature | Operations I | Operations II |
|---|---|---|
| String length | Fixed: 4 | Any even length |
| Swap constraint | Same parity AND distance = 2 | Same parity, any distance |
| Solution strategy | Enumerate 2 cases per group | Sort and compare |
| Time complexity | O(1) | O(n log n) |

In Operations I, the distance constraint limits each group to at most one swap — so enumerating both orderings works. In Operations II, unrestricted same-parity swaps give **full freedom** to rearrange within each group — so sorting is the right tool.

---

## Optimized Version — Step Slicing

```python
def checkStrings(self, s1: str, s2: str) -> bool:
    return (sorted(s1[0::2]) == sorted(s2[0::2]) and
            sorted(s1[1::2]) == sorted(s2[1::2]))
```

This is functionally identical to the current solution but written in 3 lines using Python's step slice syntax.

| Version | Lines of Code | Time | Space |
|---|---|---|---|
| Loop-based (current) | 18 | O(n log n) | O(n) |
| Step-slice (optimized) | 3 | O(n log n) | O(n) |

---

## ⚠️ Bug Note

In the test run, `obj.checkStrings(s1, s1)` passes `s1` as both arguments — comparing a string to itself, which always returns `True`. The correct call should be:
```python
print("Result: ", obj.checkStrings(s1, s2))
#                                       ^^
```

---

## Test Run (Corrected)

```
s1 = "abcdba"
s2 = "cabdab"

Even groups sorted: "abc" == "abc" ✅
Odd  groups sorted: "abd" == "abd" ✅

Output → Result: True
```
