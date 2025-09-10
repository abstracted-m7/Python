'''
1. Define a function to calculate the square of number ( using positional argument ).

'''

def sqr_num(num):
    if not isinstance(num, (int, float)):
        raise ValueError("Input must be a number.")
    return num ** 2

# Edge Case Testing
try:
    num = int(input("Enter the number: "))
    print(f"Square of {num} is: {sqr_num(num)}")
except Exception as e:
    print(f"The Error: {e}")
