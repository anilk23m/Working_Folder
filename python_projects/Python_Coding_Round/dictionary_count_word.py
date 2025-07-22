s = "hello world hello everyone"

d_count = {}

for i in s.split():
    d_count[i] = d_count.get(i, 0) + 1
print(d_count)