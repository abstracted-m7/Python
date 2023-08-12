# Q. Section D

import numpy as np

np.random.seed(211)
M = np.random.randint(10, 91, size=(5, 8))

# subtract 5 from all elements of M
M -= 5
print("subtract 5 from all elements of M:\n", M)

# subtract 5 from all elements of third row of M
M[2] -= 5
print("subtract 5 from all elements of third row of M:\n", M)

# subtract 5 from all elements of fifth column of M
M[:, 4] -= 5
print("subtract 5 from all elements of fifth column of M:\n", M)

# divide row 2 and 3 elements of M by 10
a = M[1:3, :]
b = a // 10
print("M after division :\n", b)

# create a copy of M and update its elements
M1 = M.copy()
M1[M1 < 50] = 0
M1[M1 >= 50] = 100
print(
    "M1 after updating values less than 50 to 0 and values greater than or equal to 50 to 100:\n",
    M1,
)

# split M into two nd-arrays of size 3x8 and 2x8
M_3x8 = M[:3, :]
print("Split M into two nd-arrays of size 3x8 :\n", M_3x8)
M_2x8 = M[3:, :]
print("Split M into two nd-arrays of size 2x8 :\n", M_2x8)


# create a list of 8 random integers between 1 and 5
new_row = np.random.randint(1, 6, 8)
# append the new row to M
print("The 8 random's list : :\n", M, ":\n", new_row)

# create a list of 5 random integers between 1 and 5
new_row2 = np.random.randint(1, 6, 5)
# append the new row to M
print("The 5 random's list : :\n", M, ":\n", new_row2)

print("Section D complete.")
