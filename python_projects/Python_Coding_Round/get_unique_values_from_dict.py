test_dict = {'gfg' : [5, 6, 7, 8],
            'is' : [10, 11, 7, 5],
            'best' : [6, 12, 10, 8],
            'for' : [1, 2, 5]}


values = list(sorted(test_dict.values()))
y = []
result = []
for i in values:
    y.extend(i)

for i in y:
    if i not in result:
        result.append(i)
print(result)
