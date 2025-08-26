# 7. Use set Comprehension to find squares of numbers divisible by 3

squares_div_by_3 = {x**2 for x in range(1, 13) if x % 3 == 0}
print(f"Range 1-20, squares of numbers divisible by 3:")
print(f"Numbers divisible by 3: {[x for x in range(1, 13) if x % 3 == 0]}")
print(f"Their squares: {squares_div_by_3}")