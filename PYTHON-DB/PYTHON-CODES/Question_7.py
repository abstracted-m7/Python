
#Question 7: Write a python program to implement a stack using list.

#DS
# Create a class = Stack
class Stack:
    def __init__(self):
        self.stack = []  # List to hold stack elements
    
    # Check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0
    
    # Push an element onto the stack
    def push(self, item):
        self.stack.append(item)
    
    # Pop an element from the stack
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()  # Remove and return the top element
        else:
            return "Stack is empty"
    
    # Peek at the top element without removing it
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"
    
    # Return the size of the stack
    def size(self):
        return len(self.stack)
    
    # Display all value
    def display_stack(self):
        return self.stack

# Create a menu bar
def display_menu():
    print("-------------------------------------")
    print("\nChoose an operation:")
    print("1. Push an element onto the stack")
    print("2. Pop an element from the stack")
    print("3. Peek at the top element")
    print("4. Display Element")
    print("5. Display the size of the stack")
    print("6. Check if the stack is empty")
    print("7. Exit")
    print("-------------------------------------")
    

# Create a object(stack) of Stack class
stack = Stack()

# Main program loop
while True:
    display_menu()
    
    # Get the user's choice
    choice = input("Enter your choice (1-6): ")
    
    if choice == '1':
        # Push operation
        element = int(input("Enter the element to push: "))
        stack.push(element)
        print(f"Element {element} pushed onto the stack.")
    
    elif choice == '2':
        # Pop operation
        popped_element = stack.pop()
        if popped_element == "Stack is empty":
            print(popped_element)
        else:
            print(f"Popped element: {popped_element}")
    
    elif choice == '3':
        # Peek operation
        top_element = stack.peek()
        print(f"Top element: {top_element}")

    elif choice == '4':
        # Display elements
        print(f"The data : {stack.display_stack()}")

    elif choice == '5':
        # Size operation
        print(f"Size of the stack: {stack.size()}")
    
    elif choice == '6':
        # Check if stack is empty
        if stack.is_empty():
            print("The stack is empty.")
        else:
            print("The stack is not empty.")
    
    elif choice == '7':
        # Exit the program
        print("Exiting.....!!")
        break
    
    else:
        print("Invalid choice, please try again.")
