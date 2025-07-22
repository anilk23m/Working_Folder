class Employee:
    def __init__(self, name, e_id, salary):
        self.name = name
        self.e_id = e_id
        self.salary = salary

    def display_details(self):
        return f"Employee name {self.name}\t{self.e_id}\t{self.salary}"

class Manager(Employee):
    def __init__(self, name, e_id, salary, department):
        super().__init__(name,e_id,salary)
        self.department = department
    def display_details(self):
        return f"Employee name {self.name}\t{self.e_id}\t{self.salary} and department {self.department}"
class Developer(Manager):
    def __init__(self,name,e_id,salary,department,program_language):
        super().__init__(name,e_id,salary, department)
        self.program_language = program_language
    def display_details(self):
        return f"Employee name {self.name}\t{self.e_id}\t{self.salary} and department {self.department} and Program Language {self.program_language}"

employee1 = Employee("Rahul", 1254, 50000)
emp1_data = employee1.display_details()
print(emp1_data)
manager1 = Manager("Kishore", 452562, 80000, "Atomation")
mng_data = manager1.display_details()
print(mng_data)
dev1 = Developer("Dave", 45, 45000, "Finance", "Python")
dev_data = dev1.display_details()
print(dev_data)

