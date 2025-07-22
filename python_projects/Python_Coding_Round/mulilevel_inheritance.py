class Grandparent:
    def show_gp(self):
        print("Grandparent method")

class Parent(Grandparent):
    def show_p(self):
        print("Parent method")

class Child(Parent):
    def show_c(self):
        print("Child method")

c = Child()
c.show_gp()
c.show_p()
c.show_c()
print(Child.mro())
print(c.__class__.mro())