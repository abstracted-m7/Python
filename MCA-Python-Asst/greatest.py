# def gretest_num(n1, n2, n3):
#     if n1 > n2 and n1 > n3:
#         return n1
#     elif n2 > n1 and n2 > n3:
#         return n2
#     elif n3 > n1 and n3 > n2:
#         return n3
#     else:
#         return 0

# print(gretest_num(2, 3, 4))

#using short method
def gretest_num(n1, n2, n3):
    return max(n1, n2, n3)
print(gretest_num(2, 3, 4))