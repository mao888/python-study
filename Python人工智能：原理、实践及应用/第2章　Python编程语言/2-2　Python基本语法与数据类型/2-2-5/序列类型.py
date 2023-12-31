# 序列类型
"""
序列类型是一个元素向量，元素之间存在先后关系，通过序号访问，元素之间不排他，即可出现相同值的元素。
Python中很多数据类型都是序列类型，其中比较重要的是字符串（str）、元组（tuple）、列表（list）。

字符串可以看成一个单字符的有序组合，属于序列类型，同时也是一种基本数据类型。
元组是包含0个或多个数据项的不可变序列类型，即元组一旦生成，任何数据项都不可替换或删除。
列表则是一个可以修改数据项的序列类型，使用非常灵活。
"""

# 1．元组类型
"""
元组一旦创建就不能被修改。一般用于表达固定数据项、函数返回值、多变量同时赋值、循环遍历等情况。
Python构建元组的方式非常简单，可以用tuple（）函数构建，tuple（）函数中的参数是一个可迭代的数据，若没有传入参数，则创建空元组。
也可以直接用圆括号包含多个使用逗号隔开的元素来创建元组。非空元组的括号可以省略。
"""
tup1 = tuple()  # 创建空元组
tup2 = tuple([1, 2, 3])  # 创建元组
tup3 = ()  # 创建空元组
tup4 = (1, 2, 3)  # 创建元组
tup5 = 1, 2, 3  # 创建元组
print(tup1, tup2, tup3, tup4, tup5)  # 输出：() (1, 2, 3) () (1, 2, 3) (1, 2, 3)

# 2．列表类型
"""
列表（list）是包含0个或多个对象引用的有序序列，与元组不同，列表的长度和内容都是可变的，可自由对列表中的数据项进行增加、删除或替换。列表没有长度限制，元素的类型可以各不相同，使用非常灵活。
"""
#  1）列表创建
"""
可以通过list（）函数将已有的元组字符串转换为列表。也可以直接用[ ]号创建，代码如下：
"""
list1 = list()  # 创建空列表
list2 = list([1, 2, 3])  # 创建列表
list3 = list('abc')  # 创建列表
list4 = []  # 创建空列表
list5 = [1, 2, 3]  # 创建列表
list6 = ['a', 'b', 'c']  # 创建列表
tp = (1, 2, 3)  # 创建元组
st = 'abc'  # 创建字符串
list7 = list(tp)  # 将元组转换为列表
list8 = list(st)  # 将字符串转换为列表
print(list1, list2, list3, list4, list5, list6, list7,
      list8)  # 输出：[] [1, 2, 3] ['a', 'b', 'c'] [] [1, 2, 3] ['a', 'b', 'c'] [1, 2, 3] ['a', 'b', 'c']
#  2）列表操作
"""
与整数及字符串不同，列表要处理一组数据，因此，列表必须通过显式的数据赋值才能生成，简单将一个列表赋值给另一个列表是不会生成新的列表对象的，而是将两个变量指向了同一个列表。只有通过list（）或[ ]创建才会生成新列表，代码如下：
"""
list1 = [1, 2, 3]  # 创建列表
list2 = list1  # 将list1赋值给list2
list3 = list(list1)  # 通过list（）创建新列表
list4 = list1[:]  # 通过切片创建新列表
list1[0] = 4  # 修改list1的第一个元素
print(list1, list2, list3, list4)  # 输出：[4, 2, 3] [4, 2, 3] [1, 2, 3] [1, 2, 3]

