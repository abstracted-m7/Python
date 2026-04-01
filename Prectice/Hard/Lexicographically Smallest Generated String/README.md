# 3474. Lexicographically Smallest Generated String

## Problem Source

LeetCode Problem **3474 -- Lexicographically Smallest Generated String**

------------------------------------------------------------------------

## Problem Description

You are given:

-   **str1**: A pattern string consisting of characters `'T'` and `'F'`.
-   **str2**: A target substring.

Your task is to generate the **lexicographically smallest possible
string** `result` such that:

-   If `str1[i] == 'T'`, then the substring\
    `result[i : i + len(str2)]` **must equal** `str2`.

-   If `str1[i] == 'F'`, then the substring\
    `result[i : i + len(str2)]` **must NOT equal** `str2`.

If it is impossible to construct such a string, return an **empty
string**.

------------------------------------------------------------------------

## Approach

### 1. Determine Result Length

To allow all substring checks of length `m`, the resulting string must
have length:

`n + m - 1`

Where:

-   `n = len(str1)`
-   `m = len(str2)`

------------------------------------------------------------------------

### 2. Initialize Result

Create an array filled with `'?'` representing **unassigned
characters**.

Example:

    ans = ['?'] * (n + m - 1)

------------------------------------------------------------------------

### 3. Process 'T' Constraints

For every index where:

    str1[i] == 'T'

We **force** the substring starting at `i` to match `str2`.

While assigning:

-   If the position already contains the same character → continue.
-   If it contains a **different character** → return empty string.

------------------------------------------------------------------------

### 4. Fill Remaining Positions

All remaining `'?'` characters are replaced with `'a'` to keep the
string **lexicographically smallest**.

------------------------------------------------------------------------

### 5. Process 'F' Constraints

For every index where:

    str1[i] == 'F'

Check if the substring equals `str2`.

If it matches:

-   Modify the **last available pending position** (`?`) to `'b'`.
-   This ensures the substring becomes different from `str2`.

If no pending position exists → return **empty string**.

------------------------------------------------------------------------

## Python Implementation

``` python
class Solution:

    def generateString(self, str1: str, str2: str) -> str:

        n , m = len(str1), len(str2)
        ans = ['?'] * (n + m - 1)

        # Process 'T'
        for i, b in enumerate(str1):
            if b != 'T':
                continue

            for j, c in enumerate(str2):
                v = ans[i + j]

                if v != '?' and v != c:
                    return ""

                ans[i + j] = c

        prev_ans = ans
        ans = ['a' if c == '?' else c for c in ans]

        # Process 'F'
        for i, b in enumerate(str1):

            if b != 'F':
                continue

            if ''.join(ans[i: i+m]) != str2:
                continue

            for j in range(i + m - 1, i - 1, -1):

                if prev_ans[j] == '?':
                    ans[j] = 'b'
                    break

            else:
                return ""

        return ''.join(ans)


str1 = "TFTF"
str2 = "ab"

obj = Solution()
print("The Result:", obj.generateString(str1, str2))
```

------------------------------------------------------------------------

## Complexity Analysis

### Time Complexity

    O(n × m)

Where:

-   `n = len(str1)`
-   `m = len(str2)`

Both **T and F constraints** require substring checks.

------------------------------------------------------------------------

### Space Complexity

    O(n + m)

For storing the generated result string.

------------------------------------------------------------------------

## Example

### Input

    str1 = "TFTF"
    str2 = "ab"

### Output

    abab

------------------------------------------------------------------------

## Key Concepts Used

-   Greedy Algorithm
-   String Manipulation
-   Constraint Satisfaction
-   Pattern Matching
-   Lexicographical Ordering

------------------------------------------------------------------------

## Knowledge Gained

Through solving this problem:

1.  Learned how to **construct strings under strict constraints**.
2.  Understood **greedy assignment strategies**.
3.  Practiced **conflict detection in string building**.
4.  Implemented **pattern enforcement and avoidance simultaneously**.

------------------------------------------------------------------------

## Real World Applications

### 1. Pattern Matching Systems

Used in **search engines and text processors** where certain patterns
must match or be avoided.

### 2. DNA Sequence Construction

Bioinformatics algorithms often require building sequences with
**mandatory and forbidden patterns**.

### 3. Compiler Design

Pattern validation during **token parsing and syntax checking**.

### 4. Security Validation

Systems ensuring passwords or data fields **avoid specific patterns**.

------------------------------------------------------------------------

## Conclusion

This problem demonstrates how **greedy strategies combined with
constraint validation** can efficiently construct a lexicographically
smallest valid string. It also highlights practical applications in
**pattern matching, data validation, and sequence construction**.
