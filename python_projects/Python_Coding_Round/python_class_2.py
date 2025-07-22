class Rectangle:
    def __init__(self, length:int, width:int):
        self.length = length
        self.width = width

    def area(self):
        if self.length <=0 or self.width <=0:
            print("length and width should be positive")
            return
        area_rectangle = self.length * self.width
        print(f"Area of the Rectangle is {area_rectangle}")

    def perimeter(self):
        if self.length <=0 or self.width <=0:
            print("length and width should be positive")
            return
        perimeter_rectangle = 2*(self.length + self.width)
        print(f"Perimeter of the rectangle is {perimeter_rectangle}")
rectangle1 = Rectangle(10, 20)
rectangle1.area()
rectangle1.perimeter()
