while True:
    try:
        x = int(input("Enter the value for x ? "))
    except ValueError:
        print("x is not an integer!!. Please check the value you have given for x")
    except NameError:
        print("x is not defined. Please provide value")
    else:
        break
print(f"x is {x}")