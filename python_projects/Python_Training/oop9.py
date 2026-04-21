#Single inheritance - Deriving one or more sub classes from a single base class is called single inheritance
#in single inheritance, we always have only one base class, but there can be n number of sub classes derived from it.
#For example "Bank" is a single base class from where we can derive "AndhraBank" and "StateBank" as subclasses.
#instance method, class method and static method
class Bank:
    cash = 100000000
    @classmethod
    def available_cash(cls):
        print(cls.cash)

class AndhraBank(Bank):
    pass
class StateBank(Bank):
    cash = 200000000
    @classmethod
    def available_cash(cls):
        print(cls.cash+Bank.cash)
a = AndhraBank()
a.available_cash()
s = StateBank()
s.available_cash()

#multiple inheritance - Deriving sub classes from multiple base classes is called multiple inheritance.
#In this type of inheritance, there will be more than one super class and there may be one more sub calsses.
#All the members of the super classes are by default available to sub classes.

class Father:
    def height(self):
        print("Height is 6.0 feet")
class Mother:
    def color(self):
        print("Color is brown")
class Child(Father, Mother):
    def age(self):
        self.age = 9
        print(self.age)

c1 = Child()
c1.color()
c1.height()
c1.age()