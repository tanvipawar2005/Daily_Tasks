#Q1  Write a Python program and calculate the mean of the below dictionary. Accept student anme as key and in value accept marks

# Accepting student name and marks in a dictionary
students_marks = {}

# Input loop for multiple students
num_students = int(input("Enter the number of students: "))
for i in range(num_students):
    student_name = input("Enter student name: ")
    student_marks = float(input(f"Enter marks for {student_name}: "))
    students_marks[student_name] = student_marks

# Calculating the mean
mean_marks = sum(students_marks.values()) / len(students_marks)

# Printing the result
print("The mean marks are:", mean_marks)
