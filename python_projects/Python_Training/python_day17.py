#decorator - a decorator is a function that takes another function as argument, add extra behavior and returns a new function -
#function as argument -


def greet():
    return "Hello world"

say_hello = greet #- function is assigned to another variable
print(say_hello())

def call_func(func): #function passed as argument
    print(func())
call_func(greet)

#without decorator
def say_hello():
    print("Hello Anil")
say_hello()

#i want to add behavior before and after function

def say_hello():
    print("Hello Anil")
print("Before calling say_hello()")
say_hello()
print("After calling say_hello()")

#now will use decorator
def my_decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper
@my_decorator
def say_hello():
    print("Hello Anil")

say_hello = my_decorator(say_hello) #my_decorator function receives say_hello as func
#then wrapper adds functionality - before calling and call the function and after calling statement
#it returns wrapper
#my_decorator_res now points to wrapper
#when you call my_decorator() - it actually calls wrapper() and which again calls original say_hello inside it
print(say_hello())


def my_add_decorator(func):
    def wrapper(x,y):
        print("Before calling the function", func.__name__)
        result = func(x,y)
        print(result)
        print("After calling the function", func.__name__)
        return result
    return wrapper

@my_add_decorator
def adding_function(a,b):
    return a+b
adding_function(3,4)

#in python function is also object - can be assigned to variable or can be passed as argument
#a function can return another function
def outer():
    def inner():
        return "i am the inner function!"
    return inner #returning the function, not calling it
res = outer() # res is now the inner functino - res = inner
print(res) # i am the inner function!

def factory():
    def vending_machine():
        return "here is your machine"
    return vending_machine
result = factory() #vending machine inner function object vending machine function obj
print(result()) #execute inner function object
