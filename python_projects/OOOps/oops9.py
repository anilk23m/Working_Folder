#we use property decorator on any method in the class to use the method as property.
#if the attribute depends on the function, we can make the function as a property decorator
#when we make the function as property, we normally call the method without ()
#decorators - @staticmethod @classmethod @property @getter @setter
class Student:

    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math
        #self.percentage = str((self.phy+self.chem+self.math)/3) + "%"

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.math)/3) + "%"

s1 = Student(98, 97, 88)
print(s1.percentage)
s1.phy = 56
print(s1.percentage)