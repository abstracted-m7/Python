
'''
First install the package "pip install mysql-connector-python" 

AND maintain your database which is created in SQL/MySQL/ORACLE any where but the MySQL is better use with in software based tech. 
'''

#import that package
import mysql.connector

# 1. Connect to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",  # <- Write here your database password {e.g.-->mg123}
    database="student_database" # <- Write here your database name {e.g.--> STUDENT_DB} 
)

# 2. Create a cursor object to execute SQL commands
cursor = conn.cursor()

# 3. Create the Student table (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Student (
    student_name VARCHAR(100),
    roll_number INT PRIMARY KEY,
    class VARCHAR(50),
    phone_number VARCHAR(15),
    total_marks INT
)
''')

# Function to display all students
def display_students():
    cursor.execute('SELECT * FROM Student')
    students = cursor.fetchall()
    print("\n--- Student Data ---")
    for student in students:
        print(student)

# Function to add a new student
def add_student():
    student_name = input("Enter student name: ")
    roll_number = int(input("Enter roll number: "))
    class_name = input("Enter class: ")
    phone_number = input("Enter phone number: ")
    total_marks = int(input("Enter total marks: "))
    
    cursor.execute('''
    INSERT INTO Student (student_name, roll_number, class, phone_number, total_marks)
    VALUES (%s, %s, %s, %s, %s)
    ''', (student_name, roll_number, class_name, phone_number, total_marks))
    conn.commit()
    print(f"Student {student_name} added successfully!")

# Function to update a student's details
def update_student():
    roll_number = int(input("Enter roll number of student to update: "))
    student_name = input("Enter new student name (or press Enter to keep unchanged): ")
    class_name = input("Enter new class (or press Enter to keep unchanged): ")
    phone_number = input("Enter new phone number (or press Enter to keep unchanged): ")
    total_marks = input("Enter new total marks (or press Enter to keep unchanged): ")

    update_query = "UPDATE Student SET"
    updates = []

    if student_name:
        updates.append(f" student_name = '{student_name}'")
    if class_name:
        updates.append(f" class = '{class_name}'")
    if phone_number:
        updates.append(f" phone_number = '{phone_number}'")
    if total_marks:
        updates.append(f" total_marks = {total_marks}")

    if updates:
        update_query += " " + ", ".join(updates) + f" WHERE roll_number = {roll_number}"
        cursor.execute(update_query)
        conn.commit()
        print(f"Student with roll number {roll_number} updated successfully!")
    else:
        print("No updates were made.")

# Function to delete a student
def delete_student():
    roll_number = int(input("Enter roll number of student to delete: "))
    cursor.execute('DELETE FROM Student WHERE roll_number = %s', (roll_number,))
    conn.commit()
    print(f"Student with roll number {roll_number} deleted successfully!")

# Main program loop
while True:
    print("\n--- Student Database ---")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        display_students()
    elif choice == '2':
        add_student()
    elif choice == '3':
        update_student()
    elif choice == '4':
        delete_student()
    elif choice == '5':
        break
    else:
        print("Invalid choice, please try again.")

# 7. Close the connection
conn.close()




'''
---------------------------------------------------------------------

Output
--- Student Database ---
1. Display All Students
2. Add New Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 2
Enter student name: Manish Giri
Enter roll number: 10
Enter class: BCA-22-A
Enter phone number: 1234567890
Enter total marks: 92
Student Manish Giri added successfully!

--- Student Database ---
1. Display All Students
2. Add New Student
3. Update Student
4. Delete Student
5. Exit
Enter your choice: 1

--- Student Data ---
('Anup Sah', 10, 'BCA-22-A', '5551234567', 88)
('Manish Giri', 10, 'BCA-22-A', '1234567890', 92)

'''