import csv
class Item:
    pay_rate = 0.8 #20% discount
    all = []
    def __init__(self, name: str, price: float, quantity):
        #Run validation to the received arguments
        assert price >=0, f"Price {price} is not greater than zero.!!"
        assert quantity >=0, f"quantity {quantity} is not greater than zero.!!"

        #Assign to self object
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"Item('{self.name}', {self.price}, {self.quantity})"
    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
        for item in items:
            Item(
                name = item.get('name'),
                price = float(item.get('price')),
                quantity = int(item.get('quantity')),
            )
    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False



# item1 = Item("Phone", 100, 5)
# item2 = Item("Laptop", 1000, 3)
# item3 = Item("Cable", 10, 5)
# item4 = Item("Mouse", 50, 5)
# item5 = Item("Keyboard", 75, 5)
# print(Item.all)
Item.instantiate_from_csv()
print(Item.all)
print(Item.is_integer(7.5))