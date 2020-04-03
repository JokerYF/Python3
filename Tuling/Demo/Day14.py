# 学习第十四天（2020.03.21）
class Student():
    name = "xiaoming"
    age = 19

    def sayHi(self):
        print("My name is {0}".format(self.name))
        # 如果没有return，会返回什么
        return None

    # sos是类的方法
    # 如何访问类的变量
    # 但是调用需要用到特殊的方法
    def sos():
        # 类方法中不允许访问实例的任何内容
        # 如果访问类的内容，注意两种用法
        print("My name is {},I am {} years old!".format(Student.name, __class__.age))
        return None


s = Student()
s.sayHi()
# 调用类方法的列子
Student.sos()
print("____________")


# 构造函数案例
class Student():
    name = 'NoName'
    age = 0

    # 构造函数的名称固定，写法相对固定
    def __init__(self):
        print("我是构造函数")


xiaohong = Student()
print("-----") # 在将构造函数实例化的时候，就打印了“我是构造函数”这句话
print(xiaohong.name)
print(xiaohong.age)
