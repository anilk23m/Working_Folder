#function -  a function is a reusable block of code that performs specific task. you define it once and call it whenever needed

def greet():
    print("hello, welcome to python function tutorial")
greet()

def greet_name(name):
    print("Hello", name)
greet_name("Avinash")

#multip parameter -
def case_result(test_id, status):
    print(f"{test_id}:{status}")

case_result("TC001", "Pass")
case_result("TC002", "Fail")
case_result("TC003", "Fail")

# - return statement sends a value back to the caller, without return, a function return None

def add_no_return(a, b):
    return a+b
result = add_no_return(1, 2)
print(result)

def add_num_no_return(a,b):
    print(a +b)
result = add_num_no_return(1, 2)
print(result) #- #None

#multiple return
def get_test_summary(results):
    passed = results.count("Pass")
    failed = results.count("Fail")
    total = len(results)
    return passed, failed, total
results = ["Pass", "Fail", "Pass", "Pass", "Fail"]
passed, failed, total = get_test_summary(results)
print(passed, failed, total)

def check_age(age):
    if age < 0:
        return "Invalid age"
    if age >= 18:
        return "Adult"
    return "Minor"
print(check_age(18))
print(check_age(20))
print(check_age(30))
print(check_age(-5))

#positional argument -
def greet_name(greet, name):
    return greet + " " + name
res_greet = greet_name("Avinash", "Good Morning")
print(res_greet.upper())

#keyword argument
def greet_name(greet, name):
    return greet + " " + name
res_greet = greet_name(name="Avinash", greet="Good Morning")
print(res_greet.upper())

#default argument -
def greet(name, greeting = "Hello"):
    print(f"{greeting} {name}!")

greet("Anil")
greet("Anil", "Welcome")

#variable scope - Local, Encloser, Global, Bult in
def variable_scope():
    x = 10
    print(x)
variable_scope()
print(x)


