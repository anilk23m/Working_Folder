s = "abc12xyz345mn7"
res = sum([int(x) for x in s if x.isdigit()])
print(res)