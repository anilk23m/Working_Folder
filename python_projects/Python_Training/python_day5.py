person = {"name":"Anil", "age":35, "city":"Bangalore"}
person["salary"] = 1000
print(person)

person.update({"profession": "QA", "Company": "Persistent"})
print(person)

person.update(profession= "QA", Company="Persistent")
print(person)


d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
d3 = d1 | d2
print(d3)
d1 |= d2
print(d1)


#delete
val = person.pop("home", "Not found")
print(val)
last = person.popitem()
print(last)


if "name" in person:
    print(person["name"])
if "name" not in person:
    val = person.pop("name", "Not found")
    print(val)