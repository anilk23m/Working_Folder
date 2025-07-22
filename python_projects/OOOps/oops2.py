# constructor function will be execute everytime an object is created
# all class have a function __init__() everytime class is initiated
class Student:
    college_name = "ABC College"
    name = "Anonymous name"
#default constructor and parameterized constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding students to database")
    def welcome(self):
        print("welcome student", self.name)

s1 = Student("karan", 97) #here parenthesis calls the __init__() function and print the string
print(s1.name, s1.marks)
print(s1.college_name)
s2 = Student("Abhishek", 88)
print(s2.name, s2.marks)
print(s2.college_name)
s3 = Student
print(s3.name)
s1.welcome()
s2.welcome()


