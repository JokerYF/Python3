# 学习第11天2020.03.18
# 1. 通过set关键字
sa = set()
print(sa)
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sb = set(li)  # 如果定义时，为（）,则集合的参数只能有一个
print(sb)
# 2. 使用大括号
sc = {1, 2, 3, 3, 4, 5, 6, 2, 1, 4, 5, 6, 7, 8}
print(sc)
# 集合的in操作
if 2 in sc:
    print(22222222)

# 遍历集合
for i in sc:
    print(i)
# 集合的另一种遍历
sa = {(1, 2, 3), (4, 5, 6), ("xiaoming", "xiaohong", "xiaoli")}
for i, j, k in sa:
    print(i, j, k)
# 集合的生成式
sa = {1, 2, 3, 4, 3, 2, 1, 5, 6, 7, 8, 5, 4, 5}
# 利用sa生成sb
sb = {i for i in sa}
print(sb)
sc = {i for i in sa if i % 2 == 0}
print(sc)

# 双重for循环
# 把sa中的每个元素的平方生成一个新的集合
# 1. 一个for
sd = {i ** 2 for i in sa}
print(sd)
# 2. 使用2个for
se = {m * n for m in sa for n in sa}
print(se)
# len：长度
print(len(sa))
print("----------")
sa = {1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1}
# max/min ：最值

# add：向集合中添加元素
print()
# clear：清空

# remove：删除
sa.remove(5)
print(sa)
# remove和discard的区别
# 写集合中的元素，如果是删除集合中没有的元素，会报错，但是discard不会报错
print("----------")
sa = {1, 2, 3, 4, 5, 6, 7}
print(sa)
sa.pop()
print(sa)
print("----------")
# 集合的数学操作
# intersection：交集
sa = {1, 2, 3, 4, 5, 6}
sb = {4, 5, 6, 7, 8, 9}
# sa和sb的交集
print(sa.intersection(sb))

# difference：差集
print(sa.difference(sb))
# 差集的另一种表示
print(sa - sb)
# union：并集
print(sa.union(sb)) # 不支持两个集合使用 +
print("----------")
# 冰冻集合案例
print(sa)
sb = frozenset(sa)
print(sb)