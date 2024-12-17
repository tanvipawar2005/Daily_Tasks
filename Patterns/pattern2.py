'''
Q. create the pattern:

   * 
  * * 
 * * * 
* * * *

'''
# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

for i in range(1, rows + 1):  # Loop for rows in increasing order
    print(" " * (rows - i), end="")  # Print spaces before the stars
    print("* " * i)  # Print stars
