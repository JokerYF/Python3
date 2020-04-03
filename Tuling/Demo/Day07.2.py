# find实例
s = "My name is xiaoli, his name is xiaoming"
s1 = "li"
print(s.find(s1))
print(s.find("xiao", 20))
print("----------")
# 以下均不正确，应为有除字母外的空格
s1 = "我们对着灯发誓，这个是对的"
s2 = "benbarba is friend of baberbeng"
print(s1.isalpha())
print(s2.isalpha())
print("----------")
# 判断下列数字是什么类型
# 需要注意的是，因为输入法的问题，输入罗马数字可能得不到我们想要的结果
chin_num = "一二三四"
print(chin_num.isdigit())
print(chin_num.isnumeric())
print(chin_num.isdecimal())
print("----------")
a = "xiaoming"
b = "xiaoli"
s = "xiaoming and xiaoli are friends"
print(s.startswith(a))
print(s.endswith(b))
print("----------")
# join的例子，需要使用s1，s2，s3作为分割符，把ss内的内容拼接在一起
s1 = "$"
s2 = "-"
s3 = " "
ss = ["xiaoming", "xiaoli", "xiaohong"]
print(s1.join(ss))
print(s2.join(ss))
print(s3.join(ss))
