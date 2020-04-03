# 学习第23天（2020.03.30）
# 浅拷贝：如果列表内嵌套一个列表，浅拷贝只会把最外层列表拷贝过去，内层列表只是指向原来的内层的列表
a = [1, 2, 3, [10, 20, 30]]
b = a.copy()
print(a)
print(b)
print(id(a[3]))
print(id(b[3]))
a[3][2] = 666
print(a)
print(b)
print("__________")
# 使用括号创建空元组
t = ()
print(type(t))
print(t)
# 创建一个只有一个值的元组
t = (1,)  # 在括号内写值后，加一个括号，不加，则输入元素是什么类型，t的类型还是什么类型
print(type(t))
print(t)
# 另一种方式
t = 1,  # 与上一个结果一样
# 创建多个值的元组
t = (1, 2, 3, 4, 5)
print(type(t))
print(t)
# 也可以不加括号
t = 1, 2, 3, 4, 5
print(type(t))
print(t)
# 使用其他结构创建，也可以创建tuple
l = [1, 2, 3, 4, 5]
t = tuple(l)
print(type(t))
print(t)
print("----------")
# 索引
t = (1, 2, 3, 4, 5)
print(t[4])
# 超标错误
# print(t[12])
# 切片，步长，元组也允许切片时超出自身的最大范围
t = (1, 2, 3, 4, 5, 6)
t1 = t[1::2]
print(id(t))
print(id(t1))
# 序列相加
# tuple类型不允许修改，是不允许修改元素，但是可以修改地址
t1 = (1, 2, 3)
t2 = (4, 5, 6, 7)
print(t1)
print(id(t1))
# 操作解释：将t1与t2相加，得到一个新的tuple，并将这个tuple，重新赋值给t1，所以，两个t1的id是不同的
# 如果是修改t1中的某个元素的值，则直接报错
t1 += t2
print(t1)
print(id(t1))
# 元组相乘
t = (1, 2, 3)
print(id(t))
print(t)
t = t * 3
print(id(t))
print(t)
# 成员检测
t = (1, 2, 3)
if 2 in t:
    print("yes")
else:
    print("no")
# 元组的遍历
# 一般采用for循环
# 1.单层元组遍历
t = (1, 2, 3, 'xiaoming', 'xiaohong', 'xiaowang')
for i in t:
    print(i)
# 2.双层元组的遍历
t = ((1, 2, 3), (4, 5, 6), (7, 8, 9))
# 对以上元组的遍历，可以如下操作
for i in t:
    print(i)
    for x in i:
        print(x)
for k,m,n in t:
    print(k, "---", m, "---", n)