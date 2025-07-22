import json
def load_data(filename):
    with open(filename, "r") as f:
        data = json.load(f)
    return data
data = load_data("user_data.json")
print(data)

def display_users(data):
    print("\nUsers and their connections\n")
    for user in data["users"]:
        print(f"{user['name']} is friends with: {user['friends']} and like pages are {user['liked_pages']}")
    print("\nPages information:\n ")
    for page in data["pages"]:
        print(f"{page['id']} : {page['name']}")
display_users(data)
