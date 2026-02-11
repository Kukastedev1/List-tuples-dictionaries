# 1. Create a tuple with 4 elements
dimensions = (1920, 1080, 720, 480)
print(f"Original tuple: {dimensions}")

# 2. Try to add or remove elements 
try:
    dimensions.append(360) # This will fail
except AttributeError as e:
    print(f"Error when trying to add: {e}")

try:
    del dimensions[0] # This will also fail
except TypeError as e:
    print(f"Error when trying to remove: {e}")

# 3. Create a new tuple by concatenating two tuples
extra_dimensions = (360, 240)
combined_tuple = dimensions + extra_dimensions

# 4. Print the resulting tuple
print(f"Concatenated tuple: {combined_tuple}")# 1. Create a tuple with 4 elements
dimensions = (1920, 1080, 720, 480)
print(f"Original tuple: {dimensions}")

# 2. Try to add or remove elements 
try:
    dimensions.append(360) # This will fail
except AttributeError as e:
    print(f"Error when trying to add: {e}")

try:
    del dimensions[0] # This will also fail
except TypeError as e:
    print(f"Error when trying to remove: {e}")

# 3. Create a new tuple by concatenating two tuples
extra_dimensions = (360, 240)
combined_tuple = dimensions + extra_dimensions

# 4. Print the resulting tuple
print(f"Concatenated tuple: {combined_tuple}")