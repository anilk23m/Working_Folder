#frozenset -
#A frozen set is an immutable version of set. Once created, you can not add, remove or modify any element.
#Create Frozenset
fs = frozenset([1, 2, 3])
print(fs)

s = {10,20,30}
fs = frozenset(s)
print(fs)

fs = frozenset((10,20,30,40,50))
print(fs)

fs = frozenset("Hello")
print(fs)

teams = set()
teams.add(frozenset(["Anil","Ravi"]))
print(teams)
teams.add(frozenset(["Priya","Kiran"]))
print(teams)
teams.add(frozenset(["Anil","Ravi"]))
print(teams)


