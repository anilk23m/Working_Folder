class A:
    def method_a(self):
        print("Method from A")

class B:
    def method_b(self):
        print("Method from B")

class C(A, B):
    pass

c = C()
c.method_a()
c.method_b()
print(C.mro())
print(c.__class__.mro())
