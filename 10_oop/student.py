# 面向对象编程
class Student(object):
    name = 'Student'
    def __init__(self, name, gender = 'male', score = 0):
        self.name = name
        self.gender = gender
        self.score = score

    def print_score(self):
        print(f"{self.name}, {self.gender}, score: {self.score}")
    
    def get_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

zane = Student('Zane Li', 'male', 98)
avery = Student('Avery Yan', 'female', 89)
zach = Student('Zacharich Li', 'male', 59)
zane.print_score()
print(f"grade: {zane.get_grade()}")
avery.print_score()
print(f"grade: {avery.get_grade()}")
zach.print_score()
print(f"grade: {zach.get_grade()}")