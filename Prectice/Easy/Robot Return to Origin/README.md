# Judge Route Circle — LeetCode Problem #657

## Problem Statement

A robot starts at the origin `(0, 0)` on a 2D plane. Given a string `moves` containing characters `'U'` (up), `'D'` (down), `'L'` (left), and `'R'` (right), determine if the robot **returns to the origin** after completing all its moves.

**Examples:**
```
Input:  moves = "UD"      →  Output: True   (up then down → back to origin)
Input:  moves = "LL"      →  Output: False  (moved left twice, never returned)
Input:  moves = "UDLR"    →  Output: True   (all four directions cancel out)
Input:  moves = "UUU"     →  Output: False  (odd length → impossible to return)
```

---

## Solution Approach — Direction Map + Coordinate Tracking

```python
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        if len(moves) & 1: return False
        x, y = 0, 0

        dist = {
            "U": ( 0,  1),
            "D": ( 0, -1),
            "L": (-1,  0),
            "R": ( 1,  0)
        }

        for c in moves:
            dx, dy = dist[c]
            x += dx
            y += dy

        return [x, y] == [0, 0]
```

### Core Idea
Track the robot's `(x, y)` position by accumulating directional displacements. If the final position is `(0, 0)`, the robot returned to the origin.

```
U → y+1       D → y-1
L → x-1       R → x+1

Start: (0,0)
Every move shifts x or y by ±1.
Return True only if x==0 AND y==0 at the end.
```

---

### How It Works — Step by Step

**Step 1 — Odd Length Early Exit**
```python
if len(moves) & 1: return False
```
If the number of moves is **odd**, it's mathematically impossible to return to the origin — every move shifts the robot by exactly 1 unit, and returning requires moves to cancel in pairs. This is an O(1) check that short-circuits before any iteration.

> `len(moves) & 1` uses bitwise AND to check the least significant bit. If it's `1`, the length is odd.

**Step 2 — Direction Map**
```python
dist = {"U": (0,1), "D": (0,-1), "L": (-1,0), "R": (1,0)}
```
A dictionary maps each direction character to its `(dx, dy)` displacement vector. This eliminates a chain of `if/elif` statements and enables O(1) lookup per move.

**Step 3 — Simulate Movement**
```python
for c in moves:
    dx, dy = dist[c]
    x += dx
    y += dy
```
Apply each displacement to the running position. Tuple unpacking `dx, dy = dist[c]` extracts both components cleanly in one line.

**Step 4 — Check Origin**
```python
return [x, y] == [0, 0]
```
Return `True` only if both coordinates are zero.

---

### Trace Through `moves = "UDLR"`

| Step | Move | `dx, dy` | `x` | `y` |
|------|------|----------|-----|-----|
| Start | — | — | 0 | 0 |
| 1 | `U` | (0, 1) | 0 | 1 |
| 2 | `D` | (0, -1) | 0 | 0 |
| 3 | `L` | (-1, 0) | -1 | 0 |
| 4 | `R` | (1, 0) | 0 | 0 |

`[0, 0] == [0, 0]` → **`True`** ✅

### Trace Through `moves = "UUU"` (odd length)

`len("UUU") = 3`, `3 & 1 = 1` → **`False`** immediately ✅

---

## Complexity Analysis

| Metric | Value |
|---|---|
| Time Complexity | **O(n)** — single pass through `moves` |
| Space Complexity | **O(1)** — direction map is fixed size (4 entries); only two integers tracked |

---

## Knowledge Gained

### 1. Bitwise Odd Check — `n & 1`
```python
if len(moves) & 1: return False
```
`n & 1` checks the least significant bit — `1` means odd, `0` means even. It's marginally faster than `n % 2 != 0` (no division operation) and is idiomatic in competitive programming. Both are O(1) and correct; `& 1` signals deliberate low-level intent.

### 2. Direction Vector Dictionary
```python
dist = {"U": (0,1), "D": (0,-1), "L": (-1,0), "R": (1,0)}
```
Encoding directions as `(dx, dy)` tuples in a dictionary is the standard pattern for 2D grid movement. It replaces brittle `if/elif` chains with a clean O(1) lookup and makes the code trivially extensible (e.g., adding diagonal moves `"UL": (-1,1)`).

> **Reusable in:** BFS/DFS on grids, robot path simulation, flood fill, island counting, maze solving — any problem involving movement on a 2D grid.

### 3. Tuple Unpacking for Displacement
```python
dx, dy = dist[c]
x += dx
y += dy
```
Unpacking a 2-tuple directly into named variables `dx, dy` is clean and readable. It avoids index access (`dist[c][0]`, `dist[c][1]`) and makes the intent immediately clear. This pattern scales naturally to 3D with `dx, dy, dz`.

### 4. Mathematical Insight — Parity Constraint
For a robot making unit steps on a grid to return to `(0, 0)`:
- U and D moves must be equal in count: `count('U') == count('D')`
- L and R moves must be equal in count: `count('L') == count('R')`

This means the total number of moves must be **even** — a necessary (though not sufficient alone) condition. The odd-length early exit encodes this mathematical truth as a single bitwise check.

### 5. `x, y = 0, 0` vs `x, y = [0, 0]`
```python
x, y = 0, 0       # clean tuple unpacking from literals
x, y = [0, 0]     # works too, but list is unnecessary overhead
```
Both are valid Python. The first form is preferred — no list allocation, reads naturally as "initialize two variables to zero."

### 6. `[x, y] == [0, 0]` vs `x == 0 and y == 0`
```python
return [x, y] == [0, 0]      # current — list comparison
return x == 0 and y == 0     # alternative — direct comparison
```
Both are correct. `x == 0 and y == 0` is marginally faster (no list allocation) and more idiomatic. The list comparison form is fine for readability but creates two temporary lists. In competitive programming the difference is negligible; in production the direct form is preferred.

### 7. Early Exit as a Guard Clause
The odd-length check is a **guard clause** — it filters out a whole class of impossible inputs before the main loop runs. This pattern keeps the main logic clean and avoids wasting O(n) simulation time on inputs that can be rejected in O(1). Always look for mathematical properties that can short-circuit expensive computation.

---

## Alternative — Using `Counter`

```python
from collections import Counter

def judgeCircle(self, moves: str) -> bool:
    c = Counter(moves)
    return c['U'] == c['D'] and c['L'] == c['R']
```

This directly checks the cancellation condition — no coordinate tracking needed. It's arguably the most readable solution and handles the odd-length case implicitly (if counts are unequal, returns False).

| Approach | Time | Space | Style |
|---|---|---|---|
| Direction map + coords (current) | O(n) | O(1) | Simulation, general-purpose |
| Counter comparison | O(n) | O(1) | Declarative, most readable |

---

## Test Run

```
moves = "UDLR"

U → (0,1), D → (0,-1), L → (-1,0), R → (1,0)
Final position: (0, 0)

Output → True
```
