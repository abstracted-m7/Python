'''
    5. Write the following using recursive functions:
        5.2. nth Fibonacci number
'''

def fibonacci(n):
    # Edge Case: Validate input
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")
    
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Edge Case Testing
try:
    print(fibonacci(6))  # Valid case
    print(fibonacci(-1)) # Invalid case
    print(fibonacci(1))  # Edge case for fibonacci(0)
except Exception as e:
    print(f"The Custom Error Shows: {e}")
