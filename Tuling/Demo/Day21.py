# 学习第21天（2020.03.28）
# 汉诺塔案例
def hano(n, a='A', b='B', c='C'):
    '''
    汉诺塔的递归实现
    n：代表第N个塔
    a：代表第一个塔
    b：代表第二个塔
    c：代表第三个塔
    '''
    if n == 1:
        print(a, '--->', c)
        return None
    # if n == 2:
    #     print(a, '--->', b)
    #     print(a, '--->', c)
    #     print(b, '--->', c)
    #     return None
    # 把n-1个盘子，从a塔借助c塔，移动到b塔上
    hano(n - 1, a, c, b)
    print(a, '--->', c)
    # 把n-1个盘子，从b塔借助于A塔，移动到c塔上
    hano(n - 1, b, a, c)


hano(3)

print("----------")
# 有两个列表a，b
a = [i for i in range(1, 4)]
b = [i for i in range(100, 400) if i % 100 == 0]
print(a)
print(b)
c = [m + n for m in a for n in b]
print(c)  # 结果为两个list中的元素循环相加
