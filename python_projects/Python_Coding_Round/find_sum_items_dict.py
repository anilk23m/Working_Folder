d = {'a': 100, 'b': 200, 'c': 300}

res = sum(d.values())
print(res)

res = sum([d[key] for key in d])
print(res)

res = sum(map(lambda key: d[key], d))
print(res)