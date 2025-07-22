#get_name function will return full name and use that function to convert the name to
#upper case and then split the name to list using two decorator

def decor1(func):
    def inner():
        return func().upper()
    return inner

def decor2(func):
    def inner():
        return func().split()
    return inner

@decor2
@decor1
def get_name():
    name = input("Enter first name: ")
    surname = input("Enter surname: ")
    full_name = name + surname
    return full_name

print(get_name())