"""
如果非要将一个列表的值赋给另一个变量，可通过复制的方式实现，代码如下：
"""
ls = [12, 'abc', ['red', 'green', 'blue']]  # 创建列表
lt = ls.copy()  # 复制列表
ls[0] = 24  # 修改ls的第一个元素
ls[2].append('white')  # 修改ls的第三个元素
print(ls, lt)  # 输出：[24, 'abc', ['red', 'green', 'blue', 'white']] [12, 'abc', ['red', 'green', 'blue']]
"""
列表中元素访问与操作，代码如下：
"""
ls = ['cat', 'dog', 'tiger', 1024]  # 创建列表
ls[1:2] = [1, 2, 3]  # 修改ls的第二个元素
print(ls)  # 输出：['cat', 1, 2, 3, 'tiger', 1024]
ls[1:3] = []  # 删除ls的第二个和第三个元素
print(ls)  # 输出：['cat', 3, 'tiger', 1024]
del ls[0:6:2] # 删除ls的第一个到第六个元素，步长为2
print(ls)  # 输出：[3, 1024]
"""
列表常用方法对元素操作，代码如下：
"""
ls = ['cat', 'dog', 'tiger', 1024]  # 创建列表
ls.append('elephant')  # 在列表末尾添加一个元素
print(ls)  # 输出：['cat', 'dog', 'tiger', 1024, 'elephant']
ls.insert(2, 'snake')  # 在列表第三个位置插入一个元素
print(ls)  # 输出：['cat', 'dog', 'snake', 'tiger', 1024, 'elephant']
ls.extend(['ant', 'bee'])  # 在列表末尾添加多个元素
print(ls)  # 输出：['cat', 'dog', 'snake', 'tiger', 1024, 'elephant', 'ant', 'bee']
ls.remove('snake')  # 删除列表中第一个出现的指定元素
print(ls)  # 输出：['cat', 'dog', 'tiger', 1024, 'elephant', 'ant', 'bee']
ls.pop(2)  # 删除列表中指定位置的元素
print(ls)  # 输出：['cat', 'dog', 1024, 'elephant', 'ant', 'bee']
ls.reverse()  # 将列表中的元素反向存放
print(ls)  # 输出：['bee', 'ant', 'elephant', 1024, 'dog', 'cat']
ls.clear()  # 清空列表中的元素
print(ls)  # 输出：[]
ls.extend([1, 2, 3, 10, 9])  # 在列表末尾添加多个元素
print(ls)  # 输出：[1, 2, 3, 10, 9]
ls.sort()  # 将列表中的元素按照指定方式排序
print(ls)  # 输出：[1, 2, 3, 9, 10]
ls.sort(reverse=True)  # 将列表中的元素按照指定方式逆序排序
print(ls)  # 输出：[10, 9, 3, 2, 1]
print(sum(ls))  # 输出：25

# 3）列表元素遍历
"""
对列表进行遍历使用for-in结构，可对列表中的元素按序访问。基本语法格式：
如果对元素访问时不需要删除操作，则可直接遍历列表。
如果对元素访问时涉及删除或改变元素位置等操作，
则应先对原列表进行复制，在复制的列表中遍历，而在原列表中操作，这样可以保证每个元素都能被遍历并进行操作。下面通过几个案例来实践。
"""
'''
【例2-7】　对列表元素求平均值
已知一组数据[20，10，7，6，31]，请求出这一组数据的平均值。案例分析：对列表中的每个元素进行访问，对它们的值进行累加，再
将累加结果除以列表长度即可得到列表的平均值。在这个过程中，不需要改变元素的位置，可以直接对列表进行遍历。
'''
ls = [20, 10, 7, 6, 31]  # 创建列表
sum = 0  # 创建累加变量
for i in ls:  # 遍历列表
    sum += i  # 累加求和
print(sum / len(ls))  # 输出：14.8

'''
【例2-8】　删除3的倍数
指定列表[23，45，78，87，11，67，89，13，243，56，67，311，431，111，141]中，请将其中所有为3的倍数的元素删除，并输出剩余的元素及删除元素的个数。
案例分析：在这个案例中需要对列表中每个元素访问，并判断该元素是否能被3整除，如果能被3整除，则删除该元素。
一旦涉及元素的删除，就会导致列表的元素索引号发生改变，为保证每个元素都能被遍历，故需要先复制列表，在复制的列表中遍历，在原列表中删除。代码如下：
'''
ls = [23, 45, 78, 87, 11, 67, 89, 13, 243, 56, 67, 311, 431, 111, 141]  # 创建列表
lt = ls.copy()  # 复制列表
count = 0  # 创建计数器
for i in lt:  # 遍历列表
    if i % 3 == 0:  # 判断是否能被3整除
        ls.remove(i)  # 删除元素
        count += 1  # 计数器加1
print(ls, count)  # 输出：[23, 11, 67, 89, 13, 56, 67, 311, 431] 6
