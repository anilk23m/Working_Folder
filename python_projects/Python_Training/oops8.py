from oopd6 import Teacher
#deriving a new class from the existing class such that the new class inherit all the members of the existing class
#the original class - base class or derived class or parent class
#the new class is called the sub class or derived class or child class.
class Student(Teacher):
    def setMarks(self, marks):
        self.marks = marks

    def getMarks(self):
        return self.marks

s1 = Student()
s1.setid(300)
s1.setName("Ashok")
s1.setAdd("1234 church street, Jayanagar, Bangalore")
s1.setMarks(980)
print("id: ", s1.getid())
print("name: ", s1.getName())
print("marks: ", s1.getMarks())
print("Address: ", s1.getAdd())

#When an object to Student class is created, it contains a copy of Teacher class within it.
#This means there is a relation between the Teacher class and Student class object.
#This is the reason Teacher class members are available to Student class.
#Note we don't create Teacher class object, but still a copy of it is available to Student class object.

#When  we write a constructor in the subclass, the super class constructor is not available to the subclass.
#in this case, only the sub class constructor is accessible from the subclass object.
#This means the sub class constructor is replacing the super class constructor.
#This is called constructor overriding.
#Similary in subclass, if we write a method with exactly same name as that of super class method. It will override the super class method.
#This is called method overriding.
# class Father:
#     def __init__(self):
#         self.property = 800000
#
#     def display_property(self):
#         print("Father\'s Property", self.property)
#
# class Son(Father):
#     pass
#
# s = Son()
# s.display_property()
#
class Father:
    def __init__(self):
        self.property = 800000

    def display_property(self):
        print("Father property", self.property)

class Son(Father):
    def __init__(self):
        self.property = 200000

    def display_property(self):
        print("Son property", self.property)
s = Son()
s.display_property()

class Father:

    def __init__(self, property):
        self.property = property

    def display_property(self):
        print("Father property", self.property)

class Son(Father):
    def __init__(self,property, land):
        super().__init__(property)
        self.land = land

    def display_property(self):
        print("Son property",self.property, self.land)

s = Son(800000, "mall")
s.display_property()