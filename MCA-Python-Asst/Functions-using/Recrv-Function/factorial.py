'''
    5. Write the following using recursive functions:
            5.1. Factorial of a number

'''

def factorial(n):
    # Edge Case: Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Edge Case Testing
try:
    print(factorial(5))  # Valid case
    print(factorial(-5)) # Invalid case
    print(factorial(0))  # Edge case for factorial(0)
except Exception as e:
    print(f"The Custom Error Shows: {e}")
    
