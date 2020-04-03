# 传址和传值的区别
def a(n):
    n[2] = 300
    print(n)
    return None


def b(n):
    n += 100
    print(n)
    return None


an = [1, 2, 3, 4, 5, 6]
bn = 9
# 传址
print(an)
a(an)
print(an)
# 传值
print(bn)
b(bn)
print(bn)
# 对于简单的数值，采用传值操作，即在函数内对参数的操作不能影响外面的变量
# 对于复杂的变量，采用传址操作，即此时函数内外的参数和外部变量是同一份内容，任何地方对此内容的更改都会影响另外的变量或参数的使用