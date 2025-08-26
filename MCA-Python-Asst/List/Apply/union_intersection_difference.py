# 6.2. union(), insertion(), difference() with other sets

set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}


union_AB = set_A.union(set_B)
print(f"The union of set A, B: {union_AB}")

intersection_AB = set_A.intersection(set_B)
print(f"Intersection of A, B is: {intersection_AB}")

difference_AB = set_A.difference(set_B)
print(f"Difference of set A, B is: {difference_AB}")