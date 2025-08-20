#Write a program to calculate the factorial of a number using a while loop.
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(f"The fact of 5 is = {factorial(5)}")


num,fact,i = 5,1,1
while i <= num:
    fact *= i
    i += 1
print(fact)