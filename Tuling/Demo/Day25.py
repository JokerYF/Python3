# 学习第25天（2020.04.01）
# dict字典
# 创建
d = {}
print(d)
print(type(d))

d = dict()
print(type(d))
print(d)

# 创建有值的字典（键和值之间用：隔开）
d = {"one": 1, "two": 2, "three": 3}
print(d)

# 用dict创建有内容的字典
# 关键字参数
d = dict(one=1, two=2, three=3)
print(d)

# 另一种写法
d = dict([("one", 1), ("two", 2), ("three", 3)])
print(d)

# 字典的操作
# 访问数据
d = {'one': 1, 'two': 2, 'three': 3}
# 注意访问格式
# 中括号内是建值，键值要用引号引起
print(d["one"])

# 修改字典中的值
d['one'] = "eins"
print(d)

# 删除某个值
# 使用del
del d['one']
print(d)

# 成员检测：in、not in
# 成员检测只检测key的内容
d = {'one': 1, 'two': 2, 'three': 3}

if 2 in d:
    print("value")
if 'two' in d:
    print('key')
if ('two', 2) in d:
    print('kv')

# 遍历在Python2和3中区别较大，代码不通用
# 按key来使用for循环
d = {'one': 1, 'two': 2, 'three': 3}
# 使用for循环，直接按key值访问
for k in d:
    print(k, d[k])

# 上述代码可以改写成如下：
for k in d.keys():
    print(k, d[k])

# 只访问字典的值
for v in d.values():
    print(v)

# 以下方法为错误写法
# for k,v in d:
#     print(k, '---', v)

# 正确写法
for k, v in d.items():
    print(k, '---', v)

# 字典生成式
# 常规字典生成式
d = {'one': 1, 'two': 2, 'three': 3}
dd = {k: v for k, v in d.items()}
print(dd)

# 加限制条件的字典生成式（就是为了加过滤条件）
dd = {k: v for k, v in d.items() if v % 2 == 0}
print(dd)

# 字典相关函数
# 通用函数：len,max,min,dict
# *str(字典)：返回字典的字符串格式
d = {'one': 1, 'two': 2, 'three': 3}
print(str(d))
# clear：清空字典
# items：返回字典的键值对组成的元组格式
d = {'one': 1, 'two': 2, 'three': 3}
i = d.items()
print(type(i))
print(i)
# dict_items为可迭代类型
# keys：返回字典的键组成的一个结构
k = d.keys()
print(type(k))
print(k)
# value：同理，可迭代的结构
v = d.values()
print(type(v))
print(v)
# get：根据指定键返回相应的值，优势：可以设置默认值
d = {'one': 1, 'two': 2, 'three': 3}
print(d.get("one"))
print(d.get("on333"))  # 这样写，即使不是字典中的键值，也不会报错
# get默认值是None，可以设置
print(d.get("on23", 100))  # 在字典中找对应键值，找不到，返回设置好的默认值100，如果不写，默认返回值是None
# fromkeys：使用指定的序列作为键值，使用一个值作为字典的所有键的值
l = ['eins', 'zwei', 'drei']
# 注意fromkeys两个参数的类型
# 注意fromkeys的调用主体
d = dict.fromkeys(l, 'hahahahaha')
print(d)
