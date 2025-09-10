'''
    4. Write a function that returns both sum and product of two given numbers.

'''

def sum_prod(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a + b, a * b


try:
    result = sum_prod(3, 5)
    print(f"Sum: {result[0]}, Product: {result[1]}")  
    result = sum_prod(3, '5')  
except Exception as e:
    print(f"The Custom Error: {e}")
