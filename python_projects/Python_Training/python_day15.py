def log_test(test_id, suite, status, *tags, priority="Medium", **metadata):
    print(f"Test ID: {test_id}")
    print(f"Suite: {suite}")
    print(f"Status: {status}")
    print(f"Tags: {tags}")
    print(f"Metadata: {metadata}")
    print(f"Priority: {priority}")
log_test("TC001", "Login Suite","Pass","smoke", "regression","P1", priority="High", tester="Anil", env="Production")

#nonlocal works in nested function -
#nonlocal tells python dont create a new local variable-instead use the variable from the nearest enclosing(outer) function.
def outer(): #url-request type, retry_count
    retry_count = 0
    def inner():#acutal get/post call -
        nonlocal retry_count
        retry_count += 1
        print(retry_count)
    inner()
outer()

#gloabl works at module/file level
#non local works at nested function (encloser)

#lambda function - a lambda is a small, anonymous(nameless) function written in single line. it can take
#any number of arguments but can only have one expression
#lambda argument: expression
def square(n):
    return n*n
print(square(5))

square_res = lambda n: n*n

status = lambda code : "PASS" if code ==200 else "FAIL"
print(status(200))
print(status(400))

for n in range(1, 11):
    print(square_res(n))

