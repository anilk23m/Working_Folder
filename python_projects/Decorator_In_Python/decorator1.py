def wrapper_to_func(func):
    def inner():
        result = func()
        num3 = int(input("Enter the third value? "))
        result = result + num3
        return result
    return inner
@wrapper_to_func
def addition_two_num():
    num1 = int(input("Enter the first value? "))
    num2 = int(input("Enter the second value? "))
    result = num1 + num2
    return result
print(addition_two_num())