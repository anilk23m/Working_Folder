   # Methods are the function under the class
# default parameter here is self
class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for i in self.marks:
            sum += i
        print("hi", self.name, "your avg mark is", sum/3)
s1 = Students("Tony Stark", [99, 98, 97])
s1.get_avg()
s1.name = "Iron Man"
s1.get_avg()