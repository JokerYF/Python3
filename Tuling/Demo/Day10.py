# 学习第10天（2020.03.17）
# 直接使用小括号创建
ta = ()
print(type(ta))
# 当使用小括号创建一个元素的tuple的时候，变量类型会发生改变
tb = (100)
print(type(tb))
tc = (100,)
# 下列变量的定义只有tuple类型才会使用，其他类型会报错
td = (100, 200, 300)
print(type(td))
print(td)
print("----------")
# 另一种类型
ta = 100,
print(type(ta))
tb = 100, 200, 300,  # 后面可以跟逗号，也可以不跟
print(type(tb))
print("----------")
# 使用tuple定义创建
ta = tuple()
# 使用定义创建的时候，必须加关键字
li = [1, 2, 3, 4, "xiaoming", "xiaohong"]
tb = tuple(li)  # 意为将list类型的li转换为tuple类型，并赋值给tb
print(tb)
print(li)
print("----------")
# tuple索引操作
la = [1, 2, 3, 4]
print(la)
ta = tuple(la)
print(ta[3])
# tuple 分片操作
print(ta[::2])
# 元组的相加
ta = 100, 200, 300
tb = ('i', 'y', 'x')
tc = ta + tb
print(tc)
# 元组相乘
tc = tb * 2
print(tc)
# 成员检测
print(tb)
if "i" in tb:
    print("right")
if 'x' not in tb:
    print("false")
print("----------")
# 元组的遍历
for i in tb:
    print(i)
print("----------")
# 元组可以嵌套
ta = ((10, 20, 30), ('a', "ab", "abc"))
# 1. 双层循环访问
for i in ta:
    print(i)
    for j in i:
        print(j)
print("----------")
# 2. 使用单层循环（i,k,j分别对应元组ta中嵌套的三个元素，每次循环都一一对应，随后依次打印）
for i, k, j in ta:
    print(i, k, j)
# 上述访问有特殊规定，即i,k,j要跟元素个数一一对应 ，不对应的情况下会报错

print("----------")
ta = 10, 20, 30
# 取长度
print(len(ta))
# 最大值（做比较时必须是同类型，否则会报错）
print(max(ta))
# 计数
print(ta.count(10))  # 括号内为需要计数的元素的值，打印结果为：这个元组中有多少个括号内的字符串
# 某一元素所在的位置
print(ta.index(10))  # 括号内为元素的值
print("----------")
# tuple的特殊用法
a = 100
b = "xiaoming"
# 将a，b的值进行互换
a, b = b, a
print(a)
print(b)
