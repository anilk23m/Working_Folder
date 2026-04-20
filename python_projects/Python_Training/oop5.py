#getter & setter (accessor & mutator)
#instance methods are the methods which act upon the instance variables of the class. Instance methods are bound to instance.
#Since instance variables are available in the instance, instance method need to know the memory address of the instance.
#This is provided through self variable.

# Instance methods are of two types - accessor method and mutator methods.
#Accessor method simply access or read data of the variables. They dont modify the data in the variable.
#Accessor method are generally written in the form of getXXX() and he

# def getName(self):
#     return self.name

#here getName() is the accessor method since it is reading and returning the value of "name" instance variable.
#Mutator methods are the methods which not only read the data but also modify them. They are written in the form setXXX().
#hence the are also called setter method.

# def setName(self, name):
#     self.name = name

class Student:
    #mutator method
    def setName(self, name):
        self.name = name

    #accessor method
    def getName(self):
        return self.name

    def setMark(self, mark):
        self.mark = mark

    def getMark(self):
        return self.mark

n = int(input("Enter number of student: "))
i = 0
while i < n:
    s = Student()
    name = input("Enter your name: ")
    s.setName(name)
    marks = int(input("Enter your marks: "))
    s.setMark(marks)

    print("Hi", s.getName())
    print("Your Mark", s.getMark())
    i += 1
    print("=======================================")

#Class Methods -
#Class methods act on class level. Class methods are the methods which fact on the class variables or static variables.
#These methods are written using @classmethod decorator above them.
#By default the first parameter for class methods is "cls" which refers to the class itself.
#cls.var is the format to refer to the class variable.
#These class methods are generally called using the classname.method()

class Bird:
    wings = 2 #class variable

    @classmethod
    def fly(cls, name):
        print(f"{name} fly with {cls.wings} wings.")

Bird.fly("Sparrow")
Bird.fly("Pigeon")

#static method - We need static methods when the processing is at the class level but we need not involve the class or instance.
#static methods are used when some processing is related to the class but does not need the class or its instance to perform any task.
#@staticmethod - decorator used

import math
class Sample:

    @staticmethod
    def calculate(x):
        result = math.sqrt(x)
        return result
num = int(input("Enter a number: "))

res = Sample.calculate(num)
print(res)

l = [1,2,2,3,3,3,4]
seen = {}
for i in l:
    seen[i] = seen.get(i, 0)+1
print(seen)
# for i in l:
#     if seen[i] > 1:
#         return i






