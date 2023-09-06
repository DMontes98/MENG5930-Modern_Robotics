# Imports
from math import * 
import math as m

# Print statements
#print("This is a print statement")

# Data Types
num_int = 3                                                # Integer Number
num_float = 0.50                                           # Float Number
print("Integer Number: " + str(num_int))
print("Float Number: "   + str(num_float))

# Basic Arithmetic
print("Addition and multiplication" , num_int * (num_int + num_float))                  # Addition and multiplication
print("Remainder" , num_int % 3)                                                        # Remainder
print("Max" , max(num_int, 9))                                                          # Max
print("Exponential" , m.exp(num_int))                                                   # Exponential
print('abs function for', -num_int, 'is', abs(-num_int))
print('pow function 4 for', num_int, 'is', pow(num_int, 4))
print('round function for', num_float, 'is', round(num_float))

print('floor function for',num_float, 'is', floor(num_float))
print('ceil function for', num_float, 'is', ceil(num_float))
print('sqrt function for', num_int, 'is', sqrt(num_int))
print('exp function for',num_int, 'is', exp(num_int))


# Strings                                      
university_name = "SLU"                                                                    # String definition
print("The university's name is " + university_name)
print("The first character in the university name is " + university_name[0])  # Select specific characters in string
print("The third character in the university name is " + university_name[2])
print('There are ' + str(num_int) + ' arm robots in the university, ' + str(num_float) + ' of them are broken.')
print('There are', num_int, 'arm robots at',university_name,',', num_float, 'of them are broken.')

# Lists
group_members= ["Cordan", "Hamad", "Daniel", "Nicolas" ]        # Create List
print(group_members[1])                                  # Selecting a particular element in the list
print(group_members[:3])                                 # Using slices to access a range of items in a list
group_members.append("new_member")                               # Append item to list
print(group_members)                                     
group_members.remove("new_member")                               # Remove item 
print(group_members)
group_members.insert(1, "new_member")                            # Insert item in position
group_members.sort()                                     # Sort array
group_members.reverse()                                  # Reverse array
group_members1 = ["Bryan", "Wilfredo"]                  
group_members.extend(group_members1)                      # Extend one list with another
print(group_members)
group_members.pop()                                      # Remove last element in  list
print(group_members.index("Daniel"))                        # Find index of element in list
print(group_members.count("Hamad"))                        # Count number of times a value is repeated
group_members2 = group_members.copy()                     # Copy a list into another
print(group_members)
print(group_members)
group_members.clear()                                    # Remove all items from list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]              # Create nDimensional list
print(matrix)
print(matrix[1][2])                                     # Extract specific element/vector

# Tuples
robotic_engineers = ("Cordan", "Hamad", "Daniel", "Nicolas")  # Create Tuples
print(robotic_engineers[1])
e1, e2, e3, e4 = robotic_engineers                      # Extract elements into multiple variables
print(e1, e2, e3, e4)
robotic_partners = [("Cordan", "Hamad"), ("Jim","Bella")]    # List of tuples
print(robotic_partners)

# Dictionaries
car_info = {                                      # Create Dictionary
    "car_type": "sedan",
    "car_color": "green",
    "engine_type": "V6",
    "brand": "Ford",
    "model": "Mustang",
    "year": 2023

}

print("the car type is " + car_info["car_type"])          # Get particular value from key
print("the car color is " + car_info["car_color"])
print("the car engine is " + car_info["engine_type"])
print("the car brand is " + car_info["brand"])




print(car_info.get("name", "no such object"))    # Get default value if key not found
