import json
test_config = {
    "project": "Kace cloud",
    "environment": "Production",
    "browser": "chrome",
    "base_url": "https://kacecloud.com",
    "credentials": {
        "username": "admin",
        "password": "admin123"
    },
    "test_suites": ["smoke", "regression", "api"]
}

print(type(test_config))

with open("config.json", "w") as file: #write dict in to json file
    json.dump(test_config, file, indent=4)

with open("config.json", "r") as file: #json file to python dict - read
    config = json.load(file)
    print(config)

#dumps() - loads()
json_string = json.dumps(test_config) #- converts dict to json string
print(type(json_string))
print(json_string)

parce = json.loads(json_string) # - convert json string to python dict
print(parce)
print(type(parce))


