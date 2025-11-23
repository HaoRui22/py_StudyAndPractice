#访问限制
class PtStudent(object):
    def __init__(self, name = 'unkw', gender = 'male', score = '0'):
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
    
    def set_score(self, score): #可以进行参数检查（11.2小节内容）
        if not isinstance(score, int):
            raise ValueError('bad input')
        elif score < 0 or score > 100:
            raise ValueError('bad score')
        else:
            self.__score = score
    
    def set_gender(self, gender):
        self.__gender = gender

if __name__ == "__main__":
    zane = PtStudent('Zane Li', 'male', 98)
    # 测试:
    bart = PtStudent('Bart', 'male', 77)
    if bart.get_gender() != 'male':
        print('测试失败!')
    else:
        bart.set_gender('female')
        if bart.get_gender() != 'female':
            print('测试失败!')
        else:
            print('测试成功!')