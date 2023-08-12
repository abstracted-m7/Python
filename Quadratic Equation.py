
#Quadratic Equation


# ax2 + bx + c
# Where a,b,c are coefficient and real number and also a not equal 0.
# If a is equal to 0 that equation is not valid quadratic equation.

import cmath

# Input the users value

a=float(input("Enter the value of a : "))
b=float(input("Enter the value of b : "))
c=float(input("Enter the value of c : "))


#calculate the discriminant

d=(b**2)-(4*a*c)

#Find the solutions

solve1=(-b-cmath.sqrt(d))/(2*a)
solve2=(-b+cmath.sqrt(d))/(2*a)

# Print both solutions

print("The solution are {0}and{1}".format(solve1,solve2))