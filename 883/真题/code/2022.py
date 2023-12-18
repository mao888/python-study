import math
# 选择题3 * 10
# 2
x = 30
y = 20
if x > y : print(x)
min = x if x < y else y
print(min)
# max = x > y ? x : y

while True:
    if  x > y :
        print(x)
        break
    # pass pass # 等待键盘中断 (Ctrl+C)

# 4. python关键字
import keyword
print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class',
# 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global',
# 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# 'try', 'while', 'with', 'yield']

# 5. 以下哪个类型不可以进行切片操作 str list tuple dict
# str（字符串）：
my_str = "Hello, World!"
sliced_str = my_str[1:5]
print(sliced_str)   # ello
# list（列表）：
my_list = [1, 2, 3, 4, 5]
sliced_list = my_list[1:4]
print(sliced_list)  # [2, 3, 4]
# tuple（元组）：
my_tuple = (1, 2, 3, 4, 5)
sliced_tuple = my_tuple[1:4]
print(sliced_tuple) # (2, 3, 4)

# dict（字典）：字典是无序的键值对集合，不支持切片操作。但你可以通过键来访问值。
my_dict = {'a': 1, 'b': 2, 'c': 3}
# 以下代码尝试对字典进行切片操作，会引发错误
# sliced_dict = my_dict[1:2]
# print(sliced_dict)

# 对字典而言，如果你想获得特定范围的键值对，你可以使用其他方法，例如遍历字典或使用字典视图。例如：
my_dict = {'a': 1, 'b': 2, 'c': 3}
sliced_dict = {key: my_dict[key] for key in ['a', 'b']}
print(sliced_dict)

# 6.Python合法的标识符
"""
在Python中，标识符是用来命名变量、函数、类等的名称。合法的标识符需要满足以下规则：
1. 由字母（a-z、A-Z）、数字（0-9）和下划线（_）组成。
2. 第一个字符必须是字母或下划线（不能是数字）。
3. 大小写敏感（name 和 Name 被视为不同的标识符）。
4. 不能使用保留字（关键字）作为标识符。
"""
# 以下是一些合法的标识符示例：
'''
variable_name
myVar
_name
counter1
PI
'''
# 以下是一些不合法的标识符示例：
'''
1variable (以数字开头)
my-var (包含连字符)
if (是保留字)
my name (包含空格)
my@var (包含特殊字符)
'''

# 9.给出四个类型，问哪个不是python内建数据类型。
"""
Python具有许多内建的数据类型，这些数据类型是Python语言本身提供的，无需导入额外的模块。以下是一些主要的内建数据类型：

1. **整数（int）：** 用于表示整数，如 `10`、`-5`。

2. **浮点数（float）：** 用于表示带有小数部分的数值，如 `3.14`、`-0.5`。

3. **字符串（str）：** 用于表示文本，如 `'Hello, World!'`、`"Python"`。

4. **布尔值（bool）：** 用于表示逻辑值，只有两个取值，`True` 和 `False`。

5. **列表（list）：** 有序、可变的元素序列，如 `[1, 2, 3]`、`['apple', 'banana', 'orange']`。

6. **元组（tuple）：** 有序、不可变的元素序列，如 `(1, 2, 3)`、`('apple', 'banana', 'orange')`。

7. **集合（set）：** 无序、不重复的元素集合，如 `{1, 2, 3}`、`{'apple', 'banana', 'orange'}`。

8. **字典（dict）：** 无序的键值对集合，如 `{'name': 'John', 'age': 30, 'city': 'New York'}`。

9. **字节串（bytes）：** 用于表示字节序列，如 `b'hello'`。

10. **字节数组（bytearray）：** 与字节串类似，但是是可变的。

11. **NoneType：** 表示空值或没有值的数据类型，通常用 `None` 表示。

这些内建数据类型提供了基本的数据组织和操作工具，适用于各种编程场景。在Python中，你可以使用这些数据类型来构建各种数据结构，实现各种算法，并进行数据处理和分析。
"""

# 判断题3 * 10
# 1.Python中的代码块使用缩进来表示。 True
# 2.Python字典和集合属于无序序列。  True
# 3.1+4j不是合法的python表达方式。（考察python复数表达方式）    False
# 4.元组可以组为字典的“键“。   True
# 元组作为字典的键
my_dict = {('apple', 1): 'red', ('banana', 2): 'yellow', ('orange', 3): 'orange'}
# 访问字典
print(my_dict[('apple', 1)])  # 输出: red
print(my_dict[('banana', 2)])  # 输出: yellow
print(my_dict[('orange', 3)])  # 输出: orange

# 5.表达式[] == None的值为True。   False
result = [] == None
print(result)   # False

my_list = []
if not my_list:
    print("The list is empty")      # The list is empty
else:
    print("The list is not empty")

# 6.在编写多层循环时，为了提高运行效率，应尽量减少内循环中不必要的计算。  True
# 7.深度学习是机器学习领域中一个新的研究方向，它更接近于人工智能的追求目标。    True
# 8.各个学派的代表技术，混淆一个出了一个判断题。
# 9.X、Y相互独立，则X、Y必不相关。 False
# 10.若P（A）=0，则A为不可事件。 False
'''
A 是不可能事件=⇒ P(A)=0; 注意概率为0 的事件不一定是不可能事件, 但不可能事件一定概率为0
'''