def get_testcase_status(testcases, status):
    result = []
    for tc, status in zip(testcases, status):
        result.append(f"{tc} : {status}")
    return result
testcases = ["TC001", "TC002", "TC003", "TC004"]
status = ["Pass", "Fail", "Pass", "Fail"]
result = get_testcase_status(testcases, status)
print(result)

for i in result:
    print(i)

#*args - variable positional arguments -
#when you dont know how many positional arguments will passed. collected as tuple
def total(*numbers):
    print(type(numbers))
    return sum(numbers)
print(total(1,2,3,4,5,6,7,8,9)) #numbers = (1,2,3,4,5,6,7,8,9)-tuple
print(total(4,5,6))

# **kwargs- variable keyword arguments -
#when you dont know how many keyword arguments will be passed. Collected as dict
def show_info(**details):
    print(type(details))
    for key, value in details.items():
        print(f"{key} : {value}")
# show_info(name="Anil", role="QALead", city = "Bangalore")
show_info(role="QALead",name="Anil",  city = "Bangalore")

def square(n):
    return n*n
print(square(5))

#combining different types of argument
# positional argument - *args - keyword arguemnt - **kwargs -
def demo(a, b, *args, city, country="India", **kwargs):
    print(f"a={a}")
    print(f"b={b}")
    print(f"city={city}")
    print(f"country={country}")
    print(f"args={args}")
    print(f"kwargs={kwargs}")
#a, b - required positional arguments must be passed first
#*args - capture any extra positional argument as a tuple
#city - keyword only argument (comes after *args) - must be passed by name
#countr=India keyword argument with default value
#**kwargs - capture any extra keyword arguments as a dictionary.

demo(1, 2, 3, 4, 5, city="Bangalore", company="Persistent", role="QA Lead")

#local scope - variables inside a function are local - can not access outside function
def my_func():
    x = 10
    print(x)
my_func()
# print(x)

#global scope - Variables defined outside function are global
x = 100
def my_func():
    print(x)
my_func()
# print(x)

#global keyword used to modify a global variable inside function
count = 0
def increment():
    global count
    count += 1
increment() # 1
increment() # 2
print(count)