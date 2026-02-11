# 1. Create a list of 5 fruits
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
print(f"Original list: {fruits}")

# 2. Add a new fruit to the end of the list
fruits.append("Fig")
print(f"After adding Fig: {fruits}")

# 3. Remove the first fruit in the list
# We use pop(0) to remove by index, or fruits.remove(fruits[0])
removed_fruit = fruits.pop(0)
print(f"After removing {removed_fruit}: {fruits}")