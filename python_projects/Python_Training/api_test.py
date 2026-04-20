import requests
try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    if response.status_code == 200:
        print(response.json())

except requests.exceptions.ConnectionError:
    print("Connection Error")
