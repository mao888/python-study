x = "W3Cschool"
print(type(x))  # <class 'str'>

x = 100
print(type(x))  # <class 'int'>

x = 100.0
print(type(x))  # <class 'float'>

x = ('1','2','3')
print(type(x))  # <class 'tuple'>

x = ['1','2','3']
print(type(x))  # <class 'list'>

x = {'1','2','3'}
print(type(x))  # <class 'set'>

x = {'1':1,'2':2,'3':3}
print(type(x))  # <class 'dict'>

s = r"this is a line with \n"
print(s)  # this is a line with \n

s = "this is a line with \n"
print(s)  # this is a line with

s = u"this is an unicode string"
print(s)  # this is an unicode string

s = b"this is a bytes string"
print(s)  # b'this is a bytes string'

# 字符串可以用 + 运算符连接在一起，用 * 运算符重复
str = 'Hello World!'
s = 'Runoob'
print(str + " " + s)  # Hello World! Runoob
print(str * 2)  # Hello World!Hello World!

# Python 中的字符串有两种索引方式，从左往右以 0 开始，从右往左以 -1 开始
word = 'Python'
print(word[0], word[5])  # P n
print(word[-1], word[-6])  # n P

# Python中的字符串不能改变（详见上一小点的引用）。

# 字符串的截取的语法格式如下：变量 [头下标: 尾下标: 步长]
word = 'Python'
print(word[0:2])  # Py
print(word[2:5])  # tho
print(word[:2])  # Py
print(word[2:])  # thon
print(word[-2:])  # on
print(word[2:-2])  # th
print(word[::2])  # Pto
print(word[::-1])  # nohtyP

# Python 使用反斜杠(\)转义特殊字符，如果你不想让反斜杠发生转义，可以在字符串前面添加一个 r，表示原始字符串
print('Ru\noob')  # Ru  oob
print(r'Ru\noob')  # Ru\noob

# input("这是一个简单的input信息") # 这是一个简单的input样例，他输出input信息并接受一个字符串
# x = input("请输入X的值：") # 这是一个常见的input样例，他输出提示信息，然后接受一个字符串并将值传递给一个变量X
# x = int(x) # 将输入的字符串转换为整数
# print(x) # 打印变量，可以看到输入的x的值
# print(type(x)) #查看这个变量的类型

# 其实这里并没有接受任何内容，input函数以enter作为结尾，所以只有输入回车后才会结束input函数
# input("\n\n按下 enter 键后退出。")

import sys; x = 'W3Cschool'; sys.stdout.write(x + '\n')  # W3Cschool

