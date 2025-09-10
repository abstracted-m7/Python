'''
2. Define a function for the area of a rectangle with a default value for breadth.

'''

def area_rect(length, breadth=5):
    if not isinstance(length, (int, float)) or not isinstance(breadth, (int, float)):
        raise ValueError("L & B must be numbers.")
    if length <= 0 or breadth <= 0:
        raise ValueError("L & B must be positive values.")
    return length * breadth


try:
    #Defult breadth
    print(area_rect(10))
    #custom
    print(area_rect(10, 3.65))    
    #invalid 
    print(area_rect(0, 3))    
except Exception as e:
    print(f"The Custom Error: {e}")