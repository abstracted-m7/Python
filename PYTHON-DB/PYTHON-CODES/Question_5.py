
#Question 5: Create a binary file with roll number, name and marks. Input a roll number and update the marks.


import pickle

# Sample data: list of tuples containing roll number, name, and marks
students = [
    ( 10, 'Abir', 235),
    ( 11, 'Boby', 245),
    ( 13, 'Amon', 267),
    ( 14, 'Banti', 223)
]

# Create a binary file and store the student data
with open('student_data.dat', 'wb') as file:
    pickle.dump(students, file)

# Function to update marks by roll number
def update_marks(roll_number, new_marks):
    with open('student_data.dat', 'rb') as file:
        students = pickle.load(file)  # Load existing data

    # Search for the student with the given roll number and update marks
    for i, (roll, name, marks) in enumerate(students):
        if roll == roll_number:
            students[i] = (roll, name, new_marks)
            break
    else:
        print("Roll number not found!")
        return

    # Write the updated data back to the binary file
    with open('student_data.dat', 'wb') as file:
        pickle.dump(students, file)
    print(f"Marks for roll number {roll_number} updated to {new_marks}")

# Input roll and new mark
roll_number = int(input("Enter roll number to update marks: "))
new_marks = int(input("Enter new marks: "))

# call the function with the values
update_marks(roll_number, new_marks)

#Display all data of the dat file
print("\nUpdated Student Data:")
with open('student_data.dat', 'rb') as file:
    students = pickle.load(file)
    for roll, name, marks in students:
        print(f"Roll Number: {roll}, Name: {name}, Marks: {marks}")
