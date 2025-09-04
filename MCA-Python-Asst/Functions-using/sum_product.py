'''
    4. Write a function that returns both sum and product of two given numbers.

'''

def sum_and_product(a, b):
    # Edge Case: Check if both arguments are numbers
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a + b, a * b

# Edge Case Testing
try:
    result = sum_and_product(3, 5)
    print(f"Sum: {result[0]}, Product: {result[1]}")  # Valid case
    result = sum_and_product(3, '5')  # Invalid input
except Exception as e:
    print(f"The Custom Error Shows: {e}")

