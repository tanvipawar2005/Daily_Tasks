'''
Q. create the following pattern

*******
******
*****
****
***
**
*

'''

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

for i in range(rows):  # Outer loop for rows
    for j in range(rows - i):  # Inner loop for printing stars
        print('*', end='')  # Print stars on the same line
    print()  # Move to the next line after each row
