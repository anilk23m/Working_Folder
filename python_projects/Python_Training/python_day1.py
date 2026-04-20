# # name = "Anil" #str
# # age = 30 #int
# # height = 5.9 #float (decimal)
# # is_active = True #bool (True/False)
# # items = None #None type (absence of value) - this variable exists but has no meaningful value
# #
# # #type
# #
# # print("Hello World!")
# #
# # # print(type(name))
# # print(type(age))
# # print(type(height))
# # print(type(is_active))
# # print(type(items))
#
# # full_name = input("Please enter your full name: ")
# # print(full_name)
#
# # full_mark = int(input("Please enter your full mark: "))
# # print(full_mark)
# # print(type(full_mark))
#
#
# #string -
# greeting = "Hello"
# name = "World"
#
# #concatenate
# # full_greeting = greeting +" "+ name
# # print(full_greeting)
#
# #format string - f string
# print(f"{greeting} {name}!")
#
# #lowercase
# lower_case = greeting.lower()
# print(lower_case)
# # upper_case = greeting.upper()
# # print(upper_case)
#
# #replce method -
# new_greet = greeting.replace("H", "J")
# print(new_greet)
#
# l = greeting.split("@")
# print(l)
#
# #length
# print(len(greeting))
#
# s = " this is "
# print(s.strip())
#
# #title method
# t = "this is the first program in python and we are studying string methods"
# print(t.title())
#
# #capitalize
# print(t.capitalize())
#
# print(t.find("the"))
#
# #count
# c = "this is the first line and this is the second line and this is the third line"
# print(c.count("t"))
#
# print(greeting.isalpha()) #only letters a-z A-Z (space and special char not allowed)
#
# x = "this1"
# print(x.isalnum()) #only alphabet and digits
#
# n = "123"
# print(n.isdigit())
#
# print("HELLO".islower())
#
# #startswith
# #endswith
# print(c.startswith("this"))
# print(c.endswith("line"))
#

s = "***Hello World***"
#strip
normal_s = s.strip("*")
print(normal_s)


#split converts string to list at split separator
x = "hello-world-python"
new_x = x.split("-")
print(new_x)
print(type(new_x))

#join converts list to string
x_s = "-".join(new_x)
print(x_s)


#data types in python  -
# numeric - int, float, complex
# string
# boolean - True/False
# sequential - list , tuple, range
# set
# frozenset
#
# mapping - dict
# NoneType
#
# Mutable and Immutable -
# immutable - cannot be changed after create
# data - username, password (constant) ()
# x = "Hello"
# print(id(x))
# x = x + "World"
# print(id(x))
# id remains different in immutable
#
# lst = [1,2,3]
# print(id(lst))
# lst.append(4)
# print(id(lst))
# id remains same in mutable