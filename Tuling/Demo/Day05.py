# 第五天2020.03.12
# 将九九乘法表当做一个函数
def jiujiu():
    for i in range(1, 10):
        for k in range(1, i + 1):
            print(i * k, ' ', end='')
        print()
    return None


jiujiu()
jiujiu()


# 改造九九乘法表
def printLine(line_num):
    """
    line_num:代表行号
    打印一行九九乘法表
    """
    for i in range(1, line_num + 1):
        print(line_num * i, " ", end='')
    print()


def jiujiu1():
    for o in range(1, 10):
        printLine(o)
    return None


jiujiu1()
print('-' * 20)


# 普通参数案例
def normal_para(one, two, three):
    print(one + two)
    return None


normal_para(1, 2, 3)
print('-' * 20)


# 默认参数案例
def default_para(one, two, three=100):
    print(one + two)
    return None


default_para(1, 2)

print('-' * 20)


# 关键字参数
def keys_para(one, two, three):
    print(one + two)
    print(three)
    return None


keys_para(one=1, two=2, three=3)
