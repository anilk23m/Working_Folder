import requests

url = "https://httpbin.org/post"

data = {
    "username": "testuser",
    "password": "secure123"
}

response= requests.post(url, data = data)

print("status code", response.status_code)

if response.ok:
    print("Post request successful")
    print("Response Json:", response.json())
else:
    print("Post request failed")
    print("Response text", response.text)