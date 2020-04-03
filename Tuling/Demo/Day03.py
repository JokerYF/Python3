# 图灵第三天  2020.03.10
# 分支语句练习
a = 4
b = 5
aa = a > b
if aa:
    print("a>b")
    print("a比b大")
else:
    print('a<b')
    print("a比b小")

print('_' * 20)
a = '你好'
if a:
    print('这个是真')
b = ''
if b:
    print()
else:
    print('这个是假')

print('_' * 20)
# input案例
# gender = input('请输入：')
# print(gender)
# if gender =="man":
#     print('一起玩')
# else:
#     print('回家去')
#
# print('_'*20)

# 循环
list_one = [1, 2, 3, 4, 5, 6, 7]
for i in list_one:
    print(i)
print('_' * 20)
# continue语句练习
# 在数字1-10中，找到所有的偶数，并打印
# 案例1
dig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for dig in dig_list:
    if dig % 2 == 0:
        print(dig)
    else:
        continue
print('-' * 20)
# 案例2
dig_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for dig in dig_list:
    if dig % 2 == 1:
        continue
    print(dig)
# pass案例1
age = 19
if age > 19:
    pass  # 占位符，没有的话这段代码无法执行
else:
    print("a")
# pass案例2
ages = [1, 2, 3, 4, 5, 6, 7]
for age in ages:
    pass
    print(age)
print('_'*20)
# range案例1
#生成一个从1到100的案例
dig_list = range(1, 100)
for dig in dig_list:
    print(dig)
print('-'*23)
print('|', ' '*2, '这是一个分隔符', ' '*2, '|')
print('-'*23)
# range案例2
for i in range(1,10):
    print(i)
print('-'*20)
# whlie循环案例1
a = 10000
b = 0
while a < 20000:
    a *= (1 + 0.067)
    b += 1
    print(a)
print('-' * 20)
# whlie循环案例2
a = 10000
b = 0
while a < 20000:
    a *= (1 + 0.067)
    b += 1
    print(a)
else:
    print(b)