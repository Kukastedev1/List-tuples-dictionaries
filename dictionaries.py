# 1. Create a dictionary with at least 3 key-value pairs
user_profile = {
    "username": "coder_pro",
    "level": 15,
    "is_active": True
}
print(f"Initial dictionary: {user_profile}")

# 2. Add a new key-value pair
user_profile["email"] = "hello@python.org"
print(f"After adding email: {user_profile}")

# 3. Update an existing key-value pair
user_profile["level"] = 16
print(f"After updating level: {user_profile}")

# 4. Retrieve and print a value using a key
current_level = user_profile["level"]
print(f"Retrieved level: {current_level}")

# 5. Delete a key-value pair
del user_profile["is_active"]
print(f"Final dictionary after deletion: {user_profile}")