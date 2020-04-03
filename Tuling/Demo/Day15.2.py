# 接上
# 回车换行符
s = "这是一个换行符  \r\n已经换行了"
print(s)
print("----------")
# 百分号格式化
s = "Hello %s"
# 以下两种格式均可
print(s%"xiaoming")
print("Hello %s"%"xiaoming")
print("----------")
def a():
    print("a")
    return True
def b():
    print("b")
    return True
aaa = a() and b()
print(aaa)
print("----------")
bbb = a() or b()
print(bbb)