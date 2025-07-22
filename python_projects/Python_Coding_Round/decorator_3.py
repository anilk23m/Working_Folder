# A decorator is a function that wraps another function to extend its behavior without modifying the original function.

def decorator_function(func):
    def wrapper():
        print("Before func call")
        func()
        print("After func call")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")
say_hello()

#implement log func call using decorator
def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called")
        return func(*args, **kwargs)
    return wrapper

@log_call
def greet():
    print("Hi there!")

greet()
