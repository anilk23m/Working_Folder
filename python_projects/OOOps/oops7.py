# When one class derives the properties and methods of another class
#types of inheritance - 1. Single inheritance 2. Multi-level inheritance 3. Multiple inheritance

class Car:
    @staticmethod
    def start():
        print("car started...")
    @staticmethod
    def stop():
        print("car stopped...")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

class Fortuner(ToyotaCar):
    def __init__(self, engine_type, name):
        self.type = engine_type
        super().__init__(name)

car1 = ToyotaCar("Fortuner")
car2 = Fortuner("Diesel", "Prius")
print(car1.name)
car1.start()
car2.start()
print(car2.name)

