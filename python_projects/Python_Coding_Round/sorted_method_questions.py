nums = [3, 1, 4, 1, 5, 9]
# Output: [9, 5, 4, 3, 1, 1]

sorted_nums = sorted(nums, reverse=True)
print(sorted_nums)

words = ['banana', 'apple', 'kiwi']
# a) ['apple', 'banana', 'kiwi']
# b) ['kiwi', 'apple', 'banana']

sorted_words_by_alphabet = sorted(words)
#sorted method sort the list of string in alphabet order as default
print(sorted_words_by_alphabet)

sorted_words_by_len = sorted(words, key = len)
print(sorted_words_by_len)

people = [('Alice', 25), ('Bob', 20), ('Charlie', 30)]
# Output: [('Bob', 20), ('Alice', 25), ('Charlie', 30)]

sorted_people = sorted(people, key= lambda x:x[1])
print(sorted_people)

nums = (5, 2, 9, 1)
# Output: [1, 2, 5, 9]

nums_sorted = sorted(nums)
print(nums_sorted)

products = [('Pen', 5), ('Notebook', 20), ('Eraser', 2)]
# Output: [('Notebook', 20), ('Pen', 5), ('Eraser', 2)]
sorted_products = sorted(products, key=lambda x : x[1], reverse=True)
print(sorted_products)

d = {'banana': 3, 'apple': 4, 'cherry': 1}
# Output: {'apple': 4, 'banana': 3, 'cherry': 1}
d_sorted = dict(sorted(d.items(), key = lambda x : x[0]))
print(d_sorted)

d = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
# Output: {'Bob': 92, 'Alice': 85, 'Charlie': 78}
d_sorted_v = dict(sorted(d.items(), key = lambda x : x[1], reverse=True))
print(d_sorted_v)

marks = {'A': 60, 'B': 85, 'C': 75, 'D': 90}
# Output: ['D', 'B']
sorted_marks = sorted(marks.items(), key = lambda x:x[1], reverse=True)
print(sorted_marks)
output = []
for i in range(2):
    output.append(sorted_marks[i][0])
print(output)

students = {'Ann': 85, 'Christopher': 92, 'Ben': 78}
# Output: ['Ann', 'Ben', 'Christopher']  # sorted by name length
students_sorted_by_length = sorted(students.items(), key = lambda x: x[0])
print(students_sorted_by_length)

students = [
    {'name': 'Alice', 'score': 82},
    {'name': 'Bob', 'score': 91},
    {'name': 'Charlie', 'score': 77}
]
# Output: sorted by 'score' ascending

students_sorted_key = sorted(students, key = lambda x:x['score'])
print(students_sorted_key)

s = "banana"
# Output: ['a', 'n', 'b']  # a:3, n:2, b:1

d_s = {}
for i in s:
    d_s[i] = d_s.get(i,0)+1
print(d_s)
sorted_ds = sorted(d_s.items(), key = lambda x:x[1], reverse=True)
print(dict(sorted_ds).keys())

dates = ['2024-05-10', '2023-01-15', '2024-01-01']
# Output: ['2023-01-15', '2024-01-01', '2024-05-10']
dates_sorted = sorted(dates)
print(dates_sorted)