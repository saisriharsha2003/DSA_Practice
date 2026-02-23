"""
This single program demonstrates:
1. Creating Tuples
2. Packing and Unpacking
3. Accessing Tuple Elements
4. Deleting Items
5. Checking Keys / Values
6. Looping Through Dictionary
7. Copy / Merge
8. List Comprehension
=================================================
"""

# ------------------------------------------------
# 1. Creating Tuples
# ------------------------------------------------

# Empty Tuple
t = ()

# Tuple with values
t = (1, 2, 3)

# Without Parentheses (Packing)
t = 1,2,3
print(t) # (1, 2, 3)

# Single Element Tuple 
t = (1,)
print(t) # (1,)

# Without comma
t1 = (1)
print(t1) # 1; This is int not tuple

# ------------------------------------------------
# 2. Packing and Unpacking
# ------------------------------------------------

# Packing
t = 10, 20, 30
print(t) # (10, 20, 30)

# Unpacking
a, b, c = (10, 20, 30)
print(a)  # 10

# Extended Unpacking
a, *b = (1, 2, 3, 4)
print(b)  # [2, 3, 4]

# ------------------------------------------------
# 3. Accessing Tuple Elements
# ------------------------------------------------

# Indexing
t = (10, 20, 30)
print(t[0])    # 10

# Negative Indexing
print(t[-1])   # 30

# Slicing
print(t[0:2])  # (10, 20)
