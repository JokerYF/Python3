# 学习第24天（2020.03.31）
t = (1, 2, 3, 4, 5)
print(len(t))

# max,min:最大最小值
# 如果列表或者元素找那个有多个最大最小值，则实际打印出哪个？
print(max(t))
print(min(t))

# tuple：转化或创建元组
l = [1, 2, 3, 4, 5]
t = tuple(l)
print(t)
t = tuple()
print(t)

# 元组变量交换法
a = 1
b = 3
print(a)
print(b)
print("--------")
a, b = b, a
print(a)
print(b)
print("__________")
# 集合的定义
s = set()
print(type(s))
print(s)

s = {1, 2, 3, 4, 5}
print(type(s))
print(s)

# 如果只用大括号定义，则定义的是一个dict类型
s = {}
print(type(s))
print(s)
print("__________")

# 成员检测
# in/not in
s = {1, 2, "xiaoming", 'xiaohong', 'xiaoli', 7, 8}
print(s)
if 'xiaoming' in s:
    print("True")
if 'xiaowang' in s:
    print("False")

# 集合的遍历
s = {1, 2, "xiaoming", 'xiaohong', 'xiaoli', 7, 8}
for i in s:
    print(i, end=" ")
print()
print("----------")
# 带有元组的集合遍历
s = {(1, 2, 3), ('i', 'o', 'u'), (4, 5, 6)}
for k, m, n in s:
    print(k, '---', m, '---', n)

for i in s:
    print(i)

# 普通的集合
# 以下集合在初始化后自动滤掉重复元素
s = {23, 23, 44, 22, 3, 4, 5, 34, 3, 45, 434, 54, 56}
print(s)
# 普通集合内涵
ss = {i for i in s}
print(ss)
# 带条件的集合内涵
sss = {i for i in s if i % 2 == 0}
print(sss)
# 多循环的集合内涵（生成后结果没有规则）
s1 = {1, 2, 3, 4}
s2 = {"i", 'o', 'u'}
s = {m * n for m in s2 for n in s1}
print(s)
# 如果确定重复次数
s = {m * n for m in s2 for n in s1 if n == 2}
print(s)

# len,max,min：跟其他基本函数一直
s = {32, 4, 53, 4, 5, 6, 6, 45, 4, 5}
print(len(s))
print(max(s))
print(min(s))

# set：生成一个集合
l = [1, 2, 3, 4, 5, 43, 2, 3]
print(l)
s = set(l)
print(s)

# add:向集合内添加元素
s = {1}
s.add(223)
print(s)

# clear：清空集合
s = {1, 2, 3, 4, 3, 2}
print(id(s))
s.clear()
print(id(s))

# remove和discard
# s.remove(2)
print(s)
s.discard(6)
print(s)

# pop 随机移除一个元素
s = {1, 2, 3, 4, 5, 6, 7}
d = s.pop()
print(d)
print(s)

print("----------")

# 集合元素
s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}

s_1 = s1.intersection(s2)
print(s_1)

s_2 = s1.difference(s2)
print(s_2)

s_3 = s1.issubset(s2)
print(s_3)

s_4 = s1.union(s2)
print(s_4)

s_5 = s1.issuperset(s2)
print(s_5)

# 数学操作求差集
s_6 = s1 - s2
print(s_6)

# 冰冻集合的创建
s = frozenset()
print(type(s))
print(s)