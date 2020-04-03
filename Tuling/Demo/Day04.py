# 图灵第四天2020.03.11
def func():
    print('这是一个函数')
    print('这个函数需调用才会执行')


func()
print('函数执行结束')
print('-' * 20)


# 形参和实参的实例
# 参数person只是一个符号
# 调用的时候用另一个
def hello(person):  # 括号中的person为形参，没有具体的参数，占位
    print('{0},你好'.format(person))
    print('{},你好啊'.format(person))


p = '小明'
# 调用函数，需要把p作为实参传入
hello(p)  # p有实际值，将p的值传到函数中把形参替换，即p为实参

d = hello('aa')  # 将hello函数的值赋值给d，但是hello没有返回值，所以系统默认给出返回值None，并赋值
print(d)
print('-' * 20)
help(print)

print('-' * 20)

# 九九乘法表
# version 1.0
for i in range(0, 10):
    for k in range(1, i + 1):
        print(i * k, ' ', end='')
    print()
