'''
Q. create pattern :

1
10
101
1010
10101

'''
# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(i):  # Inner loop for printing numbers in each row
        if j % 2 == 0:
            print("1", end="")  # Print 1 for even index
        else:
            print("0", end="")  # Print 0 for odd index
    print()  # Move to the next line after each row
