#
#
# ## What is a List?
# #list is a built-in, mutable, ordered collection in Python that can hold items of any data type (including mixed types). Lists are defined using square brackets `[]` and support duplicate elements.
#
#
# empty_list = []
# numbers = [1, 2, 3, 4, 5]
# x = [5,6,7,8]
# numbers.append(x)
# print(numbers)
# mixed = [1, "hello", 3.14, True, None]
# nested_list = [[1, 2], [3, 4], [5, 6]]
#
# # Key characteristics (interview talking points): Lists are ordered (maintain insertion order), mutable (can be changed after creation), support 0-based and negative indexing, can hold heterogeneous data types, allow duplicates, and are dynamically sized.
#
#
# ## Accessing Elements
#
# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
#
# print(fruits[0])    # apple (positive indexing)
# print(fruits[-1])     # elderberry (negative indexing)
# print(fruits[1:4])    # ['banana', 'cherry', 'date'] (slicing)
# print(fruits[::-1])   # reversed list
#
#
# ## All List Methods with Examples
#
# ### 1. `append(item)` — Add one item to the end
#
# colors = ["red", "green"]
# colors.append("blue")
# print(colors)  # ['red', 'green', 'blue']
#
# # Interview trap: append adds the ENTIRE object as one element
# colors.append(["yellow", "purple"])
# print(colors)  # ['red', 'green', 'blue', ['yellow', 'purple']]
#
# ### 2. extend(iterable) — Add all items from an iterable individually
#
#
# list_a = [1, 2, 3]
# list_a.extend([4, 5, 6])
# print(list_a)  # [1, 2, 3, 4, 5, 6]
#
# list_a.extend("hi")
# print(list_a)  # [1, 2, 3, 4, 5, 6, 'h', 'i']
#
#
# #**Interview Q:** *Difference between `append()` and `extend()`?*
# #`append()` adds its argument as a single element; `extend()` iterates over the argument and adds each element individually.
#
#
# ### 3. `insert(index, item)` — Insert at a specific position
#
# nums = [10, 20, 40, 50]
# nums.insert(2, 30)
# print(nums)
#
#
# ### 4. `remove(item)` — Remove the FIRST occurrence of a value
#
# letters = ['a', 'b', 'c', 'b', 'd']
# letters.remove('b')
# print(letters)  # ['a', 'c', 'b', 'd'] — only first 'b' removed
#
# # Raises ValueError if item not found
#
# ### 5. `pop(index=-1)` — Remove and RETURN item at index (default: last)
#
# stack = [10, 20, 30, 40]
# last = stack.pop()       # 40
# second = stack.pop(1)    # 20
# print(stack)             # [10, 30]
#
# ### 6. `clear()` — Remove ALL items
#
# data = [1, 2, 3]
# data.clear()
# print(data)  # []
#
# ### 7. `index(item, start, end)` — Return index of first occurrence
#
# animals = ["cat", "dog", "rabbit", "dog"]
# print(animals.index("dog"))       # 1
# print(animals.index("dog", 2))   # 3 (search starts from index 2)
#
# # Raises ValueError if not found
#
# ### 8. `count(item)` — Count occurrences of a value
#
#
# nums = [1, 2, 2, 3, 2, 4]
# print(nums.count(2))  # 3
# print(nums.count(9))  # 0
#
#
# ### 9. `sort(key=None, reverse=False)` — Sort the list IN-PLACE
#
# nums = [5, 2, 8, 1, 9]
# nums.sort()
# print(nums)  # [1, 2, 5, 8, 9]
#
# nums.sort(reverse=True)
# print(nums)  # [9, 8, 5, 2, 1]
#
# # Sort by custom key
# words = ["banana", "apple", "cherryg"]
# words.sort(key=len)
# print(words)  # ['apple', 'banana', 'cherry']
# sorted_word = sorted(words, key=len, reverse=True)
#
# #**Interview Q:** *Difference between `sort()` and `sorted()`?*
# #`sort()` modifies the list in-place and returns `None`. `sorted()` returns a **new** sorted list and leaves the original unchanged.
#
#
# ### 10. `reverse()` — Reverse the list IN-PLACE
#
# nums = [1, 2, 3, 4, 5]
# nums.reverse()
# print(nums)  # [5, 4, 3, 2, 1]
#
# #Alternative: `nums[::-1]` returns a new reversed list without modifying the original.
#
# ## Common Operations (Not Methods, but Frequently Asked)
#
# ### `del` — Delete by index or slice
# nums = [10, 20, 30, 40, 50]
# del nums[1]       # [10, 30, 40, 50]
# del nums[1:3]     # [10, 50]
#
# ### `len()`, `min()`, `max()`, `sum()`
#
# nums = [3, 1, 4, 1, 5]
# len(nums)   # 5
# min(nums)   # 1
# max(nums)   # 5
# sum(nums)   # 14
#
# ### Membership check — `in` / `not in`
#
# print(3 in [1, 2, 3])       # True
# print(9 not in [1, 2, 3])   # True
#
# ### List Concatenation and Repetition
#
# print([1, 2] + [3, 4])   # [1, 2, 3, 4]
# print([0] * 5)            # [0, 0, 0, 0, 0]

#For loop in list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for i in fruits:
    print(i)

n = [10,20,30,40,50]
for i in n:
    print(i*2)

#with index - enumerate() - on list and on string
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)

for i, c in enumerate("Hello", start=1):
    print(i, c)

#zip method - combine two list together in tuple
names = ["Anil", "Ravi", "John"]
marks = [85, 92, 78]
name_mark = zip(names, marks)
print(name_mark)
print(list(name_mark))
for name, mark in zip(names, marks):
    print(f"{name} -> {mark}")

#unpacking list element
first_name, last_name = ["Anil", "Kumar"]
print(first_name)
print(last_name)
first, *rest, last= [1,2,3,4,5] #*args -
print(first)
print(rest)
print(last)


