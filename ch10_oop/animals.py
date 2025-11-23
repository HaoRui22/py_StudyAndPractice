# 继承和多态1

class Animal(object):
    def run(self):
        print("Animal is running...")

class Dog(Animal): # Animal 是 Dog 的父类
    def run(self): # 子类的 run 覆盖了父类的 run
        print("Dog is running...")

    def eat(self):
        print("Eating meat...")

class Cat(Animal):
    def run(self):
        print("Cat is running...")
    
    def eat(self):
        print("Eating fish...")

class Schnauzer(Dog): # Schnauzer 是 Dog 的子类
    def run(self):
        print("Schnauzer is running...")

def run_twice(animal):
    animal.run()
    animal.run()

class Tortoise(Animal):
    def run(self):
        print("Tortoise is crawling slowly...")

class Timer(object):
    def run(self):
        print('Start...')

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    dog.run()
    cat.run()

    a = list() # a是list类型
    b = Animal() # b是Animal类型
    c = Dog() # c是Dog类型

    print(isinstance(a, list))
    print(isinstance(b, Animal))
    print(isinstance(c, Dog))
    print(isinstance(c, Animal)) # c 不仅仅是 Dog, 还是 Animal
    print(isinstance(b, Dog)) # 反过来则不行
    
    run_twice(Animal())
    run_twice(Dog())
    run_twice(Cat())

    run_twice(Tortoise())

    Timer().run()