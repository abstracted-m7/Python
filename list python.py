#list function for one row
list=[[30,40],[50,60]]
print(list)
print(list[0][0]+list[0][1]+list[1][0]+list[1][1])


#list function for sum of matrix
list1=[[2,11],[7,12]]
list2=[[5,2],[9,15]]
list3=[[8,3],[10,42]]
list4=[[9,8],[7,12]]
print(list1)
print("Sum of first row = ",list1[0][0]+list1[0][1]+list1[1][0]+list1[1][1])
print(list2)
print("Sum of second row = ", list2[0][0]+list2[0][1]+list2[1][0]+list2[1][1])
print(list3)
print("Sum of third row = ", list3[0][0]+list3[0][1]+list3[1][0]+list3[1][1])
print(list4)
print("Sum of last row = ", list4[0][0]+list4[0][1]+list4[1][0]+list4[1][1])
print(list1+list2+list3+list4)

# Write a python program that accepts a list from the user and prints the alternate element of the list.
# USING APPEND FUNCTION

my_list=[]

size=int(input("How many elements you  wants to want to enter :  "))
print("Enter",str(size),"elements")
for i in range (size):
    my_list.append(input())
print("The elements of list is : " +str(my_list))
print("Alternate elements are : ")
for i in range(0,size,2):
    print(my_list[i])

#Q2. Write a program that accepts a list of users.Your program should reverse the content of the list and display it. Do not use reverse() method.
# DO NOT USING reverse() FUNCTION

my_list=input("Enter the value for list :  ")
a=my_list[::-1]
print("Reversed list is :",a)

# USING reverse() FUNCTION

my_list=['MANISH',6,'BWU','BCA','PSUC','PS']
my_list.reverse()
print("Reverse list is : "+str(my_list))