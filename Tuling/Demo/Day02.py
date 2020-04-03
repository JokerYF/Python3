# 图灵第二天2020.03.09
# 逻辑表达举例
a = True
b = True
c = False

aa = a and b  # 可转换为  1*1
print(aa)

bb = b and c
print(bb)

cc = 100 and c
print(cc)

dd = 100 and b
print(dd)

# 短路问题
a = True
b = True
c = False

aa = a or b and (a and b)  # 转换为算数： 1+。。。。。
print(aa)
print("-"*10)


def a():
    print("a")
    return True


def b():
    print("b")
    return True


aaa = a() and b()
print(aaa)
print("-" * 10)
bbb = a() or b()
print(bbb)

print('_'*20)
#成员运算符
L = [1,2,3,4,5]
a = 6
aa = a in L  #a是在L列表里
print(aa)
bb = a not in L  #a不是在L列表里
print(bb)
print('_'*20)
#身份运算符
a = 1
b = 1000998
aa = a is b
print(aa)  #False
#a  b  仅仅是值一样，并不带表a  b是同一个变量
a = 1000989888
b = 1000989888
aa = a is b
print(aa)  #False

a = 1
b = 1
aa = a is b
print(aa)
