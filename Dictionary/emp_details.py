
#Q3. Write a Python program to get the key, value and item in a dictionary. Accept the input as a employee details. name,no, ID, dep , des,DOJ, DOB, salary

# Taking input from the user for employee details
name = input("Enter employee's name: ")
no = input("Enter employee's number: ")
ID = input("Enter employee's ID: ")
dep = input("Enter employee's department: ")
des = input("Enter employee's designation: ")
DOJ = input("Enter employee's date of joining (DOJ): ")
DOB = input("Enter employee's date of birth (DOB): ")
salary = float(input("Enter employee's salary: "))

# Storing the details in a dictionary
employee_details = {
    'Name': name,
    'Number': no,
    'ID': ID,
    'Department': dep,
    'Designation': des,
    'DOJ': DOJ,
    'DOB': DOB,
    'Salary': salary
}

# Printing the key, value, and item of the dictionary
print("\nEmployee Details (Key, Value, and Item):")
for key, value in employee_details.items():
    print(f"Key: {key:<12}  Value: {value:<20}  Item: ({key}, {value})")

