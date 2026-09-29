"""
This single program demonstrates:
1. Creating Tuples
2. Tuples Packing and Unpacking
3. Accessing Tuple Elements
4. Traversing a Tuple
5. Immutability
6. Concatenation
7. Repitition
8. Membership
=================================================
"""

# ------------------------------------------------
# 1. Creating Tuples
# ------------------------------------------------

# Empty Tuple
t = ()

# Tuple with Values
t = (1, 2, 3)

# Without Parentheses (Packing)
t = 1, 2, 3
print(t) # (1, 2, 3)

# Single Element Tuple 
t = (1,)
print(t) # (1,)

# Without comma
t = (1)    # This is int, not tuple
print(t) # 1

# ------------------------------------------------
# 2. Tuples Packing and Unpacking
# ------------------------------------------------

# Packing
t = (10, 20, 30)
print(t) # (10, 20, 30)

# Unpacking
a, b, c = 10, 20, 30
print(a) # 10

# Extended Unpacking
a, *b = (1, 2, 3, 4)
print(b) # [2, 3, 4]

# ------------------------------------------------
# 3. Accessing Tuple Elements
# ------------------------------------------------

# Indexing
t = (10, 20, 30)
print(t[0]) # 10

# Negitive Indexing
print(t[-1]) # 30

# Slicing
print(t[0:2]) # (10, 20)

# ------------------------------------------------
# 4. Traversing a Tuple
# ------------------------------------------------

for i in t:
    print(i, end=" ") # 10 20 30 

print()

for i in range(len(t)):
    print(t[i], end = " ") # 10 20 30 

print()

# ------------------------------------------------
# 5. Immutability
# ------------------------------------------------

# You cannot modify tuple elements.
t = (1, 2, 3)
t[0] = 10   # ❌ Error

# But if tuple contains mutable object:
t = (1, [2, 3])
t[1][0] = 99   # Allowed

# Tuple is immutable, but inner list is mutable.


# ------------------------------------------------
# 6. Concatenation
# ------------------------------------------------

t1 = (1, 2, 3)
t2 = (4, 5, 6)
t3 = t1 + t2
print(t3)  # (1, 2, 3, 4, 5, 6)

# ------------------------------------------------
# 7. Repetition
# ------------------------------------------------

tf = t * 2
print(tf) # (10, 20, 30, 10, 20, 30)

# ------------------------------------------------
# 8. Membership
# ------------------------------------------------

print(20 in t) # True
