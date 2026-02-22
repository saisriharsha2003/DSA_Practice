"""
This single program demonstrates:
1. Creating / Accessing Dictionaries
2. Adding / Modifying Items
3. Deleting Items
4. Checking Keys / Values
5. Looping Through Dictionary
6. Copy / Merge
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

student.update({"age":24, "city":"Addanki"})
print(student) # {"name":"Alice","age":24,"city":"india"}
student.update({"name":"Sai", "grade":"A"})
print(student) # {"name":"Sai","age":24,"city":"india","grade":"A"}


# Set default if key not exists

student.setdefault("country", "India")
print(student) # {'name': 'Sai', 'age': 24, 'city': 'Addanki', 'grade': 'A', 'country': 'India'}

# ------------------------------------------------
# 3. Deleting Items
# ------------------------------------------------

# Delete specific key

del student["city"]
print(student) # {'name': 'Sai', 'age': 24, 'grade': 'A', 'country': 'India'}

# Remove and return value

age = student.pop("age")
print(student) # {'name': 'Sai', 'grade': 'A', 'country': 'India'}

# Remove and return last item (Python 3.7+)

last_item = student.popitem()
print(student) # {'name': 'Sai', 'grade': 'A'}

# Remove all items

student.clear()
print(student) # {}

# ------------------------------------------------
# 4. Checking Keys / Values
# ------------------------------------------------

student = {'name': 'Sai', 'age': 24, 'city': 'Addanki', 'grade': 'A', 'country': 'India'}

# Check if key exists

if "name" in student:
    print("Exists") # Exists

# Check if value exists

if 22 in student.values():
    print("Found") 
else:
    print("Not Found") # Not Found

# ------------------------------------------------
# 5. Looping Through Dictionary
# ------------------------------------------------

# Keys only

for key in student.keys():
    print(key, end = " ") # name age city grade country 
print()

# Values only

for value in student.values():
    print(value, end = " ") # Sai 24 Addanki A India 
print()

# Keys and values

for key, value in student.items():
    print(key, value, end = ", ") # name Sai, age 24, city Addanki, grade A, country India, 
print()

# ------------------------------------------------
# 6. Copy / Merge
# ------------------------------------------------

# Shallow copy

copy_dict = student.copy()
print(copy_dict) # {'name': 'Sai', 'age': 24, 'city': 'Addanki', 'grade': 'A', 'country': 'India'}

# Merge dictionaries (Python 3.9+)

d1 = {"a":1}
d2 = {"b":2}
d3 = d1 | d2
print(d3) # {'a': 1, 'b': 2}

# Merge using update

d1.update(d2)
print(d1) # {'a': 1, 'b': 2}



