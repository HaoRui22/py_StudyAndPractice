#访问限制
class Student(object):
    def __init__(self, name, gender, score):
        self.__name = name
        self.__gender = gender
        self.__score = score

    def print_score(self):
        print(f"{self.__name}, {self.__gender}, score: {self.__score}")
    
    def get_name(self):
        return self.__name
    
    def get_gender(self):
        return self.__gender
    
    def get_score(self):
        return self.__score

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'
    
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')
    
    def set_gender(self, gender):
        self.__gender = gender

zane = Student('Zane Li', 'male', 98)
# 测试:
bart = Student('Bart', 'male', 77)
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')