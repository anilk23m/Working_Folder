a = {"name": "Nikki", "age": 25, "city": "New York"}

rv = a.pop("location", "Key not found")
print(a)
print(rv)

b = {"name": "Nikki", "age": 25, "city": "New York"}
del b["name"]
print(b)

c = {"name": "Nikki", "age": 25, "city": "New York"}
c = {k:v for k,v in c.items() if k != "name"}
print(c)

d = {"name": "Nikki", "age": 25, "city": "New York"}
v = d.popitem()
print(d)
print(v)

