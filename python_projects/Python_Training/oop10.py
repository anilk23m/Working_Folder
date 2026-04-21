#problem with constructor - Class C can not access all the super class attributes because of constructor. we have to use super() method
#in all the parent and chile class to resolve the issue.
#if se use super() method in only child class, Child can only access left side class attribute in multiple inheritance.
#so we have to sue super() method in all the parent and child class for multiple inheritance.
class A:
    def __init__(self):
        self.a = "a"
        print(self.a)
        super().__init__()

class B:
    def __init__(self):
        self.b = "b"
        print(self.b)
        super().__init__()

class C(A,B):
    def __init__(self):
        self.c = "c"
        print(self.c)
        super().__init__()
c = C()

