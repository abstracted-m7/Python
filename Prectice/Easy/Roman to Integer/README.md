# Roman to Integer — LeetCode Problem #13

## Problem Statement

Given a Roman numeral string `s`, convert it to an **integer**.

Roman numerals use seven symbols:

| Symbol | Value |
|--------|-------|
| I      | 1     |
| V      | 5     |
| X      | 10    |
| L      | 50    |
| C      | 100   |
| D      | 500   |
| M      | 1000  |

### Subtractive Notation Rule
When a **smaller value appears before a larger value**, it is **subtracted** instead of added:
```
IV  =  5  - 1  =  4
IX  =  10 - 1  =  9
XL  =  50 - 10 =  40
XC  =  100- 10 =  90
CD  =  500- 100=  400
CM  =  1000-100=  900
```

**Examples:**
```
Input:  s = "III"      →  Output: 3
Input:  s = "IV"       →  Output: 4
Input:  s = "DLXXXV"   →  Output: 585
Input:  s = "MCMXCIV"  →  Output: 1994
```

---

## Solution Approach — Lookahead Comparison

```python
class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        result = 0

        for i in range(len(s)):
            curr     = romans[s[i]]
            next_val = romans[s[i+1]] if i+1 < len(s) else 0

            if curr < next_val:
                result -= curr
            else:
                result += curr

        return result
```

### Core Idea
At every position, **peek at the next character**. If the current symbol is smaller than the next one, it's part of a subtractive pair — subtract it. Otherwise, add it normally.

---

### How It Works — Step by Step

**Step 1 — Build the Lookup Map**
```python
romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
```
A dictionary maps every Roman symbol to its integer value, enabling O(1) lookup.

**Step 2 — Iterate with Lookahead**
```python
for i in range(len(s)):
    curr     = romans[s[i]]
    next_val = romans[s[i+1]] if i+1 < len(s) else 0
```
For each character, get the current value and the **next** character's value.
The ternary guard `if i+1 < len(s) else 0` safely handles the last character — it has no next symbol, so `next_val` defaults to `0`.

**Step 3 — Add or Subtract**
```python
if curr < next_val:
    result -= curr   # subtractive case  e.g. I in "IV"
else:
    result += curr   # additive case     e.g. D in "DL"
```
This single `if/else` elegantly handles both standard and subtractive notation.

---

### Trace Through `s = "DLXXXV"` → Expected: `585`

| `i` | `s[i]` | `curr` | `next_val` | `curr < next_val?` | Action      | `result` |
|-----|--------|--------|-----------|-------------------|-------------|----------|
| 0   | `D`    | 500    | 50        | ❌ No             | `+500`      | 500      |
| 1   | `L`    | 50     | 10        | ❌ No             | `+50`       | 550      |
| 2   | `X`    | 10     | 10        | ❌ No             | `+10`       | 560      |
| 3   | `X`    | 10     | 10        | ❌ No             | `+10`       | 570      |
| 4   | `X`    | 10     | 5         | ❌ No             | `+10`       | 580      |
| 5   | `V`    | 5      | 0 (end)   | ❌ No             | `+5`        | 585      |

**Final Output → `585`** ✅

### Bonus Trace — `s = "MCMXCIV"` → Expected: `1994`

| `i` | `s[i]` | `curr` | `next_val` | Action  | `result` |
|-----|--------|--------|-----------|---------|----------|
| 0   | `M`    | 1000   | 100       | `+1000` | 1000     |
| 1   | `C`    | 100    | 1000      | `-100`  | 900      |
| 2   | `M`    | 1000   | 10        | `+1000` | 1900     |
| 3   | `X`    | 10     | 100       | `-10`   | 1890     |
| 4   | `C`    | 100    | 1         | `+100`  | 1990     |
| 5   | `I`    | 1      | 5         | `-1`    | 1989     |
| 6   | `V`    | 5      | 0 (end)   | `+5`    | 1994     |

**Final Output → `1994`** ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n)** — single pass through the string |
| Space Complexity | **O(1)** — dictionary is fixed size (7 entries), no extra structures |

---

## Knowledge Gained

### 1. HashMap for Constant-Time Lookup
Storing symbol → value mappings in a dictionary gives O(1) access per character. This is the standard way to eliminate repeated conditional chains (`if s[i] == 'I': return 1 elif ...`) and is reusable in any symbol-mapping problem.

### 2. Lookahead Pattern — Peeking at the Next Element
```python
next_val = romans[s[i+1]] if i+1 < len(s) else 0
```
Reading one position ahead while iterating is a clean and common technique. The ternary expression safely handles the boundary (last index) by providing a **sentinel value** of `0`, eliminating the need for a separate edge-case block.

### 3. Sentinel / Default Value Trick
Defaulting `next_val` to `0` at the end of the string is elegant — since `curr` (at minimum 1) is always ≥ 1 > 0, the `else` branch always fires for the last character, which is always correct behavior.

### 4. Subtractive Logic in One Line
```python
if curr < next_val:
    result -= curr
else:
    result += curr
```
Instead of hardcoding all 6 subtractive pairs (IV, IX, XL, XC, CD, CM), a single numeric comparison handles them all. This is a great example of finding the **mathematical rule** behind a pattern rather than enumerating special cases.

### 5. Ternary Expression for Clean Boundary Handling
```python
next_val = romans[s[i+1]] if i+1 < len(s) else 0
```
Python's inline ternary `value_if_true if condition else value_if_false` avoids an extra `if` block and keeps logic concise. It's especially useful when reading ahead or behind in arrays and strings.

### 6. Reading the Problem as a Math Rule
The key insight is: **"if current < next, subtract; otherwise add."** Recognizing this underlying rule — rather than treating each subtractive pair as a special case — is what makes the solution clean and generalizable.

---

## Alternative Approach — Iterate Right to Left

Process the string in reverse. Track the previous value. If `curr < prev`, subtract; otherwise add. No lookahead needed.

```python
def romanToInt(self, s: str) -> int:
    romans = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
    result = 0
    prev = 0

    for char in reversed(s):
        curr = romans[char]
        if curr < prev:
            result -= curr
        else:
            result += curr
        prev = curr

    return result
```

### Comparison Table

| Approach | Direction | Lookahead / Lookbehind | Time | Space |
|---|---|---|---|---|
| Lookahead (current) | Left → Right | Peek at `i+1` | O(n) | O(1) |
| Reverse iteration | Right → Left | Track `prev` | O(n) | O(1) |

Both are equivalent in performance. The right-to-left approach avoids the index boundary check entirely.

---

## Test Run

```
s = "DLXXXV"

Output → Int value: 585
```
