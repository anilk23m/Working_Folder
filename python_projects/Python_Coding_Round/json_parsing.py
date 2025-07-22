import json

person_dict1 = {
    "Name": "Anil",
    "age": 12,
    "Children": None
}

person_json = json.dumps(person_dict1)
print(person_json)
print(type(person_json))

#json.dumps() used to convert python dictionary object to json string object

#dict - object
#list,tuple - array
#str - string
#int, float, int - number
#True - true
#False - false
#None - null

person_dict2 = {"name": "Bob",
"languages": ["English", "French"],
"married": True,
"age": 32
}

with open("person.txt", "w") as json_file:
    json.dump(person_dict2, json_file)
#json.dump() - method is used to write dictionary object to a file as json string object

person = '{"name": "Bob", "languages": ["English", "French"]}'
person_dict3 = json.loads(person)
print(person_dict3)
print(type(person_dict3))
#json.loads() - This method takes json string object and converts it to a dictionary object

with open("user_data.json", "r") as f:
    data = json.load(f)
print(data)
print(type(data))
#json.load() - This method takes json file and return a dictionary object