
'''
3. Write a program to:
    a. Create a file named student.txt
    b. Add student name and marks.
    c. Append additional student records without overwrite existing content.
'''
'''
# For check purpose
with open('student.txt', 'r') as file:
    content = file.read()
    print(content)
'''
    
def student_db():
    """
    Manages student records by creating a file, adding initial data,
    and allowing the user to append more records.
    """
    file_name = "student.txt"

    # a. Create and write initial records
    with open(file_name, 'w') as file:
        file.write("Student Name,Marks\n")  # Header
        # b. Add some initial student names and marks
        file.write("Manish,40\n")
        file.write("Avik,38\n")
        print(f"File '{file_name}' created with initial student data.")

    # c. Append additional student records based on user input
    while True:
        try:
            # Get user input for student details
            student_name = input("Enter student name (or 'q' to quit): ")
            if student_name.lower() == 'q':
                break

            marks = int(input(f"Enter marks for {student_name}: "))

            # Append the new record to the file
            with open(file_name, 'a') as file:
                file.write(f"{student_name},{marks}\n")
            print(f"Record for {student_name} added successfully.")

        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")

    print("Student record management complete.")

# Run the program
student_db()