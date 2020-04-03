# 学习第17天（2020.03.24）
# 年利率是6.7%，则多少年后本金会翻倍，本利是每年翻滚
principal = 10000
year = 0
while principal <= 20000:
    year += 1
    principal *= 1.067

print(principal)
print(year)
principal = 10000
year = 0
while principal <= 20000:
    year += 1
    principal *= 1.067
else:
    print(year)
    print(principal)

print("__________")


# 参数的定义和使用
# 参数person只是一个符号，代表的是调用的时候的某一个数据
# 调用的时候，会用p的值代替函数中所有的person
def hello(person):
    print("{}, 你怎么了".format(person))
    print("{}, 你到底怎么了".format(person))
    return None


p = "明月"
hello(p)


def hello(person):
    print("{}, 你怎么了".format(person))
    print("{}, 你到底怎么了".format(person))
    return "我跟{0}打过招呼了，但是{0}不理我".format(person)


p = "明月"
rst = hello(p)
print(rst)
print("__________")
# 九九乘法表
for i in range(0, 10):
    for k in range(1, i + 1):
        print(i, "+", k, "=", i * k, end=" ")
    print()
print("__________")

# 默认参数案例
def reg(name, age, gender="male"):
    if gender == "male":
        print("{0} is {1}, and he is a good student".format(name, age))
    else:
        print("{0} is {1}, and she is a good student".format(name, age))
    return None


reg("xiaoming", 19)
reg("xiaohong", 18, "female")
