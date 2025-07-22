import json

data = {
   "name":"Ashish",
   "age":30,
   "Location":{
      "City":"Bangalore",
      "Pin":560100,
      "State":"Karnataka"
   },
   "Language":[
      "Python",
      "Golang",
      "Robot-Frame"
   ],
   "email":"anilk23m@gmail.com",
   "isActive":True,
   "currentJob":None
}

person = '{"name": "Bob", "languages": ["English", "French"]}'

#Using dumps method we will convert python dictionary to json string which will be used to send data in API.
upload_data = json.dumps(data)
print(upload_data)

#using dump, we will be able to write python dictionary to a json file
with open("data.json", "w") as f:
    json.dump(data, f)

#using loads we will be able to parse json string to python dict
data_loads = json.loads(person)
print(data_loads)

#using load we can read json from a file
with open("data.json", "r") as file:
   data_load = json.load(file)
print(data_load["name"])


#json.dumps()	Python dict➝ JSON string
#json.dump()	Python dict➝ JSON file
#json.loads()	JSON string ➝ Python dict
#json.load()	JSON file ➝ Python dict