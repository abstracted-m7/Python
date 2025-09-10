'''
    3. Define a function using keyword arguments to print employee details.

'''

def emp_details(**employee_info):
    if not employee_info:
            raise ValueError("Employee details is empty.")
    for key, value in employee_info.items():
        print(f"{key}: {value}")

# Edge Case Testing
try:
    emp_details(name="MG", age=22, role="SDE-I")
    emp_details()  # No data
except Exception as e:
    print(f"The Custom error: {e}")