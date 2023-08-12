a = float(input("Enter the magnitude of a vector(in mts) :"))
b = float(input("Enter the magnitude of second vector(in mts) :"))
# t=float(input("Enter the value of angle between row vectors[0,30,45,60,90] : "))

# Value of cos 0,30,45,60,90
cos0 = 1
cos30 = (3**1 / 2) / 2
cos45 = 1 / (2**1 / 2)
cos60 = 1 / 2
cos90 = 0

# Calculate the square
d = a**2
e = b**2

# Calculate vector's value
f = (2 * d * e) * cos60
print("Resulant vector of", a, "and", b, "is :", f)
