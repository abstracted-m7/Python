'''
    5. Write the following using recursive functions:
            5.3. power calculation (x ^ n).
'''

def power(x, n):
    # Edge Case: Validate input
    if not isinstance(x, (int, float)) or not isinstance(n, int):
        raise ValueError("Please input positive-integer.")
    
    if n == 0:
        return 1
    elif n < 0:
        return 1 / power(x, -n)
    return x * power(x, n - 1)

# Edge Case Testing
try:
    print(power(2, 3))
    print(power(2, -3))
    print(power(2, 0))
    print(power(2, '3'))
except Exception as e:
        print(f"The Custom Error: {e}")
