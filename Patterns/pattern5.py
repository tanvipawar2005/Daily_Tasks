'''
Q. create pattern :

* * * * * * * 
 * * * * * * 
  * * * * * 
   * * * * 
    * * * 
     * * 
      *
      
'''

# Take the number of rows as input from the user
rows = int(input("Enter the number of rows: "))

for i in range(rows, 0, -1):  # Loop for rows in decreasing order
    print(" " * (rows - i), end="")  # Print spaces
    print("* " * i)  # Print stars with spaces between
