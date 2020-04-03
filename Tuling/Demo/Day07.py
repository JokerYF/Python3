# 第七天2020.03.14
# 不用指定位置，按顺序读取
s = "{} , {}"
print(s.format("hello", "world"))
# 另一种形式
s = "{} {}!".format("hello", "world")
print(s)
# 使用编码
s = "{0} {1}".format("Hello", "World")
print(s)
s = "{1} {1}".format("Hello", "World")
print(s)
print('__________')
s = "我今天遇到{0}了，{0}对我打了招呼".format("小明")
print(s)
print('__________')
s = "你好，这里是{a_name}，欢迎{person_name}的到来，这里的地址是{c_name}"
s = s.format(a_name="开心学堂", person_name="小芳", c_name="河北省南部某镇")
print(s)
print('__________')
s = "你好，这里是{a_name}，欢迎{person_name}的到来，这里的地址是{c_name}"
# 该定义为字典，将字符串加入到一个字典中
s_dict = {"a_name": "开心学堂", \
          "person_name": "小芳", \
          "c_name": "河北省南部某镇"}
# **代表解包
s = s.format(**s_dict)
print(s)
print('__________')
s = "I am {:.2f}fKG weight, {:.2f}m Heigh"
print(s.format(50, 1.7))
print('__________')
help(str)
# find实例
s = "My name is xiaoli, his name is xiaoming"
s.find("li")
s.find("xiao",20)