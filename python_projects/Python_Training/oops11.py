#Method resolution Order (MRO)
class A():
    def method(self):
        print("A class method")
        super().method()
class B():
    def method(self):
        print("B class method")
        super().method()
class C():
    def method(self):
        print("C class method")
class X(A,B):
    def method(self):
        print("X class method")
        super().method()
class Y(C):
    def method(self):
        print("Y class method")
        super().method()
class P(X,Y):
    def method(self):
        print("P class method")
        super().method()
p = P()
p.method()
print(P.mro())

#rule1 = Search for the sub class before going for its base class
#rule2 = when a class is inherited from several class, it searches in the order from left to right
#rule3 = it will not visit any class more than once.
