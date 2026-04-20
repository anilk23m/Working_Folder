#generator - A generator is special type of function that returns values one at a time instead of all at once.
#it uesed yield instead of return

#regular function - runs completely, returns one result and forgets everything
#generator - pause at each yield, remembers its state, and resumes from where it left off.


def get_number(n):
    result = []
    for i in range(1, n+1):
        result.append(i)
    return result
number = get_number(5)
print(number)
print(type(number))

def get_num_gen(n):
    for i in range(1, n+1):
        yield i
num_gen = get_num_gen(5)
print(num_gen)
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen))
print(next(num_gen)) #stop iteration error when out of range
print(type(num_gen))