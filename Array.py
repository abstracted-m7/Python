import array as arr

myarray = arr.array("i", [])
n = int(input("Enter the number of column : "))
for i in range(n):
    value = int(input("Enter the elements : "))
    myarray.append(value)
for i in range(n):
    for j in range(n - i - 1):
        if myarray[j] > myarray[j + 1]:
            temp = myarray[j]
            myarray[j] = myarray[j + 1]
            myarray[j + 1] = temp
print(myarray)


# Find the sum of each row of the matrix of size m * n. For example, the following matrix output will be like this:
#[2  11  7  12]
#[5  2  9  15]
#[8  3  10  42]
#sum of row 1 = 32
#sum of row 2 = 31
#sum of row 3 = 63

a = [    
        [2, 11, 7, 12],  
        [5, 2, 9, 15],  
        [8, 3, 10, 42]  
    ]
rows = len(a) 
cols= len(a[0])
for i in range(0, rows):  
    sumRow = 0  
    for j in range(0, cols):  
        sumRow = sumRow + a[i][j] 
    print("Sum of " + str(i+1) +" row: " + str(sumRow))



#write a program that inputs a string and asks the user to delete a given word from a string.

print("Enter 5 Elements: ")
arr = []
for i in range(5):
    arr.append(input())

print("\nEnter the Value to Delete: ")
val = input()

arr.remove(val)

print("\nThe New list is:")
print(arr)
