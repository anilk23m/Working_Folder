# if we want a method which will work for class - we call it static method
# OOP in every language having 4 important concepts
#1 Abstraction
#2 Encapsulation
#3 Inheritance
#4 Polymorphism
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    @staticmethod #here decorator @static method takes the function and manipulate the function and return the function
    def hello():
        print("hello world")
    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hi", self.name, "your avg mark is", sum/3)
s1 = Students("Tony Stark", [99, 98, 97])
s1.get_avg()
s1.name = "Iron Man"
s1.get_avg()
s1.hello()