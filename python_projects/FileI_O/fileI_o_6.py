with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")


with open("practice.txt", "w") as f:
    data = f.write(new_data)