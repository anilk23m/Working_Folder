#Project in Python
#Menu
menu = {
    "Pizza" : 40,
    "Pasta" : 50,
    "Burger": 60,
    "Salad" : 70,
    "Coffee": 80
}

print(menu)

#Greet customer
print("Welcome to PYTHON Restaurant")
print("Pizza:", menu["Pizza"])
print("Pasta:", menu["Pasta"])
print("Burger:", menu["Burger"])
print("Salad:", menu["Salad"])
print("Coffee:", menu["Coffee"])

order_total = 0

item_1 = input("Enter the name of item you want to order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to place another order? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of the second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Ordered item {item_2} is not available yet!")
print(f"The total amount of items to pay is {order_total}")
