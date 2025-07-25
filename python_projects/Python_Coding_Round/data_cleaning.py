import json


def clean_data(data):
    # Remove users with missing names
    data["users"] = [user for user in data["users"] if user["name"].strip()]

    # Remove duplicate friends
    for user in data["users"]:
        user["friends"] = list(set(user["friends"]))

    # Remove inactive users
    data["users"] = [user for user in data["users"] if user["friends"] or user["liked_pages"]]

    # Remove duplicate pages
    unique_pages = {}
    for page in data["pages"]:
        unique_pages[page["id"]] = page
    data["pages"] = list(unique_pages.values())

    return data


# Load, clean, and display the cleaned data
data = json.load(open("user_data2.json"))
data = clean_data(data)
json.dump(data, open("user_data2.json", "w"), indent=2)
print("Data cleaned successfully!")