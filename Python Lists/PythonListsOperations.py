# =================================
# Python List Operations Demo
# =================================

# 1. Creating Lists
numbers = [1, 2, 3, 4, 5]                  # List of integers
fruits = ["apple", "banana", "cherry"]     # List of strings
mixed = [1, "apple", 3.5, True]           # Mixed data types
nested_list = [[1, 2], [3, 4], [5, 6]]    # Nested lists (2D)

# 2. Accessing Elements
print(numbers[0])    # Access first element -> 1
print(numbers[-1])   # Access last element -> 5
print(numbers[1:4])  # Slicing -> [2, 3, 4]
print(numbers[::2])  # Every second element -> [1, 3, 5]

# 3. Adding Elements
numbers.append(6)             # Add single element at end
numbers.extend([7, 8])        # Add multiple elements
numbers.insert(0, 0)          # Insert 0 at index 0
print(numbers)                # [0, 1, 2, 3, 4, 5, 6, 7, 8]

# 4. Removing Elements
numbers.remove(0)             # Remove first occurrence of 0
popped_element = numbers.pop() # Remove last element (8)
popped_index_2 = numbers.pop(2) # Remove element at index 2
print(numbers)                # [1, 2, 4, 5, 6, 7]
numbers.clear()               # Remove all elements
print(numbers)                # []

# 5. Searching and Counting
fruits = ["apple", "banana", "cherry", "apple"]
print(fruits.index("banana")) # Find index -> 1
print(fruits.count("apple"))  # Count occurrences -> 2

# 6. Sorting and Reversing
numbers = [5, 2, 9, 1, 5]
numbers.sort()                # Sort ascending -> [1, 2, 5, 5, 9]
numbers.sort(reverse=True)    # Sort descending -> [9, 5, 5, 2, 1]
numbers.reverse()             # Reverse current order -> [1, 2, 5, 5, 9]
print(numbers)

# 7. Copying Lists
original = [1, 2, 3]
copy_list = original.copy()   # Shallow copy
another_copy = list(original) # Another way to copy
original.append(4)
print(original)   # [1, 2, 3, 4]
print(copy_list)  # [1, 2, 3]

# 8. List Comprehensions
squares = [x**2 for x in range(6)]        # Square of numbers -> [0, 1, 4, 9, 16, 25]
evens = [x for x in range(10) if x % 2 == 0] # Even numbers -> [0, 2, 4, 6, 8]
print(squares)
print(evens)

# 9. Nested Lists
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[1][2])  # Access element 6
for row in matrix:
    for value in row:
        print(value, end=" ")  # Prints all elements in matrix
print()

# 10. Built-in Functions
nums = [1, 2, 3, 4, 5]
print(len(nums))    # 5 -> Number of elements
print(min(nums))    # 1 -> Minimum element
print(max(nums))    # 5 -> Maximum element
print(sum(nums))    # 15 -> Sum of elements
print(any([0, False, 1])) # True -> at least one True element
print(all([0, True, 1]))  # False -> not all elements are True

# 11. Mutable Behavior
a = [1, 2, 3]
b = a          # b references same list as a
b.append(4)
print(a)       # [1, 2, 3, 4] -> changes reflected in a
c = a.copy()   # Independent copy
c.append(5)
print(a)       # [1, 2, 3, 4]
print(c)       # [1, 2, 3, 4, 5]
