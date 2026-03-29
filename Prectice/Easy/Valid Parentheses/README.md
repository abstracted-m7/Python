# Valid Parentheses — LeetCode Problem #20

## Problem Statement

Given a string `s` containing only the characters `(`, `)`, `{`, `}`, `[`, and `]`, determine if the input string is **valid**.

A string is valid if:
1. Every open bracket is closed by the **same type** of bracket.
2. Open brackets are closed in the **correct order**.
3. Every closing bracket has a **corresponding open bracket**.

**Examples:**
```
Input:  s = "([])"       →  Output: True
Input:  s = "()[]{}"     →  Output: True
Input:  s = "(]"         →  Output: False
Input:  s = "([)]"       →  Output: False
Input:  s = ""           →  Output: True   (empty string is valid)
```

---

## Solution Approach — Stack (LIFO)

```python
from typing import List

class Solution:
    def isValid(self, s: str) -> bool:
        a = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                a.append(s[i])
            else:
                if not a:
                    return False
                top = a.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == ']' and top != '[':
                    return False
                if s[i] == '}' and top != '{':
                    return False

        return len(a) == 0
```

### Core Idea — The Stack Matches Pairs
A **stack** (Last-In First-Out) is the perfect data structure here. Every time you see an opening bracket, push it. Every time you see a closing bracket, the most recently pushed open bracket **must** be its match. If it isn't — or if the stack is empty — the string is invalid.

```
 s  =  ( [ ] )
        ↓
      push (       stack: ['(']
        ↓
      push [       stack: ['(', '[']
        ↓
      pop  [ ← matches ]    stack: ['(']
        ↓
      pop  ( ← matches )    stack: []
        ↓
      stack empty → True ✅
```

---

### How It Works — Step by Step

**Step 1 — Initialize an Empty Stack**
```python
a = []
```
Python's list acts as a stack using `.append()` (push) and `.pop()` (pop from top).

**Step 2 — Push Opening Brackets**
```python
if s[i] == '(' or s[i] == '[' or s[i] == '{':
    a.append(s[i])
```
Whenever an opening bracket is encountered, push it onto the stack to remember it for later.

**Step 3 — Validate Closing Brackets**
```python
else:
    if not a:
        return False
    top = a.pop()
    if s[i] == ')' and top != '(':  return False
    if s[i] == ']' and top != '[':  return False
    if s[i] == '}' and top != '{':  return False
```
Three checks happen on every closing bracket:
- **Empty stack check** (`if not a`) — a closing bracket with nothing on the stack means an unmatched closer. Return `False` immediately.
- **Pop the top** — remove the most recent unmatched opener.
- **Match check** — verify it's the right type. If not, return `False`.

**Step 4 — Final Stack Check**
```python
return len(a) == 0
```
After processing all characters, the stack must be empty. Any leftover opening brackets mean they were never closed.

---

### Trace Through `s = "([])"`

| Step | `s[i]` | Type    | Action            | Stack      | Valid? |
|------|--------|---------|-------------------|------------|--------|
| 0    | `(`    | Opening | push `(`          | `['(']`    | —      |
| 1    | `[`    | Opening | push `[`          | `['(','[']`| —      |
| 2    | `]`    | Closing | pop `[` ✅ matches `]` | `['(']` | —   |
| 3    | `)`    | Closing | pop `(` ✅ matches `)` | `[]`   | —      |
| End  | —      | —       | stack empty ✅    | `[]`       | **True** |

**Final Output → `True`** ✅

### Trace Through `s = "([)]"` — Invalid Case

| Step | `s[i]` | Type    | Action                    | Stack        | Valid?  |
|------|--------|---------|---------------------------|--------------|---------|
| 0    | `(`    | Opening | push `(`                  | `['(']`      | —       |
| 1    | `[`    | Opening | push `[`                  | `['(','[']`  | —       |
| 2    | `)`    | Closing | pop `[` ❌ doesn't match `)` | —          | **False** |

**Final Output → `False`** ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n)** — each character is visited exactly once |
| Space Complexity | **O(n)** — in the worst case (all opening brackets), the stack holds all `n` characters |

---

## Knowledge Gained

### 1. Stack — The Go-To Structure for Matching Problems
Any problem involving **nested** or **ordered pairing** is a strong signal to use a stack. The LIFO property guarantees that the most recently opened bracket is always checked first — exactly what nesting requires.

> **Reusable in:** Evaluate Reverse Polish Notation, Min Stack, Daily Temperatures, Decode String, and many more.

### 2. Python List as a Stack
Python has no built-in `Stack` class. A `list` with `.append()` and `.pop()` behaves as a perfect O(1) stack:
```python
a.append(x)   # push  → O(1)
a.pop()        # pop   → O(1)
not a          # empty check → O(1)
```

### 3. Empty Stack Guard — Critical Edge Case
```python
if not a:
    return False
```
Checking before `.pop()` is essential. Calling `.pop()` on an empty list raises an `IndexError`. This guard handles inputs like `")"` or `"]"` — strings that start with a closing bracket.

### 4. Final `len(a) == 0` Check
Returning `len(a) == 0` (instead of just `True`) catches unmatched **openers** like `"((("`. Without this check, the loop would finish without error but the stack would still hold unmatched brackets. This is a subtle but critical final validation step.

### 5. `not a` vs `len(a) == 0`
Both check if a list is empty, but `not a` is more **Pythonic** and slightly faster since it doesn't compute the length. Use `not a` inside the loop for the guard; `len(a) == 0` at the end reads more explicitly as a deliberate final check.

### 6. Encoding Bracket Pairs Cleanly (Optimization Tip)
The three separate `if` checks work correctly, but a cleaner pattern uses a dictionary to encode pairs:
```python
pairs = {')': '(', ']': '[', '}': '{'}
```
This reduces three conditionals to one lookup — making it easier to extend if new bracket types were ever added.

---

## Optimized Version — HashMap for Bracket Pairs

```python
def isValid(self, s: str) -> bool:
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in pairs:                        # closing bracket
            if not stack or stack[-1] != pairs[char]:
                return False
            stack.pop()
        else:
            stack.append(char)                   # opening bracket

    return not stack
```

### Comparison Table

| Approach | Time | Space | Bracket Check Method |
|---|---|---|---|
| Three `if` statements (current) | O(n) | O(n) | Explicit per-type comparison |
| HashMap pairs (optimized) | O(n) | O(n) | Dict lookup — cleaner & extensible |

Both are O(n). The HashMap version is preferred in interviews for its clarity and extensibility.

---

## Test Run

```
s = "([])"

Output → Valid: True
```
