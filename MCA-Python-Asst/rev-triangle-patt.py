# 5.	Reverse triangle:
#    * * * *
#    * * *
#    * *
#    *

def reverse_triangle(n, row=None):
    if row is None:
        row = n
    if row == 0:
        return
    print("* " * row)
    reverse_triangle(n, row - 1)

reverse_triangle(5)