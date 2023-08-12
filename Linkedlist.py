# # Q1:- Write a python program to insert an item in different position ~~ At the beginning / At the end / In between two nodes


# # creating node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # Insert a node at the beginning
#     def insert_at_beginning(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     # Insert a node at the end
#     def insert_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     # Insert a node in between two nodes
#     def insert_between_nodes(self, prev_node_data, data):
#         if not self.head:
#             return
#         new_node = Node(data)
#         current_node = self.head
#         while current_node:
#             if current_node.data == prev_node_data:
#                 new_node.next = current_node.next
#                 current_node.next = new_node
#                 return
#             current_node = current_node.next

#     # printing the linked list
#     def display(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data)
#             current_node = current_node.next


# # Create a empty linked list
# list = LinkedList()

# # Insert values for the beginning nodes
# list.insert_at_beginning("Suman -- 005")
# list.insert_at_beginning("Kuntal -- 004")
# list.insert_at_beginning("Dipayan -- 001")

# # Insert values for the end nodes
# list.insert_at_end("Ayan -- 007")
# list.insert_at_end("Jayanta -- 008")

# # Insert a node in between two nodes
# list.insert_between_nodes("Suman -- 005", "Manish -- 006")

# # Display the linked list
# list.display()


# # Q2:- Write a python program to append n element in a linkedlist and display that.


# # creating node
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     # add a node to the end
#     def append(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             return
#         last_node = self.head
#         while last_node.next:
#             last_node = last_node.next
#         last_node.next = new_node

#     # printing the linkedlist.
#     def display(self):
#         current_node = self.head
#         while current_node:
#             print(current_node.data, end=" ")
#             current_node = current_node.next
#         print()


# # Create an empty linked list
# list = LinkedList()

# # Get the number of elements to append from the user
# n = int(input("Enter the number of elements to add: "))

# # Append n elements to the linked list
# for elements in range(n):
#     data = input(f"Enter element {elements+1}: ")
#     list.append(data)

# # Display the linked list
# print("The linked list is:")
# list.display()


# Q3. create a doubly linkedlist and add an element at the beginning / any specific position / at the end


# create a node
class node:
    def __init__(self, data):
        self.data = data
        self.prv = None
        self.next = None


# create a linkedlist
class linkedlist:
    def __init__(self):
        self.head = None

    def list_print(self):
        values = self.head
        while values is not None:
            print(values.data)
            values = values.next

    # insert an element at the beginning
    def beginning(self, new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prv = new_node
            self.head = new_node

    # insert an element at any position
    def at_any_position(self, new_data, index):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prv = new_node
            self.head = new_node
        else:
            now_node = self.head
            now_index = 0
            while now_index < index - 1 and now_node.next is not None:
                now_node = now_node.next
                now_index += 1
            if now_node.next is None:
                now_node.next = new_node
                new_node.prv = now_node

            else:
                new_node.next = now_node.next
                now_node.next.prv = new_node
                now_node.next = new_node
                new_node.prv = now_node

    # insert an element at the end
    def at_the_end(self, new_data):
        new_node = node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            end_node = self.head
            while end_node.next is not None:
                end_node = end_node.next
            end_node.next = new_node
            new_node.prv = end_node


# add values in the  linkedlist
list = linkedlist()
list.head = node(1)
n1 = node(2)
n2 = node(3)
n3 = node(4)
list.head.next = n1
n1.next = n2
n2.next = n3
print("The list is: ")
list.list_print()
print("After add an element at the beginning :")
list.beginning(5)
list.list_print()
print("after add an element at any position: ")
list.at_any_position(9, 3)
list.list_print()
print("After add an element at the end: ")
list.at_the_end(30)
list.list_print()



#4. Write a program in Python to organize a Singularly linked list
class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Singly_Linkedlist:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printvalue = self.headval
        while printvalue is not None:
            print(printvalue.data)
            printvalue = printvalue.next


list = Singly_Linkedlist()
list.headval = node("x")
e2 = node("M")
e3 = node("Z")
list.headval.next = e2
e2.next = e3
list.listprint()


