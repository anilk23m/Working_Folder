#class method - A class method is bound to the class and receives the class as first argument
#Note - static method can't access or modify class state

#static method - not accessing neither class or instance object
#class method - takes cls as first implicit argument
#instance method - takes instance as the first implicit argument

class Person:
    name = "Annonymous"
    def change_name(self, name):
        self.name = name #it will not change the class object
        Person.name = "Rahul Kumar" #it will change the class object
        self.__class__.name = "Rahul" #it can also change the class object
    @classmethod
    def update_name(cls, name):
        cls.name = name

p1 = Person()
p1.change_name("Rahul Kumar")
print(p1.name)
print(Person.name)
p2 = Person()
p2.update_name("Kiran Kumar")
print(p2.name)
print(Person.name)

