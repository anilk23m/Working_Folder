#control flow decides which code will run, when and how many times.
#without it, python executes code line by line top to bottom.

#if statement -
age = 17
if age >= 18:
    print("You are old enough to vote!")
#if the condition is True, the indented block runs. if False, it skipped entirely.
#if-else -
else:
    print("You are not eligible to vote!")
#if condition is False - execute the else block

score = 40
if score >= 50:
    print("Test passed")
else:
    print("Test failed")

#if-elif-else - multiple condition -
score = 75
if score >= 90:
    print("Grade : A")
elif score >= 70:
    print("Grade : B")
elif score >= 50:
    print("Grade : C")
else:
    print("Grade : F")
#python checks conditions top to botton and runs the first match only, once match found, rest conditions are skipped
