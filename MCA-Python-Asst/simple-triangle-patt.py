# 4.	Program to print patterns using nested loops:
#    *
#    * *
#    * * *
#    * * * *

def triangle(n, row=1):
    if row > n:
        return
    print("* " * row)
    triangle(n, row + 1)
    
triangle(5)