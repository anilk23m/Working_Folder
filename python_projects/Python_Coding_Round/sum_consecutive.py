s = 'abc3def5ghi89j'
numb = ''
res = 0

for i in s:
  if i.isdigit():
    numb += i
  else:
    if numb:
      res += int(numb)
      numb = ''
if numb:
  res += int(numb)
print(res)