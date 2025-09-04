'''
1. Define a function to calculate the square of number ( using positional argument ).

'''

def square_of_number(num):
    # Edge Case: Check if the number is not a valid number (e.g., string, None, etc.)
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number.")
    return num ** 2

# Edge Case Testing
try:
    print("Sqr of 4: ",square_of_number(4))  # Normal case
    print("Sqr of -4:",square_of_number(-4)) # Negative number
    print(square_of_number('abc'))  # Invalid input
except Exception as e:
    print(f"The Custom Error Shows: {e}")

