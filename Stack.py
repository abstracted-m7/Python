#Write a Python program to organize an element of STACK using the PUSH operation

stack = []


def push():
    data = int(input("How many elements you want to add in stack :"))
    stack.append(data)
    print("Success")


def pop():
    temp = stack[-1]
    stack.pop()
    print(temp, "is deleted.")


def display():
    print(stack)


while True:
    print("Menu")
    print("1-Add elements")
    print("2-Delete elements")
    print("3-Display the stack")
    print("4-Exit from the programm")
    choice = int(input("Enter your choice : "))
    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        print("The programm is ended.")
        break



#2 write a python programm to insert / detete / display / and exited in stack.
# Initializing a stack
stack = []


# # function to display stack
# def display():
#     print(stack)


# # function to delete element from stack
# def pop():
#     temp = stack[-1]
#     stack.pop()
#     print(temp, "is deleted")


# # function to insert element in stack
# def push():
#     data = input("enter data to be insert-")
#     stack.append(data)
#     print("success")


# # menu for stack operations
# while 1:
#     print(" menu ")
#     print("1-push")
#     print("2-pop")
#     print("3-display")
#     print("4-exit")
#     choice = input("enter choice-")
#     if choice == "1":
#         push()
#     elif choice == "2":
#         pop()
#     elif choice == "3":
#         display()
#     elif choice == "4":
#         print("The programm is ended.")
#         break


# # Covert Decimal to Binary Using Stack Operation
# class Stack:
#     def _init_(self):
#         self.items = []

#     def push(self, item):
#         self.items.append(item)

#     def pop(self):
#         return self.items.pop()

#     def size(self):
#         return len(self.items)


# s1 = Stack()
# dec = int(input("Enter the decimal num : "))
# while dec != 0:
#     bin = dec % 2
#     dec = dec // 2
#     s1.push(bin)
# while s1.size() != 0:
#     a = s1.pop()
#     print(a)