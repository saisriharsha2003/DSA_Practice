"""
This single program demonstrates:
1. Access & Update
2. Insertion
3. Deletion
4. Searching & Counting
5. Sorting & Reversing
6. Copying & Extending
7. List Comprehension
8. Built-in Functions
=================================================
"""

# ------------------------------------------------
# 1. ACCESS & UPDATE OPERATIONS
# ------------------------------------------------
arr = [10, 20, 30, 40, 50]

# O(1) Access by index
print(arr[0])        # First element
print(arr[-1])       # Last element

# O(1) Update by index
arr[1] = 25
print(arr)           # [10, 25, 30, 40, 50]

# O(k) Slicing (creates new list)
slice_arr = arr[1:4]
print(slice_arr)     # [25, 30, 40]

# ------------------------------------------------
# 2. INSERTION OPERATIONS
# ------------------------------------------------

# O(1) Amortized append
arr.append(60)
print(arr)

# O(n) Insert at beginning (shifts elements)
arr.insert(0, 5)
print(arr)

# O(n) Insert at middle
arr.insert(3, 35)
print(arr)

# ------------------------------------------------
# 3. DELETION OPERATIONS
# ------------------------------------------------

# O(1) Pop last element
last = arr.pop()
print("Popped:", last)
print(arr)

# O(n) Pop from specific index
middle = arr.pop(3)
print("Removed:", middle)
print(arr)

# O(n) Remove by value (search + shift)
arr.remove(25)
print(arr)

# O(n) Clear entire list
temp = [1, 2, 3]
temp.clear()
print(temp)   # []

# ------------------------------------------------
# 4. SEARCHING & COUNTING
# ------------------------------------------------
nums = [1, 2, 3, 2, 4, 2, 5]

# O(n) Linear search
print(3 in nums)      # True

# O(n) Index of first occurrence
print(nums.index(2))  # 1

# O(n) Count occurrences
print(nums.count(2))  # 3

# ------------------------------------------------
# 5. SORTING & REVERSING
# ------------------------------------------------
data = [5, 1, 4, 2, 3]

# O(n log n) In-place sort
data.sort()
print(data)

# O(n log n) Sorted copy (new list)
new_sorted = sorted(data, reverse=True)
print(new_sorted)

# O(n) Reverse list
data.reverse()
print(data)

# ------------------------------------------------
# 6. COPYING & EXTENDING
# ------------------------------------------------
a = [1, 2, 3]

# O(n) Copy list
b = a.copy()

# Modifying original does not affect copy
a.append(4)
print("Original:", a)
print("Copy:", b)

# O(m) Extend list
a.extend([5, 6, 7])
print(a)

# O(n+m) Concatenation (creates new list)
c = a + b
print(c)

# ------------------------------------------------
# 7. LIST COMPREHENSION
# ------------------------------------------------

# O(n) Create new list
squares = [x * x for x in range(6)]
print(squares)

# O(n) Conditional comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

# ------------------------------------------------
# 8. BUILT-IN FUNCTIONS
# ------------------------------------------------
values = [3, 7, 1, 9, 4]

print(len(values))     # O(1)
print(min(values))     # O(n)
print(max(values))     # O(n)
print(sum(values))     # O(n)

# any(): True if at least one element is True
print(any([0, False, 5]))

# all(): True if all elements are True
print(all([1, True, 3]))

