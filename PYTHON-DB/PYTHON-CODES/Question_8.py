
#Question 8: Create a CSV file by entering user-id and password, read and search the password for given userid.

import csv

# Function to create a CSV file with user-id and password
def create_csv_file():
    filename = 'user_data.csv'
    
    # Open the file in write mode
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['User ID', 'Password'])  # Writing header row
        
        # Get number of users to add
        num_users = int(input("How many users would you like to add? "))
        
        for _ in range(num_users):
            user_id = input("Enter user ID: ")
            password = input("Enter password: ")
            writer.writerow([user_id, password])  # Write user-id and password row
    
    print(f"\nUser data has been written to {filename}.\n")

# Function to search for the password by user-id
def search_password():
    filename = 'user_data.csv'
    
    user_id_to_search = input("Enter user ID to search for: ")
    
    # Open the file in read mode
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        
        found = False
        for row in reader:
            user_id, password = row
            if user_id == user_id_to_search:
                print(f"Password for User ID {user_id_to_search}: {password}")
                found = True
                break
        
        if not found:
            print(f"User ID {user_id_to_search} not found.")

# Main function
def main():
    create_csv_file()  # First create the CSV file with user ids and passwords
    search_password()  # Then search for password for a given user-id

# Run the program
if __name__ == '__main__':
    main()
