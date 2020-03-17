#面向对象OOD编程

class Person:
    name = "张三"
    age = 23
    sex = "男"

    def run(self):
        print('走路')
    def sleep(self):
        print('睡觉')

class Animal:
    animalName = "金毛"
    animalSex = "公"
    animalLifeAge = "50"
    def __init__(self,animalName,animalSex,animalLifeAge):
        print("构造函数被执行")
        self.animalName = animalName
        self.animalSex = animalSex
        self.animalLifeAge = animalLifeAge

    def eat(self):
        print(self.animalName+"吃肉")
    def run(self):
        print(self.animalLifeAge+self.animalSex+self.animalName+"跑")


if __name__ == '__main__':
    # person = Person()
    # person1 = Person()
    # res = person.name
    # print(res,end="")
    # person.run()
    # res1 = person1.name="李四"
    # print(res1,end="")
    # person1.sleep()
    animal = Animal(animalName="金毛",animalSex="公的",animalLifeAge="生活了50年")
    animal.animalName="藏獒"
    animal.eat()

