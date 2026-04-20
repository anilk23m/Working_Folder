#list comprehension using if-else
nums = [1,2,3,4,5,6,7,8,9,10]
labels = ["even" if x %2 == 0 else "odd" for x in nums]
print(labels)

#short-hand if else block
age = 25
status = "adult" if age >= 18 else "minor"
print(type(status))

score = 75
result = "Pass" if score >= 50 else "Fail"
print(result)

#nested if statement -
# # age = int(input("Enter your age: "))
# # has_license = input("Enter if you have license : Yes/No")
#
# if age >= 18:
#     if has_license == "Yes": #false
#         print("You can drive")
#     else:
#         print("Get a license first")
# else:
#     print("you are too young to drive")

#multiple conditions with and, or, not -
age = 25
role = "QA Lead"

#and - both condition should be true
if age >= 18 and role == "QA Lead":
    print("Eligible for the new project")

#or - at least one must be true
browser = "safari"
if browser == "chrome" or browser == "firefox":
    print("supported browser")
else:
    print("unsupported browser")

#not - reverse condition check
is_bug = False
if not is_bug:
    print("No bug found")

test_result = [1,2]
if test_result: #false
    print("Test found")
else:
    print("Test not found")

#in operator in if statement
browser = ["chrome", "firefox", "edge"]
user_browser = "chrome"
if  user_browser in browser:
    print("Chrome is supported")

if user_browser not in browser:
    print("Safari is not supported")

# for loop
tools = ["selenium", "Playwright", "Robot Framework"]
for item in tools:
    print(item)

for i in "PYthon":
    print(i)

config = {"browser":"chrome", "headless": True}
for item in config:
    print(item)

for key, value in config.items():
    print(f"{key}= {value}")
#range -
for i in range(9):
    print(i)

for i in range(1, 11):
    print(i)

for i in range(0, 10, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)
#enumerate -
tools = ["selenium", "Playwright", "Robot Framework"]
for index, tool in enumerate(tools):
    print(f"{index}: {tool}")

for index, tool in enumerate(tools, start=1):
    print(f"{index}: {tool}")