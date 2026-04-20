person = {"name": "Anil", "role": "QA Lead", "city": "Bangalore"}

print(person.get("name"))
print(person.get("role"))
print(person.get("salary", "key not exist")) #key not exist

if person.get("salary") == None:
    person["salary"] = "key not exist"

d = {"a": 1, "b": 2}
d.clear()
print(d)

d = {"a": 1, "b": [2,3]} #1530804624704
#a - 100
#b - 200
d2 = d.copy() #shallow copy will give - 1530804568640
#a - 100
#b - 200
print(id(d))
print(id(d2))
d2["b"] = [5,6]
print(d2["b"])
print(d)
#new dictionary object is new, but all the values inside points to same object in memory
print(id(d["a"]))
print(id(d2["a"]))
# outer object will have different memory address but values inside will point to same object address in memory

#fromkeys() - creates a new dictionary with keys from an iterable
key = ["name", "age", "city"]
d_key = dict.fromkeys(key, "unknown")
print(d_key)

person = {"name": ["Anil", "Avinash"], "role": ["QA Lead", "Manager"], "city": ["Bangalore", "Kolkata"]}
print(person["name"][1])
person["name"].append("Raju")
print(person)
person["city"] = "Mumbai"
print(person)
person["active"] = True
print(person)

#setdefault() - returns value if key exists, otherwise insert key with default value
l = {"name": "Anil"}
v = l.setdefault("name", "Unknown")
print(v)
v2 = l.setdefault("role", "QA Lead")
print(v2)

print("name" in l)


