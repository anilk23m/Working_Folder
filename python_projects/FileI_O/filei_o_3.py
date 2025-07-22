#with Syntax
with open("file1.txt", "r") as f:
    data = f.read()
    print(data)

with open("file1.txt", "a") as f:
    f.write("this is the 2nd last line\n")
