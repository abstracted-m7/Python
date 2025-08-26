# 4.1. TUPLE UNPACKING

# Basic tuple unpacking
nums = (1, 2)
x, y = nums
print(f"Original tuple: {nums}")
print(f"After unpacking = x: {x}, y: {y}")

# Unpacking mixed types
person_data = ("Alice", 25, "Engineer", True)
name, age, job, is_employed = person_data
print(f"Person data: {person_data}")
print(f"Name: {name} ({type(name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"Job: {job} ({type(job).__name__})")
print(f"Employed: {is_employed} ({type(is_employed).__name__})")


# Using * for collecting multiple elements
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
first, *middle, last = numbers
print(f"Original: {numbers}")
print(f"First: {first}")
print(f"Middle: {middle}")  # This will be a list
print(f"Last: {last}")