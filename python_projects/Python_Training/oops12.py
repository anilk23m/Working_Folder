#Polymerphism - if a variable, object or method exhibits different behavior in different context, called polymerphism.
#duck typing -
#method overloading
#method overriding
#operator overloading

class Duck:
    def talk(self):
        print("Quack, quack!")

class Human:
    def talk(self):
        print("Hi, Hello!")

def call_talk(obj):
    obj.talk()

x = Duck()
call_talk(x)

y = Human()
call_talk(y)
#
# Method overriding - repeat same name
# method overloading - one method but does more then one action
# operator overloading - one operator but does more then one action
# + - __add__()
# print(2+5)  - __add__(2,5)
# - - __sub__()
# * - __mul__()

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def __mul__(self, other):
        return self.salary*other.days
class Attendance:
    def __init__(self, name, days):
        self.name = name
        self.days = days
x1 = Employee("Xavier", 10000)
x2 = Attendance("Xavier", 5)
print("This month salary is", x1*x2)