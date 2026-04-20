#inheritence -
class Teacher:
    def setid(self, id):
        self.id = id

    def getid(self):
        return self.id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setAdd(self, address):
        self.address = address

    def getAdd(self):
        return self.address

    def setSalary(self, salary):
        self.salary = salary

    def getSalary(self):
        return self.salary

# t = Teacher()
# t.setid(100)
# t.getid()
# t.setName("Prakash")
# t.setAdd("123 Main Street Electronic city phase1 Bangalore")
# t.setSalary(20000)
#
# print("id", t.getid())
# print("name", t.getName())
# print("address", t.getAdd())
# print("salary", t.getSalary())
