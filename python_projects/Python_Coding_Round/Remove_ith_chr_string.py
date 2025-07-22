#Given string, remove ith character from the string

#Method 1
s = "hello world"
s1 = ""
for char in s:
    if char != "o":
        s1 += char
print(s1)

#Method 2

s1 = "".join([char for char in s if char != "o"])
print(s1)

#Method 3

s1 = "".join(filter(lambda ch: ch != "o", s))
print(s1)