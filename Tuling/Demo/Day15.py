# 学习第15天2020.03.22
# 所有类都必须有父类
# 默认是object
class Person1():
    pass


class Person2(object):
    pass


class Person():
    name = "NoName"
    age = 0


# 父类写在类定义的时候的括号里
class Teacher(Person):
    pass


t = Teacher()
print(t.name)
print("----------")


# 一个子类可以继承多个父类的案例
class Bird():
    fiy = "yes,we can"

    def flying(self):
        print("飞呀飞")


class BirdMan(Person, Bird):
    pass


bm = BirdMan()
bm.flying()
print(bm.name)
print("__________")
# 利用刚刚定义的Bird,BirdMan,Person,Teacher，检测父子关系
print(issubclass(BirdMan, Bird))
print(issubclass(BirdMan, Person))
print(issubclass(BirdMan, Teacher))
print("__________")


# 构造函数
class Bird:
    def __init__(self):
        print("我被调用了")
        return None


b = Bird()


# 构造函数2
class Person():
    def __init__(self, name, age):
        print(name, age)

# 传参
p = Person("xiaohong", 19)


# 构造函数默认继承
class Person():
    def __init__(self, name, age):
        print("person =( {}, {})".format(name, age))


class Teacher(Person):
    pass

# 子类继承父类以后，构造函数会被继承，实例化子类的时候，需把父类中构造函数的变量一一对应填写，否则会报错
t = Teacher("xiaoming", 19)
t = Teacher() # 没有一一对应，这条会报错
