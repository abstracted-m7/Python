
# Evaluate number
x=1
print(eval('x+1'))

# Find Area using eval function

# Type a functin: calculateArea(i)

def calculatePerimeter(i):
    return 4*i

def calculateArea(i):
 
    return i*i

expression=input("Type a function:  ")
for i in range (1,5):
    if (expression=='calculatePerimeter(i)'):
        print("If Length is",i,",  Perimeter = ",eval(expression))
    elif (expression=='calculateArea(i)'):
        print("If Length is ", i,", Area = ",eval(expression))
    else:
        print('Wrong Function')
        break


# If we using eval(input()) in our code,it is a good idea to check which variables and method the users can use. You can see which variables and methods are available using dir() method.

from math import*
print(eval('dir()'))


# Passing a square root in dictionary method.

# In dir() function define which calculation use here.

from math import*
names = {'sqrt':sqrt,'power':pow}
print(eval('dir()',names))

# Using Square_root in expression

print(eval('sqrt(16)',names))