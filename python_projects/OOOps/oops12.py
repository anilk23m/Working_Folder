class Employee:
    def __init__(self, role, department, salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showDetails(self):
        #return self.role, self.department, self.salary
        print("role = ", self.role)
        print("department = ", self.department)
        print("salary = ", self.salary)


class Engineer(Employee):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__(role="Engineer", department="IT", salary=75000)

e1 = Employee("Account", "Finance", 54000)
e1.showDetails()
e2 = Engineer("Elon Musk", 45)
e2.showDetails()
