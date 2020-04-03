# 学习第13天2020.03.20
# 类的例子
# 注意类的定义
class Student():
    name = "xiaoming"
    age = 19

    def sayHi(self):
        print("My name is {0}".format(self.name))
        # 如果没有return，会返回什么
        return None


# self举例
# 实例调用函数
yaoyao = Student()
# 让瑶瑶跟我打声招呼
# 瑶瑶调用sayHi没有输入参数
# 因为默认实例作为第一个参数传入
# yaoyao.sayHi()
print("----------")


# self可以更换名字
class Student2():
    name = "xiaoming"
    age = 19

    def sayHi(self, n, a):
        self.name = n
        self.age = a

        print("My name is {}, I am {} years old.".format(self.name, self.age))
        return None


# 以下案例说明，实例变量可以借用类的变量
xiaohong = Student2()
xiaohong.sayHi("ping", 16)
print("My name is {}, I am {} years old.".format(Student2.name, Student2.age))
print("My name is {}, I am {} years old.".format(xiaohong.name, xiaohong.age))
# 如果访问实例的属性没有定义，则自动访问类的属性
# 如果类的属性没有定义，报错
# print(xiaohong.father)

