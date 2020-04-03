# 学习第22天（2020.03.29）
# append案例
a = [i for i in range(1, 4)]
print(a)
a.append(100)
print(a)
print("__________")
# insert案例
# insert(index,date)
print(a)
a.insert(3, 90)
print(a)
print("__________")
# 删除
# del
print(a)
del a[3]
print(a)
print("__________")
# pop
print(a)
last_ele = a.pop()
print(last_ele)
print(a)
print("__________")
a.insert(7, 100)
print(a)
print(id(a))
a.remove(100)
print(a)
print(id(a))
print("__________")
print(a)
print(id(a))
a.clear()
print(a)
print(id(a))
print("__________")
a = [1, 2, 3, 4, 5]
print(a)
print(id(a))
a.reverse()
print(a)
print(id(a))
print("__________")
b = [6, 7, 8, 9, 10]
print(a)
print(b)
print(id(a))
print(id(b))
a.extend(b)  # 将列表b拼接到a上
print(a)
print(id(a))  # 新列表是原来的列表a，id不变
print("__________")
print(a)
a.append(8)
a.insert(2, 8)
ss = a.count(8)
print(a)
print(ss)
print("__________")
# 列表类型变量赋值示例
a = [1, 2, 3, 4, 5, 6, 7, 888, 999]
print(a)
# list 类型，简单赋值操作，是传址操作
b = a
b[3] = 777
print(a)
print(id(a))
print(b)
print(id(b))
print("*" * 10)

# 为了解决上述问题，list赋值需要采用copy函数
b = a.copy()
print(a)
print(id(a))
print(b)
print(id(b))

print("*" * 10)
b[3] = 888
print(a)
print(b)
