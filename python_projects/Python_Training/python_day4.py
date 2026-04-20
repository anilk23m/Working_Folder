#Tuple
#A tuple is an ordered, immutable collection that can hold any data type and allows duplicate represented by ()
fruits = ("apple", "banana", "cherry")
mixed = (1, "hello", 3.14, True, [1,2])
empty_tuple = ()
single_value = (41,)
n = 1,2,3
print(n)
print(tuple("hello"))
print(tuple([1,2,3,4]))


nums = (1,2,3,2,4,2,5)
print(nums.count(2))
print(nums.index(2))
print(len(nums))
print(sum(nums))
print(max(nums))
print(min(nums))

#sorted method on tuple
sorted_nums = sorted(nums)
print(tuple(sorted_nums))
reverse_sort = sorted(nums, reverse=True)
print(tuple(reverse_sort))

reverse_nums = reversed(nums)
print(tuple(reverse_nums))

#slicing - DYI
slice_num = nums[2:5]
print(slice_num)

for i, fruit in enumerate(fruits):
    print(i, fruit)

enum_obj = enumerate(fruits)
print(enum_obj)
print(tuple(enum_obj))

names = ("Anil", "Ravi", "John")
marks = (85, 92, 78)
zip_name_mark = zip(names, marks)
print(zip_name_mark)
print(tuple(zip_name_mark))

t1 = (1,2,3)
t2 = ("a", "b", "c")
result = list(zip(t1, t2))
print(result)


square = []
for x in range(1, 6):
    square.append(x**2)
print(square)

new_list = [x**2 for x in range(1, 6)] #list comprehension
print(new_list)
#[expression for item in iterator if condition]

evens = [x for x in range(1, 10) if x % 2 == 0]
print(evens)
#print(2%2) - module operator checks remainder

result = (x**2 for x in range(1, 6) if x % 2 == 0)
print(list(result)) #generator data type


