try:
    x = int(input("Enter the value for x ? "))
    print(f"x is {x}")
except ValueError:
    print("x is not an integer!!. Please check the value you have given for x")
except NameError:
    print("x is not defined. Please provide value")
else:
    print(x * 10)
