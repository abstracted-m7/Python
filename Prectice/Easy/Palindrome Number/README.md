# Palindrome Number — LeetCode Problem #9

## Problem Statement

Given an integer `x`, return `true` if `x` is a **palindrome**, and `false` otherwise.

A number is a palindrome when it reads the same forward and backward.

**Examples:**
```
Input:  x = 121     →  Output: True   (121 reversed is 121)
Input:  x = -121    →  Output: False  (negative numbers are never palindromes)
Input:  x = 10      →  Output: False  (10 reversed is 01, not equal)
```

---

## Solution Approach — Full Integer Reversal

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        rev = 0
        num = x
        while num != 0:
            rev = rev * 10 + num % 10
            num = num // 10

        return rev == x
```

### How It Works — Step by Step

**Step 1 — Early Exit for Negatives**
```
if x < 0: return False
```
Negative numbers like `-121` can never be palindromes because of the leading `-` sign, so we reject them immediately.

**Step 2 — Preserve the Original**
```
num = x
```
We work on a copy `num` so the original `x` stays intact for the final comparison.

**Step 3 — Reverse the Digits using Math**
```
while num != 0:
    rev = rev * 10 + num % 10   ← extract last digit and append to rev
    num = num // 10              ← remove last digit from num
```

Trace through `x = 121`:

| Iteration | `num` | `num % 10` | `rev` |
|-----------|-------|-----------|-------|
| Start     | 121   | —         | 0     |
| 1st       | 12    | 1         | 1     |
| 2nd       | 1     | 2         | 12    |
| 3rd       | 0     | 1         | 121   |

**Step 4 — Compare**
```
return rev == x   →   121 == 121   →   True ✅
```

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(log₁₀ n)** — we process each digit once |
| Space Complexity | **O(1)** — only two integer variables used |

---

## Knowledge Gained

### 1. Digit Extraction with Modulo ( `%` )
`num % 10` always gives the **last digit** of any integer. This is a fundamental technique used in many number-manipulation problems (digit sum, reverse number, check divisibility, etc.).

### 2. Digit Removal with Floor Division ( `//` )
`num // 10` strips the last digit from a number. Combined with `%`, these two operations let you process any integer digit-by-digit — no string conversion needed.

### 3. Reversing a Number Mathematically
The pattern `rev = rev * 10 + digit` is the standard algorithm to build a reversed integer:
- Shift existing digits left by multiplying by 10.
- Append the new digit at the units place.

This pattern is reusable in problems like **Reverse Integer (LeetCode #7)**.

### 4. Early Exit / Guard Clause Pattern
Handling the negative case first with an early `return False` keeps the main logic clean and avoids unnecessary computation — a clean coding habit known as a **guard clause**.

### 5. Non-Destructive Variable Usage
Copying `x` into `num` before modifying it preserves the original value for the final comparison. This prevents a subtle bug where you'd be comparing the reversed number against `0` instead of the original.

### 6. No String Conversion Needed
A common naive approach is `str(x) == str(x)[::-1]`. While it works, the mathematical approach is more efficient in memory and better demonstrates understanding of number theory.

---

## Alternative: String Reversal (Simpler but Less Optimal)

```python
def isPalindrome(self, x: int) -> bool:
    if x < 0:
        return False
    return str(x) == str(x)[::-1]
```

| Metric | Value |
|---|---|
| Time Complexity | **O(n)** — string slicing |
| Space Complexity | **O(n)** — new string created |

The mathematical approach is preferred in interviews as it avoids extra memory allocation.

---

## Test Run

```
x = 121

Output → Palindrome: True
```
