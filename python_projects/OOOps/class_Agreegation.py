class Customer:
    def __init__(self, name, gender, address):
        self.name = name
        self.gender = gender
        self.address = address
    def editProfile(self, new_name, new_city, new_pin, new_state):
        self.name = new_name
        self.address.changeAddress(new_city, new_pin, new_state)
class Address:
    def __init__(self, city, pincode, state):
        self.city = city
        self.pincode = pincode
        self.state = state

    def changeAddress(self, new_city, new_pincode, new_state):
        self.city = new_city
        self.pincode = new_pincode
        self.state = new_state

add = Address("Kolkata", 700516, "WB")
cust = Customer("Nitish", "Male", add)