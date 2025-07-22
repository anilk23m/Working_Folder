s = "abc12xyz345mn7"
temp = ''
res_list = []
for i in s:
  if i.isdigit():
    temp += i
  else:
    if temp:
      res_list.append(temp)
      temp = ''
if temp:
  res_list.append(temp)

print(res_list)
print(len(res_list))
res = max(map(int, res_list))
print(res)