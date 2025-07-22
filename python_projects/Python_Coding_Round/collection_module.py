from collections import Counter
x = Counter (a = 2, x = 3, b = 3, z = 1, y = 5, c = 0, d = -3)
for i in x.elements():
    # print(i)
    print( "% s : % s" % (i, x[i]), end ="\n")

from collections import defaultdict
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d.__missing__('a'))
print(d.__missing__('d'))