#Private attributes and methods-
#Private attributes and methods are meant to be used within the class and are not
#accessible from outside the class
#This is done to prevent exposing our instance attributes and methods outside the clas

class Person:
    __name = "annonymous"
    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()
