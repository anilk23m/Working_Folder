#Nested Function
def outer(x):
    def inner(y):
        return x+y
    return inner

add_five = outer(5)
result = add_five(6)
print(result)

#Pass function as argument
def add(x,y):
    return x+y
def calculate(func, x,y):
    return func(x,y)
result = calculate(add, 4,6)
print(result)

#Return a function as a value
def greetings(name):
    def hello():
        return "Hello " + name + "!"
    return hello
greet = greetings("Atlasian")
print(greet())

#python decorator takes a function, adds some functionality and returns it.
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
def ordinary():
    print("I am ordinary")
decorated_func = make_pretty(ordinary)
decorated_func()

