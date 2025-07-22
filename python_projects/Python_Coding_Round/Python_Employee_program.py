class Employee:
    __Emp_id = 0
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Employee.__Emp_id = Employee.__Emp_id + 1
        self.__Emp_id = Employee.__Emp_id


    def employeeDetails(self):
        return f"fullname is {self.firstname} - {self.lastname} - {self.__Emp_id}"

emp1 = Employee("Rahul", "Kumar")
emp2 = Employee("Anil", "Kumar")
output1 = emp1.employeeDetails()
output2 = emp2.employeeDetails()
print(output1)
print(output2)
