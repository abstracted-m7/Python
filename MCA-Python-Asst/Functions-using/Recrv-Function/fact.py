'''
    5. Write the following using recursive functions:
            5.1. Factorial of a number

'''

def factorial(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Please input positive-integer.")
    
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Edge Case Testing
try:
    print(factorial(5))  
    print(factorial(-5)) 
except Exception as e:
    print(f"The Custom Error: {e}")
    