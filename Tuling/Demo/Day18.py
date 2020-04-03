# 学习第18天2020.03.24

# 普通参数只是按照位置传递，容易出错
def stu(name, age, addr):
    print("I am a student")
    print("我叫 {0}，我今年 {1} 岁了，我住 {2}".format(name, age, addr))
    return None


n = "xiaohong"
a = 19
addr = "我家"
stu(n, a, addr)


# 关键字参数案例
def stu_keys(name='No name', age=0, addr="No addr"):
    print("I am a student")
    print("我叫 {0}，我今年 {1} 岁了，我住 {2}".format(name, age, addr))
    return None


n = "xiaohong"
a = 19
addr = "我家"
stu_keys(name=n, age=a, addr=addr)
print("__________")


# 收集参数代码
# 函数模拟一个学生进行自我介绍，但是不清楚具体内容
# args可以看做一个列表
def stu(*args):
    print("Hello 大家好，我自我介绍一下")
    # type函数作用是检测变量的类型
    print(type(args))
    for item in args:
        print(item)


stu("xiaoming", "河北省石家庄市", 18, 'danshen')
stu("dazhou")

print("__________")
# 收集参数案例
# 说明收集参数可以不带任何实参调用，此时收集参数为空tuple
stu()
print("__________")


# 收集参数之关键字参数
def stu(**kwargs):
    print("Hello 大家好，自我介绍")
    print(type(kwargs))
    # 对于字典的访问，Python2.x和Python3.x有区别
    for i, k in kwargs.items():
        print(i, "---", k)
    return None


stu(name="zhangsan", age=19, addr="河北省石家庄市", work="Teacher")
stu(name='LiSi')

print("__________")
# 收集参数的混合调用案例
# stu模拟一个学生的自我介绍
def stu(name, age, hobby="没有", *args, **kwargs):
    print("Hello 大家好！")
    print("我叫{0}，我今年{1}。".format(name, age))
    if hobby == "没有":
        print("我没有爱好")
    else:
        print("我的爱好是{0}".format(hobby))
    for i in args:
        print(i)
    for k, v in kwargs:
        print(k, "---", v)
    return None
# 开始调用函数
name = "wangwu"
age = 19
hobby = "游泳"
stu(name, age, hobby)
print("__________")

# 收集参数的解包问题
def stu(*args):
    print("hhhhhhhhhhh")
    for i in args:
        print(type(i))
        print(i)


stu("zhangsan", "lisi", 19, 20)
l = list()
l.append("zhangsan")
l.append(20)
l.append(230)
stu(l)
# 此时，args的表示形式是字典，字典中包含一个list类型的元素，即 args = (["zhangsan", 20, 230])
# 很显然与我们最初的想法违背

# 此时的调用，我们就需要解包符号
