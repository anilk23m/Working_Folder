def wrapper(func):
    def inner(num1,num2):
        result = func(num1,num2)
        num3 = int(input("Enter the number: "))
        result = result + num3
        return result
    return inner

def wrapper_1(func):
    def inner(num1,num2):
        result = func(num1,num2)
        first_digit = int(str(abs(result))[0])
        return first_digit
    return inner

@wrapper_1
@wrapper
def input_func(num1,num2):
    result = num1 + num2
    return result
print(input_func(8,9))


