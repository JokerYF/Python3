# 第六天2020.03.13
# 转义字符的案例
# 想表达Let's Go
# 使用转义字符
s = 'Let\'s Go'
print(s)

# 使用单双引号嵌套
s = "Let's Go"
print(s)

# 表示斜杠
# 例如路径
s = "c:\\user\\aaa"
print(s)

# 回车换行
# windows 下也可以使用\r\n，效果相同
s = "I\nLove\nChina"
print(s)

print('___________')


def myDemo(x, \
           y, \
           z):
    print('aaaaaaaa')


myDemo(1, 2, 3)
print('___________')

# %s 表示简单的字符串
# 占位符可以单独使用
s = "Hello %s"
print(s)
# 用实际意义替换s中的占位符
print(s % '小明')
print(s % '小张')
# 另一种方式
print('hello %s' % "小赵")
# 占位符一般只能被同种类型替换，或者类型能被转换成占位符的类型

print('___________')
# 浮点数占位符案例
s = "I am %fKG weight, %fm Heigh"
print(s)
print(s % (50, 1.7))

# 占位符浮点数格式控制（控制小数点后位数）
s = "I am %.2fKG weight, %f.2m Heigh"
print(s % (50, 1.7))
