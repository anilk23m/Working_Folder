# + operator
first = "hello"
second = "world"

print(first + second)

#* operator - repetition - repeats a string multiple times

# n = 6
# print(n*first)
#
# print(n-first)

# indexing
s = "python is my first language"
v = s.split(" ")
print(v)
print(len(s))
#left to right - positive index starts from 0
#right to left - negative index starts from -1
print(s[0])
print(s[1])
print(s[5])
# print(s[27]) - #string index out of range error
print(s[-1])
print(s[-2])
# print(s[-28])
#if index is out of range - error will give index error

#slicing - extract a portion of the string [start:end:step]
print(s[::])
# membership -
print("python" in s)
print("java" not in s)

# comparison operator - = != < > >= <=

print("Hello" != "hello")
A = 65
Z = 90
a = 97
z = 122
print("apple" < "banana")

#formatting
name = "Anil"
age = 35

print("Name : %s" %name)
print("Age : %d" %age)

# = check the value
# is check the memory address
l = [1,2,3,"hello", True]
# ordered
# mutable
# allows duplicates
# can store mix data types

b = list((4,5,6))
print(l[0:3])
print(b)
print(l[-2:])
l[0] = 100
print(l)
#append, extend, insert methods  - data add to list
l.append("world")
print(l)

x = [4,5,6]
# l.append(x)
l.extend(x)
print(l)

l.insert(0, 200)
print(l)

m = ["this", "is", "first", "join", "method"]
d = " @".join(m)
print(d)




