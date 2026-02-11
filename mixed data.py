# 1. Create a list of dictionaries representing students
students = [
    {
        "name": "Alice",
        "age": 20,
        "subjects": ["Math", "Physics"]
    },
    {
        "name": "Bob",
        "age": 22,
        "subjects": ["Biology", "Chemistry"]
    },
    {
        "name": "Charlie",
        "age": 21,
        "subjects": ["History", "Art"]
    }
]

# 2. Print name, age, and subjects for each student
for student in students:
    print(f"Student: {student['name']} | Age: {student['age']}")
    print(f"Subjects: {', '.join(student['subjects'])}\n")

# 3. Modify a student's subject list (Alice adds Computer Science)
students[0]["subjects"].append("Computer Science")

# Remove a subject (Bob drops Chemistry)
students[1]["subjects"].remove("Chemistry")

print("--- After Modifications ---")
print(f"Alice's updated subjects: {students[0]['subjects']}")
print(f"Bob's updated subjects: {students[1]['subjects']}")