#exception handling - An exception is an error that occurs during program execution, without handling, it crashes your code.
#exception handling lets you catch errors gracefully and keep your program running.

#syntax - try and except

try:
    result = 10/0
except ZeroDivisionError:
    print("Something went wrong/zero division not possible")

try:
    num = int(input("Enter a number: "))
    result = 100/num
    print(result)
except ValueError:
    print("this is not the valid number")
except ZeroDivisionError:
    print("can not divide by zero")

try:
    num = int("hello")
except (ValueError, TypeError) as e:
    print(e)

#else block - when no exception, else block execute

try:
    result = 10/2
except ZeroDivisionError:
    print("zero division error")
else:
    print(result)

try:
    num = int("hello")
    result = 100/num
    print(result)
except (ValueError, TypeError, ZeroDivisionError) as e:
    print(e)
else:
    print(result)
finally:
    print("this step always run")

#finally block will execute irrespective of exception
#try block code runs -
#if error -> jump to matching except block
#if no error -> jumps to else block
#finally block always run (error or no error)