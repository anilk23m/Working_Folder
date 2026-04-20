class StudentMarks:
    def __init__(self, name, math, science, english):
        self.name = name
        self.math = math
        self.science = science
        self.english = english
    def calculate_percentage(self):
        total = self.math + self.science + self.english
        percentage = (total/300)*100
        return percentage
    def display_result(self):
        percentage = self.calculate_percentage()
        print(f"\n Student : {self.name}")
        print(f"Math : {self.math}")
        print(f"Science : {self.science}")
        print(f"English : {self.english}")
        print(f"Percentage : {percentage:.2f}%")

student1 = StudentMarks("Anil", 85, 90, 78)
student1.display_result()

