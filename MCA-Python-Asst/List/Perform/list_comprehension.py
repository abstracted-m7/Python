# 2.5.Use list comprehension to generate a list of squares of even numbers.

org_list = list(range(1, 10))

# Conditional expression in comprehension
even_odd_labels = ['even' if x % 2 == 0 else 'odd' for x in org_list]
print(f"Even/odd labels: {even_odd_labels}")

# sequence of even numbers 
even_numbers = [x for x in org_list if x % 2 == 0]
print(f"Even numbers: {even_numbers}")

# Basic list comprehension for squares of even numbers
even_squares = [x**2 for x in org_list if x % 2 == 0]
print(f"Squares of even numbers : {even_squares}")

# Nested comprehension (creating a multiplication table)
mult_table = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print(f"3x3 multiplication table: {mult_table}")
