d1 = {'x': 1, 'y': 2}
d2 = {'y': 3, 'z': 4}

d1.update(d2)
print(d1)

d3 = d1 | d2
print(d3)

d4 = {**d1, **d2}
print(d4)