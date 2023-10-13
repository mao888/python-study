"""
【例2-2】　时间转换
给定一个以秒为单位的时间t，要求用“ H ： M ： S ”的格式来表示这个时间。 H 表示小时， M 表示分钟， S 表示秒，它们都是整数且没有前导的“0”。例如，若t=0，则应输出“0：0：0”；若t=3661，则输出“1：1：1”。
案例分析：输入的数字为一个总秒数，需要将总秒数拆成几小时几分钟几秒，可通过1小时=60分钟，1分钟=60秒的规则进行拆分。
输入：
输入只有一行，是一个整数t（0 =t =86399），如5436。
输出：
输出只有一行，是以“ H ： M ： S ”的格式表示时间，不包括引号，如1：30：36。
解题思路：
给定的数字t是一个总秒数，所以应该是
t=s+m∗60+h∗60∗60
反推过来则是：小时h=t//3600，余数是剩下的s+m∗60，用余数继续可整除60得到分钟m=余数//60，余数则为秒s。
可以按照这个顺序，整除→取余→整除→取余。
"""
t = eval(input())
H = t // 3600  # 整除
t = t % 3600  # 取余
M = t // 60  # 整除
S = t % 60  # 取余
print(H, ':', M, ':', S, sep='')
print(H, ':', M, ':', S)
print("{}:{}:{}".format(H, M, S))

"""
【例2-3】　猜数游戏
程序中给出一个固定的数字，用户通过键盘输入一个数，如果这个数与程序给出的数字相同，则输出“恭喜你猜对了!”，如果这个数比程序给出的数字大则输出“太大了!”，如果这个数比程序给出的数字小，则输出“太小了!”。
案例分析：
输入：用户猜的数字。
处理：将用户猜的数字与程序给出的数字进行比较，可使用多分支结构进行判断。
输出：根据比较结果输出不同的结果。
"""
y = 50
x = eval(input())
if x == y:
    print('恭喜你猜对了!')
elif x > y:
    print('太大了!')
else:
    print('太小了!')

"""
【例2-4】　剪刀石头布游戏
小明和小红想玩“剪刀，石头，布”游戏。在这个游戏中，两个人同时说“剪刀”“石头”或“布”，压过另一方的为胜者。规则是：“布”胜过“石头”，“石头”胜过“剪刀”，“剪刀”胜过“布”。
案例分析：通过输入两人的选择，程序自己判断输赢，并输出相应的结果。
输入：
两个数分别代表小明和小红的选择，范围为{0，1，2}，用逗号隔开。0表示石头，1表示布，2表示剪刀。这两个数分别表示两个人所选的物品。如：0和2，则表小明出石头，小红出剪刀。
输出：
如果前者赢，输出“小明胜”。如果后者赢，输出“小红胜”。如果是平局，输出“平局”。
"""
a, b = eval(input())
if (a == 0 and b == 1) or (a == 1 and b == 2) or (a == 2 and b == 0):
    print('小红胜')
if (a == 1 and b == 0) or (a == 2 and b == 1) or (a == 0 and b == 2):
    print('小明胜')
if a == b:
    print('平局')

"""
【例2-5】　凯撒密码
凯撒密码是古罗马凯撒大帝用来对军事情报进行加密的算法，它采用替换方法对每一个英文字符循环替换为字母表序中该字符后面第3个字
符，对应关系如下：
原文：a b c d e f g h i j k l m n o p q r s t u v w x y z密文：d e f g h i j k l m n o p q r s t u v w x y z a b c假设原文字符为P，对应密文为S，则两者的关系为
S=（P+3）%26
P=（S-3）%26
加密的程序设计过程：
（1）输入一串原文字符串（假设信息全是小写字母a～z）。
（2）将字符串中的每一个字符进行转换，规则为S=（P+3）%26。由于字符没有办法直接与数字进行加法运算，所以需要先将字符转换为相应的Unicode编码，再进行加法运算，
    算完之后得到的Unicode编码又需要转为相应的字符。
    模26是因为字母表总共有26个字母，起始字母为'a'，所以将当前字母与字母'a'的差取模运算，结果再加上'a'的编码值即可得到加密后的字母编码值。
（3）将加密码后得到的新字符串进行输出。
实现代码如下：
"""
F = input('请输入明文：')     # Life is short,I use Python!
for P in F:
    if 'a' <= P <= 'z':
        S = chr((ord(P) - ord('a') + 3) % 26 + ord('a'))
    else:
        S = P
    print(S)    # Llih lv vkruw,I xvh Pbwkrq!

"""
【例2-6】　文本进度条
进度条是计算机处理任务或执行软件中常用的增强用户体验的重要手段，能实时显示任务或软件的执行进度。
我们用print（）函数结合字符串的格式化实现非刷新文本进度条和单行刷新文本进度条。
先按任务执行百分比将整个任务分成100个单位，每执行n%就输出一次进度条，每一次输出包含进度百分数，完成的部分用（∗∗）表示，未完成的部分用（…）表示。
中间用一个小箭头（→）分隔。如
由于程序执行速度非常快，远超人眼的视觉感知，如果直接输出，我们看不出来效果，因而每一次输出时让计算机等待t秒，增强显示效果。而等待需要使用时间库time中的sleep（）方法。
非刷新文本进度程序，代码如下：
"""
import time
scale = 10
for i in range(scale + 1):
    a = '*' * i
    b = '.' * (scale - i)
    c = (i / scale) * 100
    print("{:^3.0f}%[{}->{}]".format(c, a, b))
    time.sleep(0.1)