'''
Question 4: Create a binary file with name and roll number.
Search for a given roll number and display the name,
if not found display appropriate message.
'''

#import the reqire package
import pickle

# Define the binary file name
file_name = 'student_data.dat'

# Create a list of student records (name, roll number, marks)
students = [
    ('Abir', 10),
    ('Boby', 11),
    ('Amon', 13),
    ('Banti', 14)
]

# Write the student records to a binary file
with open(file_name, 'wb') as file:
    pickle.dump(students, file)

# Function to search for a roll number
def search_roll_number(roll_number):
    with open(file_name, 'rb') as file:
        students = pickle.load(file)  # Load the student records
        # Search for the roll number
        for name, roll in students:
            if roll == roll_number:
                return name
        return None  # Return None if roll number is not found

# Input roll number to search
print("------------------------------------------")
search_roll = int(input("Enter roll number to search: "))

# Search and display result
name = search_roll_number(search_roll)
if name:
    print(f"Student Name: {name}")
else:
    print("Roll number not found.")
print("------------------------------------------\n")



#if require to convert a 'bat' file to 'txt' then ->

# Read the data from the binary .dat file
with open('student_data.dat', 'rb') as file:
    students = pickle.load(file)

# Write the data to a text file
with open('student_data.txt', 'w') as file:
    for name, roll in students:
        file.write(f"Name: {name}, Roll Number: {roll}\n") #declear the structure of stored data

print("Binary file data has been written to student_data.txt.")
print("---------------------------------------------\n")


#if you want to show all data from 'bat' & 'txt' file->

# binary file (.bat)
print("------------------------------------------")
print("\nContents of the binary file:")
with open('student_data.dat', 'rb') as file:
    students = pickle.load(file)
    for name, roll in students:
        print(f"Name: {name}, Roll Number: {roll}")
print("------------------------------------------\n")


#txt file (.txt)
print("------------------------------------------")
print("\nContents of the text file : ")
with open('student_data.txt', 'r') as file:
    for line in file:
        print(line.strip())
print("------------------------------------------")



