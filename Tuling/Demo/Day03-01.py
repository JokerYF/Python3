# 练习
num = input('请输入分数')
num = int(num)
if num >= 90:
    print(num)
    print('优秀')
elif 80 <= num:
    print(num, '分')
    print('良好')
elif 70 <= num:
    print(num)
    print('中等')
elif 60 <= num:
    print(num)
    print('差劲')
elif num > 0:
    print(num)
    print('太差劲了')
else:
    print("要填写分数")
