'''
    3. Define a function using keyword arguments to print employee details.

'''

def print_employee_details(**employee_info):
    # Edge Case: Ensure that employee details are given
    if not employee_info:
        raise ValueError("Employee details cannot be empty.")
    
    for key, value in employee_info.items():
        print(f"{key}: {value}")

# Edge Case Testing
try:
    print_employee_details(name="Manish", age=22, role="SDE-I")  # Valid data
    print_employee_details()  # No data
except Exception as e:
    print(f"The Custom error shows: {e}")
