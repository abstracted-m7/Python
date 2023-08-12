

'''#   @ DATA STRUCTURES  --- SUHANA MA'AM & SURYA SHEKAR SIR 

# Q1. Write a python program that takes two number after that add this two number then show the result..

a=int(input("Enter the first number :  "))
b=int(input("Enter the second number :  "))
c=a+b
print("Sum of two number = ",c)


# Q2. Write a python program multiplication table of a number using loop..

num=int(input("Enter the which number of table you want to show :  "))
print("The multiplication table of ",num,"is : ")
for i in range(0,11):
    c=num*i
    print(num,"*",i,"=",c)


# Q3. Write a python program that sum n natarul number using loop..

num=int(input("Enter the number :  "))
if num==0 or num<0:
    print("Enter a valid positive number.")
else:
    sum=0
    for i in range(1,num+1):
        sum=sum+i
    print("Sum from 1 to {0} = {1}".format(num,sum))

# Q4. Write a python program that show the pattern like this..

#     1
#     1 2
#     1 2 3
#     1 2 3 4

num=int(input("Enter the number of row :  "))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

# Q5. Write a python program that takes 9 numbers in a variable after that it shows in a 3*3 matrix form..

a=int(input("What is the number of rows in metrix : "))
b=int(input("What is the number of columns in metrix : "))
matrix=[]
print("Enter the number of cells = ")
for i in range(a):
    m=[]
    for j in range(b):
        m.append(int(input()))
    matrix.append(m)
print("The result = ")
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=' ')
    print()



# Q6. Write a python program that takes two 3*3 matrix after that add this two matrix after that show the result.


a=int(input("What is the number of rows in metrix : "))
b=int(input("What is the number of columns in metrix : "))
matrix=[]
print("Enter the number of cells = ")
for i in range(a):
    m=[]
    for j in range(b):
        m.append(int(input()))
    matrix.append(m)
print("The result = ")
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=' ')
    print()

a=int(input("What is the number of rows in metrix : "))
b=int(input("What is the number of columns in metrix : "))
mat=[]
print("Enter the number of cells = ")
for i in range(a):
    m=[]
    for j in range(b):
        m.append(int(input()))
    mat.append(m)
print("The result = ")
for i in range(a):
    for j in range(b):
        print(mat[i][j],end=' ')
    print()
print ("Sum of two metrix is = ")
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[i][j]=matrix[i][j]+mat[i][j]
for sum in result:
    print(sum)
'''

# arr=[]
# number=int(input("How many number you want: "))
# for m in range(number):
#     arr.append(int(input()))
# print("The list of array: ",arr)
# a=int(input("Enter the searching number:  "))
# if a in arr:
#     print("This number exist.")
# else:
#     print("This number does not exist.")
# #using insert function
# index=int(input("Allocate the indexing position:  "))
# new_number=int(input("Enter the new number: "))
# arr.insert(index,new_number)
# print("The new list : ",arr)
# #using append function
# new_number=int(input("Enter the new number: "))
# arr.append(new_number)
# print("The new list : ",arr)
# #runtime input value delete
# a=int(input("What number you want to delete:  "))
# arr.remove(a)
# print("The new list: ",arr)
# #indexing value delete
# b=int(input("Allocate the indexing position: "))
# arr.pop(b)
# print("The new list : ",arr)
# #reverse list
# arr.reverse()
# print("The Reverse araay: ",arr)
# #delete all element
# arr.clear()
# print("The new list : ",arr)



a=int(input("Enter the number of rows: "))
b=int(input("Enter the number of column: "))
matrix=[]
print("Enter the values in matrix: ")
for i in range(a):
    m=[]
    for j in range(b):
        m.append(int(input()))
    matrix.append(m)
#print matrixxxxx
for i in range(a):
    for j in range(b):
        print(matrix[i][j],end=' ')
    print()
#row-wise Summation......
for i in range(a):
    sum=0
    for j in range(b):
        sum=sum+matrix[i][j]
    print("Sum of row",i+1,":",sum)