data_list = [{"name": "Nandini", "age": 20},
             {"name": "Manjeet", "age": 20},
             {"name": "Nikhil", "age": 19}]

res = sorted(data_list, key = lambda x : x["age"])
print(res)

data = {'banana': 3, 'apple': 5, 'cherry': 2}
data = dict(sorted(data.items(), key = lambda x : x[1]))
print(data)

student_marks = {"anandh":60, "bala":90, "chandra":70}

items = list(student_marks.items())
items.sort(key = lambda x:x[1])
print(dict(items))

for i in range(len(items)):
    for j in range(len(items)-1):
        if items[j][1] < items[j+1][1]:
            items[j],items[j+1] = items[j+1],items[j]
print(dict(items))

sorted_items = dict(sorted(student_marks.items(), key = lambda x : x[1]))
print(sorted_items)
