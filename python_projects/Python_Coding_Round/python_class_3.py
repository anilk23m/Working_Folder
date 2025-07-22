class Student:
    def __init__(self, name, grades = None):
        self.name = name
        self.grades = {}
        if grades:
            for subject, marks in grades.items():
                self.add_grade(subject, marks)

    def add_grade(self, subject, marks):
        if not (0<=marks<=100):
            raise ValueError(f"marks {marks} for subject {subject} is invalid. It should be between 0 to 100.")
        self.grades[subject] = marks

    def avg_grade(self):
        total = sum(self.grades.values())
        avg = total/len(self.grades)
        return f"Student Name {self.name} {avg}"

    def __str__(self):
        grade_str = ",".join(f"{subject}:{marks}" for subject, marks in self.grades.items())
        return f"Student Name {self.name} \t Grades - {grade_str}"

student1 = Student("Alice", {"Math": 85, "Science": 92})
student1.add_grade("English", 70)
student1.add_grade("Math", 90)
student1.add_grade("Physics", 105)
average = student1.avg_grade()
print(student1)
print(average)
