#different types of variable we use in class
#different types of methods we use in class

#instance variable
# instance variable is belongs to object (instance)
# each object has its own copy - if we want to change instance variable we use self.variable

#and class variable (Statis variable)


class Car:
    def __init__(self):
        self.color = "Blue" #instance variable (same copy available to all the instances)
    def modify(self): #instance method
        self.color = "Red"

s1 = Car() #object or instance of the class
s2 = Car()
print("x in s1 = ", s1.color)
print("x in s2 = ", s2.color)
s1.modify()
print("x in s1 = ", s1.color)
print("x in s2 = ", s2.color)


class Sample:
    x = 10 #class variable  (available to all the instances)

    @classmethod
    def modify(cls):
        cls.x += 1
s1 = Sample()
s2 = Sample()
print(s1.x, s1.x)
s1.modify()
print(s1.x, s2.x)

#static method - no dependency with cls or self.
#@staticmethod

#Namespace -
# A name space represents a memory block where names are mapped to object

class Student:
    n = 10
s1 = Student()
print(s1.n)
s2 = Student()
print(s2.n)
s1.n += 1
print(s1.n)
print(s2.n)

#instance method
#class method
#static method

class Student:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark
    def display(self):
        print("Hi", self.name)
        print("Your mark is ", self.mark)
    def calculate(self):
        if (self.mark >= 600):
            print("You got first grade")

        elif (self.mark >= 500):
            print("You got second grade")

        elif (self.mark >= 350):
            print("You got third grade")

        else:
            print("You got failed")

n = int(input("Enter number of student: "))
i = 0
while i<n:
    name = input("Enter your name: ")
    mark = int(input("Enter your mark: "))
    s = Student(name, mark)
    s.display()
    s.calculate()
    i += 1
    print("===============================")
#two types of instance method - Accessor method(get) and Mutator method (set)
