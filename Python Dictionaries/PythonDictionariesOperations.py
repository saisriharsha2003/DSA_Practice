"""
This single program demonstrates:
1. Creating / Accessing Dictionaries
2. Adding / Modifying Items
3. Deletion
4. Searching & Counting
5. Sorting & Reversing
6. Copying & Extending
7. List Comprehension
8. Built-in Functions
=================================================
"""

# ------------------------------------------------
# 1. Creating / Accessing Dictionaries
# ------------------------------------------------

# Create empty dictionary

d = {}
d = dict()

# Access value by key

student = {"name":"Alice","age":22}
print(student["name"])   # Alice

# Safe access using .get()

print(student.get("grade", "Not Found"))   # Not Found

# ------------------------------------------------
# 2. Adding / Modifying Items
# ------------------------------------------------

# Add new key-value

student["city"] = "Stockholm"
print(student) # {"name":"Alice","age":22,"city":"stockholm"}

# Update value of existing key

student["age"] = 23 
print(student) # {"name":"Alice","age":22,"city":"stockholm"}

# Update multiple values

student.update({"age":24, "city":"india"})
print(student) # {"name":"Alice","age":24,"city":"india"}
student.update({"name":"Sai", "grade":"A"})
print(student) # {"name":"Sai","age":24,"city":"india","grade":"A"}


# Set default if key not exists

student.setdefault("country", "Sweden")

