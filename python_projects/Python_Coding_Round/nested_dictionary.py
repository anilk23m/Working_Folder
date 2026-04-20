students = {
    "Alice": {"Math":75, "Science": 80, "English": 85},
    "Bob": {"Math": 60, "Science": 65, "English": 70}
}
# output = {'Alice': 80.0, 'Bob': 65.0}

students_name = list(students.keys())
print(students_name)

students_marks = []
for i in students:
    students_marks.append(list(students[i].values()))
print(students_marks)

output = {}
for i in range(len(students)):
    output[students_name[i]] = sum(students_marks[i])/len(students_marks[i])

print(output)

result = {}
for name, marks in students.items():
    avg = sum(marks.values())/len(marks)
    result[name] = avg
print(result)