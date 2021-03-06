# 学习第九天  2020.03.16
# 直接赋值创建列表
L1 = [1, 2, 3, 4, 5]
# list内的数据可以不是同一类
L2 = [1, 2, 3, 'xiaoming', '小红']
# 可以创建空列表
L3 = []
# 或者
L4 = list()
print(L1)
print(L2)
print(L3)
print(L4)
print(type(L3))
print("----------")
# list创建的特例演示
s = "xiaohong"
# 想创建一个只包含s一个字符串的列表
L1 = list(s)
print(type(L1))
print(L1)
print("----------")
L1 = [20, 65, 88, 669, 88, 55, 22, 11, 44]
# 使用下标访问
print(L1[1])
print("----------")
# 切片操作案例（左包括右不包括）
L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(L1[1:6])
# 通过内置函数id可以判断出切片是否生成了全新的列表
# id的作用是用来判断两个变量是否是同一个变量
L2 = L1[0:10]
print(id(L1))
print(id(L2))
# 切片的下标可以为空
print(L1[:4])  # 从0开始，到第 4 号下标前一位为止
print(L1[3:])  # 从第 3 号下标开始，到末尾为止
print(L1[:])   # 复制一个完整的列表
# 切片可以控制增长幅度，默认增长幅度为1
print(L1[::1])  # 等于print(L1[:])
print(L1[::2])  # 第一个冒号控制列表长度，第二个冒号控制步长
# 下标可以超出范围，超出后不再考虑多余下标的内容
print(L1[:100])
print("----------")
# 下标值，增长幅度可以为负数
#   如果下标值为负数，标明从右往左
#   如果步长为正的情况下，顺序为从左往右，反则反之
# 为负数，标明顺序是从右往左
# 规定，数组最后一个数字的下标是-1
#   下面例子为空，原因是默认顺序为从左往右
print(L1[-2:-5])
# 如果想利用负数下标打印
#   方法1：打印结果为倒序
print(L1[-2:-5:-1])
#   方法2：打印结果为顺序
print(L1[-4:-1:1])