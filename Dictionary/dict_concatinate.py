
'''
Q2.Write a Python script to concatenate the following dictionaries to create a new one.

Sample Dictionary :

dic1={1:10, 2:20}

dic2={3:30, 4:40}

dic3={5:50,6:60}

Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


'''



# Accepting input for the three dictionaries
dic1 = {}
dic2 = {}
dic3 = {}

# Taking input for dic1
n1 = int(input("Enter the number of items for dictionary 1: "))
for i in range(n1):
    key = int(input(f"Enter key for item {i+1} in dictionary 1: "))
    value = int(input(f"Enter value for key {key}: "))
    dic1[key] = value

# Taking input for dic2
n2 = int(input("\nEnter the number of items for dictionary 2: "))
for i in range(n2):
    key = int(input(f"Enter key for item {i+1} in dictionary 2: "))
    value = int(input(f"Enter value for key {key}: "))
    dic2[key] = value

# Taking input for dic3
n3 = int(input("\nEnter the number of items for dictionary 3: "))
for i in range(n3):
    key = int(input(f"Enter key for item {i+1} in dictionary 3: "))
    value = int(input(f"Enter value for key {key}: "))
    dic3[key] = value

# Concatenating the dictionaries
concatenated_dict = {**dic1, **dic2, **dic3}

# Displaying the result
print("\nThe concatenated dictionary is:", concatenated_dict)
