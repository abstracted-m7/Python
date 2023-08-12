
# WAP to find the area of a triangle using hron's formula.


#Adding those three input

a= float(input("Enter the Value of first side :  "))
b= float(input("Enter the value of second side : "))
c= float(input("Enter the value of third side : "))

# Calculate the semi_perimeter

s=(a+b+c)/2
print("The semi-perimeter is : ",s)

# Calculate the Area 

area= (s*(s-a)*(s-b)*(s-c))**0.5
print("The area of the triangle is %0.2f"%area)
