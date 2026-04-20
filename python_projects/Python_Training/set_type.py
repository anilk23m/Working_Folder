d1 = {"name": "Anil", "role": "QA Lead"}
d2 = {"role": "Project Lead", "city": "Bangalore"}

d3 = d2 | d1
print(d3)

d1 |= d2
print(d1)