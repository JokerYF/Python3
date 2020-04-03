# 文档案例
# 函数stu是模拟一个学生的自我介绍的内容
def stu(name, age, *args):
    '''
    这是文档
    name:表示学生名字
    age：表示年龄
    *args：表示收集参数
    '''
    print("This is a wendang")


# 查看函数1
help(stu)
print("__________")
# 查看文档2
print(stu.__doc__)
print("__________")
# 局部变量和全局部变量
a1 = 100


def fun():
    print(a1)
    print("I am in fun")
    a2 = 99
    print(a2)


print(a1)
fun()
# print(a2)
print("__________")
# 局部变量升为全局变量
b1 = 100


def fun():
    global b1
    b1 = 200
    print(b1)
    # print("I am in fun")
    # b2 = 99
    # print(b2)


fun()
print(b1)
# print(b2)
print("__________")
# globals 和 locals
a = 1
b = 2


def fun(c, d):
    e = 111
    print("Locals = {0}".format(locals()))
    print("Globals = {0}".format(globals()))


fun(100, 200)
print("__________")
x = 100
y = 200
# 执行x+y
z = eval("x+y")
print(z)
print("----------")
x = 100
y = 200
# 执行x+y
z1 = x + y
# 1. 注意字符串中引号的写法
# 2. 比对exec执行结果和代码执行结果
z2 = exec("print('x+y:', x + y)") # 先打印括号中的的内容：x+y: 300，并将exec的结果赋值给z2
print(z1) # 打印z1结果
print(z2) # 由于exec并没有返回结果，所以z2的值为None，打印：None
print("----------")
# 递归调用深度限制
x = 0


def fun():
    global x
    x += 1
    print(x)
    # 函数自己调用自己
    fun()


fun()