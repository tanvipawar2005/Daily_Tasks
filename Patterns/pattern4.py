'''
Q. create pattern:

    0
   01
  010
 0101

'''

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):  
    print(" " * (rows - i), end="")# Print spaces for alignment

    for j in range(i):
        print(j % 2, end="")  # Print 0 if even, 1 if odd
    
    print()  # Move to the next line after each row
