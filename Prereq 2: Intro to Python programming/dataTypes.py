# Imports
import math as m

# Print statements
#print("This is a print statement")

# Data Types
num_int = 2                                             # Integer Number
num_float = 5.0                                         # Float Number
print("Integer Number: " + str(num_int))
print("Float Number: "   + str(num_float))

# Basic Arithmetic
print(num_int * (num_int + num_float))                  # Addition and multiplication
print(num_int % 3)                                      # Remainder
print(max(num_int, 9))                                  # Max
print(m.exp(num_int))                                   # Exponential

# Strings
factory_name = "ABC"                                    # String definition
print("The factory\'s name is " + factory_name)
print("The first character in the factory name is " + factory_name[0])  # Select specific characters in string
print("The third character in the factory name is " + factory_name[2])

# Lists
robot_brands= ["ABB", "KUKA", "FANUC", "Omron" ]        # Create List
print(robot_brands[1])                                  # Selecting a particular element in the list
print(robot_brands[:3])                                 # Using slices to access a range of items in a list
robot_brands.append("UR")                               # Append item to list
print(robot_brands)                                     
robot_brands.remove("UR")                               # Remove item 
print(robot_brands)
robot_brands.insert(1, "UR")                            # Insert item in position
robot_brands.sort()                                     # Sort array
robot_brands.reverse()                                  # Reverse array
robot_brands1 = ["yaskawa", "stabuli"]                  
robot_brands.extend(robot_brands1)                      # Extend one list with another
print(robot_brands)
robot_brands.pop()                                      # Remove last element in  list
print(robot_brands.index("ABB"))                        # Find index of element in list
print(robot_brands.count("ABB"))                        # Count number of times a value is repeated
robot_brands2 = robot_brands.copy()                     # Copy a list into another
print(robot_brands)
print(robot_brands2)
robot_brands.clear()                                    # Remove all items from list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]              # Create nDimensional list
print(matrix)
print(matrix[1][2])                                     # Extract specific element/vector

# Tuples
robotic_engineers = ("Hannah", "Jim", "Bella", "John")  # Create Tuples
print(robotic_engineers[1])
e1, e2, e3, e4 = robotic_engineers                      # Extract elements into multiple variables
print(e1, e2, e3, e4)
robotic_partners = [("Hannah", "John"), ("Jim","Bella")]    # List of tuples
print(robotic_partners)

# Dictionaries
objects_colors = {                                      # Create Dictionary
    "ball": "red",
    "cube": "green",
    "flower": "pink",
    "pyramid": "blue"

}

print("the ball is " + objects_colors["ball"])          # Get particular value from key
print("the cube is " + objects_colors["cube"])

print(objects_colors.get("floer", "no such object"))    # Get default value if key not found
