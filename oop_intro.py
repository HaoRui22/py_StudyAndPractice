# 面向过程编程
std1 = {'name': 'zane', 'score': 80}
std2 = {'name': 'avery', 'score': 90}

def print_score(std):
    print('%s: %s' % (std['name'], std['score']))

print_score(std1)
print_score(std2)

# 面向对象编程
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

zane = Student('Zane Li', 98)
avery = Student('Avery Yan', 100)
zane.print_score()
avery.print_score()