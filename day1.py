class Student:
    def __init__(self, name, num, chinese = 0, math = 0, english = 0):
        self.name = name
        self.num = num
        self.grades = {"chinese": chinese, "math": math, "english": english}

    def set_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject] = grade

    def print_grade(self):
        print(f"{self.name} ({self.num}) 的各科成绩为：")
        for subject, grades in self.grades.items():
            print(f"{subject}:{grades}")
    def get_average(self):
        total = sum(self.grades.values())
        count = len(self.grades)
        return total / count
    def pass_all(self):
        return all(grade >= 60 for grade in self.grades.values())




san = Student("张三", "001", 90, 80, 75)
si = Student("李四", "002", 50, 60, 70)

print(f"平均分: {san.get_average()}")
print(f"是否通过所有科目: {san.pass_all()}")

san.print_grade()
si.print_grade()
print(f"平均分: {si.get_average()}")
print(f"是否通过所有科目: {si.pass_all()}")
