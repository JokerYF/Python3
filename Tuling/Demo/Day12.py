# 学习第12天2020.03.19
def funa(n):
    print("aaa")


def funb(n):
    funa(100)
    print("bbb")


funb(100)


# 阶乘
# func_a表示计算阶乘
def fun_a(n):
    print(n)
    # 递归一定要有结束条件
    if n == 1:
        return 1
    return n * fun_a(n - 1)


rst = fun_a(5)
print(rst)


# 斐波那契数列
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)


rst = fib(10)
print(rst)

# 汉诺塔
a = 'a'
b = 'b'
c = 'c'


def hano(a, b, c, n):
    if n == 1:
        print("{}-->{}".format(a, c))
        return None
    if n == 2:
        print("{}-->{}".format(a, c))
        print("{}-->{}".format(a, b))
        print("{}-->{}".format(b, c))
        return None
    hano(a, b, c, n - 1)
    print("{}-->{}".format(a, c))
    hano(b, a, c, n - 1)


hano(a, b, c, 1)
hano(a, b, c, 2)
hano(a, b, c, 5)
print("----------")


# 定义一个学生类
class Student():
    # 此处定义一个空类
    # pass是关键字，表示占位用的，无意义
    pass


print("----------")
# 定义一个对象
a = Student()
print("----------")


# 创建类，并在类里创建函数
class PythonStudent():
    name = "NoOne"
    age = 18
    course = "python"

    def giveMeMoney(self):
        print("Show me the money")
        return None

# 为这个了定义一个对象（自己写的，可能不正确）
xiaobai = PythonStudent()
# 打印这个对象的信息
print(xiaobai.age)
print(xiaobai.name)
print(xiaobai.course)
