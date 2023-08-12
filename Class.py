# # instant printing two output..


# class bwu:
#     def __init__(self):
#         print("Manish giri--006")

#     def student(self):
#         print("Ayurved--007")


# here = bwu()
# here.student()


# # define cpu's configar..


# class computer:
#     def __init__(self, cpu, ram):
#         self.cpu = cpu
#         self.ram = ram

#     def configer(self):
#         print("Configer is ", self.cpu, "GEN, with ", self.ram, "GB")


# computer1 = computer("i5", 16)
# computer2 = computer("Ryzen 5", 8)
# computer1.configer()
# computer2.configer()

# #information of students..

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def student(self):
#         print("My name is ", self.name, "and my age is", self.age)

# p1 = Person("John", 36)
# p2 = Person("Manish", 20)
# p3 = Person("Akash", 23)
# p4 = Person("Ayan", 21)
# p5 = Person("Jayanti", 58)

# p1.student()
# p2.student()
# p3.student()
# p4.student()
# p5.student()

# # Find computer adress using class method..

# class computer:
#     pass
# here1 = computer()
# here2 = computer()
# print(id(here1))
# print(id(here2))


# asst 4
# creating node
# class node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class linkedlist:
#     def __init__(self):
#         self.head = None

#     # head _value printing
#     def listprint(self):
#         values = self.head
#         while values is not None:
#             print(values.data)
#             values = values.next

#     # replace between privious head value & new_data
#     def beginning(self, new_data):
#         new_node = node(new_data)
#         new_node.next = self.head
#         self.head = new_node


# # denot the values for node
# list = linkedlist()
# list.head = node("Monday")
# here = node("Tuesday")
# here2 = node("Wednesday")
# # denotes which value after head value
# list.head.next = here
# here.next = here2
# # denot the value for begnning
# list.beginning("Sunday")
# # for print the list
# list.listprint()


# # make some new code

# class student:
#     def __init__(self):
#         self.name = "manish"
#         self.age = 56

#     def insert_1(self):
#         self.name = "tinu"
#         self.age = 90

#     def update(self):
#         self.age = 21

#     def insert_1_update(self):
#         self.name = "prantik"


# # manish's age change
# c1 = student()
# c1.update()
# print(c1.name, c1.age)

# # replace only name {ram to ayan}
# c2 = student()
# c2.name = "ram"
# c2.age = "78"
# m = input("Enter a name: ")
# c2.name = m
# print(c2.name, c2.age)

# # jayanta's detail
# c4 = student()
# c4.name = input("Enter the name: ")
# c4.age = int(input("Enter the age of his/her : "))
# print(c4.name, c4.age)

# # replace tinu to prantik
# c5 = student()
# c5.insert_1()
# c5.insert_1 = c5.insert_1_update
# c5.insert_1_update()
# print(c5.name, c5.age)

# data science
