
# 一 选择
# 3.
x = 1
y = 2
f = lambda x, y: x + y
print(f(1,2))

my_list = [(1, 3), (4, 2), (2, 8)]

# 使用 lambda 函数按照元组的第一个元素进行排序
sorted_list = sorted(my_list, key=lambda x: x[0])

print(sorted_list)

# 7.
# z = 1
# x = (y = z + 1)  # SyntaxError: invalid syntax

x,y = y,x
print(x,y)  # 2 1

# 三 填空
# 4.
print(sum(range(12)))   # 66
# 6.
print("hello world".find('w'))  # 6
# 7.
print("123123123".count("12"))    # 3
# 8. 浮点数的取值范围的上限，科学计数法  1.7976931348623157e+308

# 四 简答
# 1. 机器学习和深度学习的联系
# 深度学习是机器学习领域中一个新的研究方向,它更接近于人工智能的追求目标.深度学习是学习样本数据的内在规律和表示层次,这些学习过程中获得的信息对诸如文字,图像和声音等数据的解释有很大的帮助.
# 它的最终目标是让机器能够像人一样具有分析学习能力,能够识别文字,图像和声音等数据.
# 深度学习是一个复杂的机器学习算法,在语音和图像识别方面取得的效果远远超过先前技术.深度学习在很多相关领域都取得了很多成果.
# 深度学习使机器模仿视听和思考等人类的活动,解决了很多复杂的模式识别难题,使得人工智能相关技术取得了巨大进步.

# 2.
def fact(a):
    f = 1
    for i in range (1, a+1):
        f *= i
    return f
n = eval(input("请输入n的值："))
m = eval(input("请输入m的值："))
a=fact(n)
b=fact(m)
d=fact(n-m)
c = fact(n)/(fact(m) * fact(n-m))
print(c)

# 3、IOError、IndexError、AttributeError、KeyError、ImportError、SyntaxError

# 五 分析与计算
"""
1、给出函数def fmax(a, b)
调用fmax(m, n)
（1）参数传递（2）举五种参数传递
"""
def fmax(a, b):
    """返回两个数中的较大值"""
    return max(a, b)

# 调用方式一：位置参数传递
result_1 = fmax(3, 7)

# 调用方式二：关键字参数传递
result_2 = fmax(b=5, a=2)

# 调用方式三：混合使用位置参数和关键字参数
result_3 = fmax(8, b=4)

# 调用方式四：通过列表或元组的解包传递参数
# args = (10, 15)
args = {10, 15}
result_4 = fmax(*args)

# 调用方式五：通过字典的解包传递参数
kwargs = {'a': 20, 'b': 25}
result_5 = fmax(**kwargs)

# 打印结果
print("调用方式一:", result_1)  # 输出: 7
print("调用方式二:", result_2)  # 输出: 5
print("调用方式三:", result_3)  # 输出: 8
print("调用方式四:", result_4)  # 输出: 15
print("调用方式五:", result_5)  # 输出: 25


# 3. 时间转换
t = eval(input())
H = t // 3600  # 整除
t = t % 3600  # 取余
M = t // 60  # 整除
S = t % 60  # 取余
print("{}:{}:{}".format(H, M, S))               # 1:0:2

