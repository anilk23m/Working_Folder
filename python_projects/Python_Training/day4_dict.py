#dictionary data type -
# A dictionary is unordered(before 3.5) and ordered after 3.7+, mutable collection of key-value pair

person = {"name":"Anil", "age":35, "city":"Bangalore"}
print(person)
print(person["name"])
print(person["age"])
print(person["city"])

p = {}
p["name"] = "Raju"
p["age"] = 35
p["city"] = "Bangalore"
print(p)

d1 = dict(a=1, b=2, c=3)
print(d1)

d2 = dict([("a",1), ("b",2), ("c",3)])
print(d2)

print(person.keys())
print(person.values())
print(person.items())
print(person.get("name"))
print(person.get("city"))
print(person.get("salary", 0))








