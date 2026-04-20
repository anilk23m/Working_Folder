#single argument -
double = lambda x:x*2
print(double(10))

#multiple argument -
add = lambda a,b: a+b
print(add(4,5))

mul = lambda a,b,c : a*b*c
print(mul(10,20,30))

#no argument -
greet = lambda : "Hello world"
print(greet())

#default argument -
power = lambda base, exp=2: base**exp
print(power(2, 3))

#condition -
status = lambda code: "PASSED" if code==200 else "FAILED"
print(status(200))
print(status(400))

#map(), reduce(), filter(), sorted() -
response_time = [100,200,300,400,500,600,700]
#map(function, iterable) - syntax - function can be named function or lambda funtion
#map() - this method applies a function to every item in an iterable and return new iterable
in_second = list(map(lambda rt:rt/1000, response_time))
print(in_second)

def double_num(x):
    return x*2
result = list(map(double_num, response_time))
print(result)

#filter() - keep the item where the lambda function returns true
status_code = [200,301,404,200,500,403,502]
errors = list(filter(lambda code:code >=400, status_code))
print(errors)

#redufce() - applies a function cumulatively to reduce a list to one value
from functools import reduce
numb = [1,2,3,4,5,6]
total = reduce(lambda x,y:x+y, numb)
print(total)

test_resuls = [
    {"name":"test_login", "duration":1.5},
    {"name": "test_research", "duration":0.3},
    {"name": "test_checkout", "duration":2.1},
    {"name": "test_logout", "duration":0.8},
]
print(test_resuls)
sorted_test_res = sorted(test_resuls, key=lambda x:x["duration"])
print(sorted_test_res)

tests = [
    ("test_login", "FAIL", 1.2),
    ("test_research", "PASS", 0.5),
    ("test_checkout", "FAIL", 0.8),
    ("test_logout", "PASS", 0.3),
]
sorted_test = sorted(tests, key=lambda x: x[2])
print(sorted_test)

def print_test_ids(count):
    for i in range(1, count+1):
        print(f"TC-{i}")
print_test_ids(5)


