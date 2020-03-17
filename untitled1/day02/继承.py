class Persion:
    name = "张三"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def run(self):
        print(self.name+str(self.age)+"岁在跑步")

class Student(Persion):
    def __init__(self,name,age,sex):
        self.naem=name
        self.age=age
        self.sex=sex
        # super.name = "王五"
    def run(self):
        print(self.name+self.sex+str(self.age)+"岁飞快的跑步")

if __name__ == '__main__':
    p = Persion("李四",23)
    p.run()
    s = Student("刘二",24,"女")
    s.run()
