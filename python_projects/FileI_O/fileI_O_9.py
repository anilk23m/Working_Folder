c = 0
with open("practice1.txt", "r") as f:
    data = f.read()
    num = data.split(",")
    print(num)
    for i in num:
        if int(i) % 2 == 0:
            c += 1
print(c)
