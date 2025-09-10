'''
    5. Write the following using recursive functions:
        5.2. nth Fibonacci number
'''
 
def fibonacci(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Please input positive-integer.")

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

try:
    print(fibonacci(3))  
    print(fibonacci(5))
except Exception as e:
    print(f"The Custom Error: {e}")