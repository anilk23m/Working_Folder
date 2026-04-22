import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert response.status_code == 200
except requests.exceptions.ConnectionError as e:
    print("got an exception", e)
else:
    print(data)
print(data)
first_user = data[0]
import json
with open ("response_get.json", "w") as f:
    json.dump(first_user, f, indent=4)

payload = {"title": "Test Post", "body": "Hello", "userId": 1}
r = requests.post("https://jsonplaceholder.typicode.com/users", json=payload)
print(r.status_code) #201 - added/created
print(r.json())

response = requests.get("https://jsonplaceholder.typicode.com/users/9999")
print(response.status_code)  # Should be 404
