'''
    2. Define a function for the area of a rectangle with a default value for breadth.

'''

def area_of_rectangle(length, breadth=5):
    # Edge Case: Check if both length and breadth are valid numbers
    if not isinstance(length, (int, float)) or not isinstance(breadth, (int, float)):
        raise ValueError("Length and breadth must be numbers.")
    if length <= 0 or breadth <= 0:
        raise ValueError("Length and breadth must be positive values.")
    
    return length * breadth

# Edge Case Testing
try:
    print(area_of_rectangle(10))       # Default breadth case
    print(area_of_rectangle(10, 3))    # Custom breadth case
    print(area_of_rectangle(0, 3))     # Invalid length
except Exception as e:
    print(f"The Custom Error Shows: {e}")

