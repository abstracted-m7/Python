import os
import csv

def create_or_check_file(file_name, headers):
    """Creates a new CSV file with headers if it doesn't exist."""
    if not os.path.exists(file_name):
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print(f"Created new file: {file_name}")

def view_records(file_name):
    """Displays all records from a CSV file."""
    if not os.path.exists(file_name):
        print("File does not exist. Please add records first.")
        return

    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        headers = next(reader)
        print("-" * 40)
        print(f"| {' | '.join(headers)} |")
        print("-" * 40)
        for row in reader:
            print(f"| {' | '.join(row)} |")
        print("-" * 40)

def add_record(file_name, headers):
    """Adds a new record to the CSV file."""
    with open(file_name, 'a', newline='') as file:
        writer = csv.writer(file)
        record = []
        for header in headers:
            value = input(f"Enter {header}: ")
            record.append(value)
        writer.writerow(record)
    print("Record added successfully.")

def edit_record(file_name, headers):
    """Edits an existing record by its unique ID (first column)."""
    records = []
    found = False
    with open(file_name, 'r', newline='') as file:
        reader = csv.reader(file)
        all_rows = list(reader)
        headers = all_rows[0]
        records = all_rows[1:]

    record_id = input(f"Enter the {headers[0]} of the record to edit: ")

    for i, record in enumerate(records):
        if record[0] == record_id:
            print("Current Record:")
            print(f"{' | '.join(record)}")
            print("-" * 20)
            
            for j, header in enumerate(headers):
                new_value = input(f"Enter new {header} (or press Enter to keep old value '{record[j]}'): ")
                if new_value:
                    records[i][j] = new_value
            found = True
            break
    
    if not found:
        print("Record not found.")
        return

    # Write the updated records back to the file
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(records)
    
    print("Record updated successfully.")

def main_menu():
    """Main menu for the management system."""
    while True:
        print("\n*** Data Management System ***")
        print("1. Manage Students")
        print("2. Manage Employees")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            manage_data("students.csv", ["Student_ID", "Name", "Major"])
        elif choice == '2':
            manage_data("employees.csv", ["Employee_ID", "Name", "Department", "Salary"])
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def manage_data(file_name, headers):
    """Handles the sub-menu for a specific data type (students or employees)."""
    create_or_check_file(file_name, headers)
    
    while True:
        print(f"\n--- Managing {file_name.split('.')[0].capitalize()} ---")
        print("1. View Records")
        print("2. Add Record")
        print("3. Edit Record")
        print("4. Back to Main Menu")
        sub_choice = input("Enter your choice (1-4): ")

        if sub_choice == '1':
            view_records(file_name)
        elif sub_choice == '2':
            add_record(file_name, headers)
        elif sub_choice == '3':
            edit_record(file_name, headers)
        elif sub_choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
