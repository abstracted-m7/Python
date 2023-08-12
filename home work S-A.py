#Q.1 create a list L1 containing numbers from 15 to 24 (24 exclusive),using LIST COMPREHENSION (do not use list function or usual FOR loop).Sort the list in ascending oreder. Create a new list L2 from L1 using LIST COMPREHENSION.

A = int(input("Enter the starting number: "))
B = int(input("Enter the ending number: "))
# create list L1 containing numbers from 15 to 23 (24 exclusive)
L1 = [num for num in range(A, B)]
# sort L1 in ascending order
L1.sort()
print("The list : ", L1)
# create list L2 using list comprehension
L2 = []
for i, e in enumerate(L1):
    if e % 2 == 1:
        if e > i:
            L2.append(e + i)
        else:
            L2.append(e * i)
print("The new list: ", L2)

# Q.2 let b=[61,25,36,21,58,101,254,200] be a list.Apply the following function(x**2-(x*2))//50 on each element of b.dont use for loop.

list = [61, 25, 36, 21, 58, 101, 254, 200]
b = [(x**2 - (x * 2)) // 50 for x in list]
print("After apply function the new list is : ", b)

# Q.3 "dvoxlnv gl rhv 291 rg droo yv z ivzoob rmgvivhgrmt xlfihv, dfg gsg ncvojd jfid fojfv cvnndfg dfnijf nvdf."
# quistion: create a list of words(all contiguous characters) in the order of their appearnce. Remove newline character(if any) from the list.

my_str = input("Enter the string values: ")
words = my_str.split()
words.sort()
print("After sorting the new list is : ", words)

# Q.4

name = input("Enter the students name: ")
roll = input("Enter the students roll: ")
dict = []
for i in range(len(name)):
    dict[name[i]] = roll[i]
print(dict)
