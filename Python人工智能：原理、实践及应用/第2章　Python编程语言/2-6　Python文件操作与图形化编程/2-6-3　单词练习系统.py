"""
设计单词练习系统，建立一个单词库，可以从单词库中随机抽取单词进行练习。
练习方式有英译中、中译英、拼写填空，对于回答正确的问题会给出提示，并增加积分，错误的问题只有提示，不增加积分。
练习完成后可以查看出错的单词，并对错误的单词进行次数统计。模块示意图如图2-15所示。
"""
"""
图2-15 单词练习系统模块示意图
            单词练习系统
界面元素     单词练习      错词查看
标题         英译中        错词表
积分         中译英        错误次数
练习选择     拼写填空       返回
输入框       正误判断
判断         积分现实
链接         判断提示
退出
"""
# 1．界面设计
"""
使用tkinter进行GUI图形界面设计，界面可参考图2-16。
"""
"""
图2-16　单词练习系统界面设计
"""
"""
初始化设置：
创建系统类，在类中创建构造方法，设置各种初始化变量。
（1）创建tkinter窗口对象，设置窗口属性。
（2）设置窗口中需要使用的变量，如：当前积分、显示的随机单词，以及回答提示信息。
（3）创建单选按钮组名。
创建各类变量，相当于是全局变量。
（1）创建单词列表变量。
（2）创建错词列表变量。
（3）创建显示单词变量。
（4）创建拼写填空的变量。
（5）创建随机数变量（用于从单词表中随机抽取单词）。
（6）引用各种方法：如界面设置布局、窗体运行方法。
初始化设置代码如下：
"""
import tkinter
import random
import tkinter.messagebox
import math
from tkinter import ttk
class Recite():
    def __init__(self):
        self.root = tkinter.Tk()    # 创建主窗体
        self.root.geometry('450x500')   # 设置窗口大小
        self.root.title('背单词')      # 设置窗口标题
        self.root['bg'] = 'yellow'   # 设置窗口背景颜色
        self.word = tkinter.StringVar()  # 创建显示单词变量
        self.score = tkinter.StringVar()    # 创建显示积分变量
        self.fen = 0    # 设置初始积分为0
        self.score.set(0)   # 设置初始积分为0
        self.prompt = tkinter.StringVar()   # 创建显示提示信息变量
        self.prompt.set('你最棒')
        self.wrong = []     # 创建错词列表
        self.dic = []   # 创建单词列表
        self.word_list()    # 调用单词列表方法
        # print(len(self.dic))
        self.radiolist = tkinter.IntVar()   # 创建单选按钮组名
        self.fill = ''  # 创建拼写填空的变量
        self.space = ''    # 创建空格

        self.r = random.randint(0, len(self.dic)-1)  # 创建随机数变量（用于从单词表中随机抽取单词）
        self.word.set(self.dic[self.r][0])  # 设置显示单词变量
        self.layout()   # 调用界面设置布局方法
        self.root.mainloop()    # 调用窗体运行方法

# 2．单词读取设计
"""
从单词库文件中将单词读取出来。可以用数据库，也可以使用文件，此处用的是文件。文件中的每一行由一个单词的中英文构成。
打开文件读取数据，先对数据进行清洗，按换行符将它们分离成列表，一个单词为一个元素。
再对列表进行遍历，对于遍历到的每一个元素即单词再次进行分离，即每个单词分成中文和英文两个元素，将分离得到的列表追加到初始化设置中创建的单词列表变量中。
代码如下：
"""
def word_list(self):
    f = open('words.txt', 'r', encoding='utf-8')
    t = f.read().split('\n')
    for d in t:
        self.dic.append(d.split())
    f.close()

"""
参照界面图进行界面元素的创建与布局并进行主界面设计。
（1）标题：为标签，放置到顶部。
（2）积分：标签+标签，提示标签中的文本属性为“当前积分”，积分标签中的内容为文本变量，显示初始设置中的积分变量。
（3）单词显示：标签，文本为初始设置中的显示单词变量。
（4）答案输入：输入文本框。
（5）练习方式：单选按钮组，根据选择通过command属性调用不同的方法。
（6）回答提示：标签，文本为初始设置中的提示变量。
（7）判断（确定）：按钮，通过command属性调用判断方法。
（8）退出：按钮，通过command属性调用退出方法。
（9）查看错词表：按钮，通过command属性调用错词显示方法。
（10）查看单词表：按钮，通过command属性调用单词显示方法。
主界面布局代码如下：
"""
def layout(self):
    # 标题
    lab1 = tkinter.Label(self.root, text='背单词,赢积分', font=('宋体', 30), bg='yellow')   # 创建标签
    lab1.pack(pady=20)    # 设置标签位置
    lab_score = tkinter.Label(self.root, textvariable=self.score, font=('宋体', 30), fg='red', bg='yellow')   # 创建标签
    lab_score.pack()    # 设置标签位置
    lab_2 = tkinter.Label(self.root, text='当前积分：', font=('宋体', 16), bg='yellow')   # 创建标签
    lab_2.place(x=40, y=100)    # 设置标签位置
    lab_word = tkinter.Label(self.root, textvariable=self.word, font=('宋体', 20), bg='white')   # 创建标签
    lab_word.place(x=130, y=140)    # 设置标签位置
    lab_prompt = tkinter.Label(self.root, textvariable=self.prompt, font=('宋体', 18), fg='blue', bg='yellow')   # 创建标签
    lab_prompt.place(x=150, y=250)    # 设置标签位置

    self.entry = tkinter.Entry(self.root, font=('宋体', 20), width=15)   # 创建输入文本框
    self.entry.place(x=120, y=200)    # 设置输入文本框位置

    r1 = tkinter.Radiobutton(self.root, text='英译中', variable=self.radiolist, value=0, command=self.select1, bg='yellow')   # 创建单选按钮组
    r2 = tkinter.Radiobutton(self.root, text='中译英', variable=self.radiolist, value=1, command=self.select2, bg='yellow')   # 创建单选按钮组
    r3 = tkinter.Radiobutton(self.root, text='拼写填空', variable=self.radiolist, value=2, command=self.select3, bg='yellow')   # 创建单选按钮组
    self.radiolist.set(0)   # 设置单选按钮组默认选项
    r1.place(x=40, y=130)    # 设置单选按钮组位置
    r2.place(x=40, y=150)    # 设置单选按钮组位置
    r3.place(x=40, y=170)    # 设置单选按钮组位置
    but1 = tkinter.Button(self.root, text='确定', width=5, font=('宋体', 15), command=self.judge)   # 创建按钮
    but1.place(x=130, y=300)    # 设置按钮位置
    but2 = tkinter.Button(self.root, text='退出', width=5, font=('宋体', 15), command=self.root.exit)   # 创建按钮
    but2.place(x=230, y=300)    # 设置按钮位置
    but3 = tkinter.Button(self.root, text='查看错词表', width=10, font=('宋体', 15), command=self.wrong_word)   # 创建按钮
    but3.place(x=130, y=400)    # 设置按钮位置

# 3．单词练习方式模块设计
"""
（1）根据练习的单选按钮，标签显示不同的内容。在文本输入框中输入相应的内容，单击“确定”按钮进行判断。
（2）由单选按钮的command事件链接到相应的方法中。
单选“英译中”：标签显示英文，随机显示单词表中的一个单词。
单选“中译英”：随机显示单词表中一个词语，标签显示中文。
单选“拼写填空”：单词字母随机缺少一个。利用随机数生成一个数字，遍历英文单词的字母，数字应对的位置替换为下画线，其他的字母正常显示。实现代码如下：
"""
def select1(self):
    self.r = random.randint(0, len(self.dic)-1)  # 创建随机数变量（用于从单词表中随机抽取单词）
    self.word.set(self.dic[self.r][0])  # 设置显示单词变量
def select2(self):
    self.r = random.randint(0, len(self.dic)-1)  # 创建随机数变量（用于从单词表中随机抽取单词）
    self.word.set(self.dic[self.r][1])  # 设置显示单词变量
def select3(self):
    self.r = random.randint(0, len(self.dic)-1)  # 创建随机数变量（用于从单词表中随机抽取单词）
    word = self.dic[self.r][0]  # 设置显示单词变量
    k = random.randint(0, len(word)-1)  # 创建随机数变量（用于从单词中随机抽取字母）
    self.space = ''     # 创建空格
    for i in range(len(word)):  # 遍历英文单词的字母
        if i != k:  # 数字应对的位置替换为下画线
            self.space += word[i]   # 其他的字母正常显示
        else:
            self.space += '_'
            self.fill = word[k]     # 创建拼写填空的变量
    self.space = self.space + '' + self.dic[self.r][1]  # 设置显示单词变量
    self.word.set(self.space)   # 设置显示单词变量

# 4．正误判断设计
"""
先判断练习方式是哪一种，再获取文本框输入的内容，将获取的内容与对应的单词表内容进行比对，如果相同，则增加积分，给出赞扬提示；如果不同，则给出鼓励提示，并将对应单词加到错词表。
1）若为拼写填空模式
获取文本框输入内容（如果不区分大小写，则统一变成小写）。如果输入内容与空缺内容相同，则给出赞扬提示，增加积分，将积分变量进行更新并显示在标签中。
如果输入内容与空缺内容不同，则给出鼓励提示，将单词追加到错词列表，再次生成随机数，用于下一轮的单词抽取，调用拼写填空方法，并将文本输入框的内容清空。
2）若为中译英或英译中
如果为中译英模式，设c=1，即与文本框内容匹配的是列表中的索引号为1，提取词语中的中文。如果为英译中模式，设c=0，即与文本框内容
匹配的是列表中的索引号为0，提取单词中的英文。将文本框内容与提取到的内容进行比对，如果相同，则给出赞扬提示，增加积分，更新积分并显示。如果不同，则给出鼓励提示，将单词追加到错词表。再次生成随机数，用于下一轮单词抽取，将抽取到的单词更新并显示出来，清空文本框中的内容。
实现代码如下：
"""
def judge(self):
    if self.radiolist.get() == 2:  # 若为拼写填空模式
        s = self.entry.get().lower()    # 获取文本框输入内容（如果不区分大小写，则统一变成小写）
        if s == self.fill:  # 如果输入内容与空缺内容相同
            self.prompt.set('你真棒')   # 给出赞扬提示
            self.fen += 1  # 增加积分
            self.score.set(self.fen)    # 将积分变量进行更新并显示在标签中
        else:
            self.prompt.set('很遗憾,加油')
            self.wrong.append(self.dic[self.r])    # 将单词追加到错词列表
        self.r = random.randint(0, len(self.dic)-1)  # 再次生成随机数，用于下一轮的单词抽取
        self.select3()  # 调用拼写填空方法
        self.entry.delete(0, 'end')     # 将文本输入框的内容清空
    else:
        if self.radiolist.get() == 0:   # 若为中译英模式
            e = 0
            c = 1
        elif self.radiolist.get() == 1:   # 若为英译中模式
            e = 1
            c = 0
        word = self.dec[self.r][c]  # 提取词语中的中文

        s = self.entry.get()    # 获取文本框输入内容
        if word == s:   # 如果输入内容与空缺内容相同
            self.prompt.set('你真棒')   # 给出赞扬提示
            self.fen += 1  # 增加积分
            self.score.set(self.fen)    # 将积分变量进行更新并显示在标签中
        else:
            self.prompt.set('很遗憾,加油')
            self.wrong.append(self.dic[self.r])
        self.r = random.randint(0, len(self.dic)-1)  # 再次生成随机数，用于下一轮的单词抽取
        self.word.set(self.dic[self.r][e])  # 将抽取到的单词更新并显示出来
        self.entry.delete(0, 'end')     # 将文本输入框的内容清空

# 5．退出设计
"""
单击“退出”按钮，退出程序，代码如下：
"""
def exit(self):
    self.root.destroy()

# 6．错词表设计
"""
单击“查看错词表”按钮调用错词方法，打开新的窗口，原窗口隐藏。在新窗口将错词表中的内容以表格的形式列出来，并显示错误次数。
（1）隐藏原窗口，创建新窗口，显示标题：标签。
（2）创建表格：表格位置、列数目3，列标题。
（3）遍历错词表，统计错词出现的次数：
①对错词表进行排序，让相同的单词相邻。
②在错词表末尾追加一个符号，用于遍历结束，便于统计次数。
③获取错词中的第一个单词，并设出现次数为1，从第二个单词开始对单词表进行遍历。
④如果单词与第一个单词相同，则将次数加1。如果不同，则将单词的英文、中文、次数写入表格中并显示，同时将次数修改为1，第一个单词的变量值改为当前单词。将添加的符号删除，以防止下次对它进行统计。
实现代码如下：
"""
def wrong_word(self):
    self.root.withdraw()    # 隐藏原窗口
    self.wt = tkinter.Tk()  # 创建新窗口
    self.wt.title('错词表')     # 设置窗口标题
    self.wt.geometry('400x500')     # 设置窗口大小
    self.wt['bg'] = 'yellow'    # 设置窗口背景颜色
    lab_wr = tkinter.Label(self.wt, text='本次练习错词表', font=('宋体', 20), bg='yellow')   # 创建标签
    lab_wr.place(x=100, y=10)   # 设置标签位置
    tree = ttk.Treeview(self.wt, show='headings', height=15)   # 创建表格
    tree.place(x=30, y=50)    # 设置表格位置
    tree['columns'] = ['1', '2', '3']   # 设置表格列数目
    tree.column('1', width=110)  # 设置表格列
    tree.column('2', width=110)  # 设置表格列
    tree.column('3', width=100)  # 设置表格列

    tree.heading('1', text='英文', anchor='center')     # 设置表格列标题
    tree.heading('2', text='中文', anchor='center')     # 设置表格列标题
    tree.heading('3', text='错误次数', anchor='center')     # 设置表格列标题

    but_re = tkinter.Button(self.wt, text='返回', font=('宋体', 15), command=self.back) # 创建按钮
    but_re.place(x=150, y=400)  # 设置按钮位置
    self.wrong.sort(key=lambda x:x[0])   # 对错词表进行排序，让相同的单词相邻
    self.wrong.append(['', ''])    # 在错词表末尾追加一个符号，用于遍历结束，便于统计次数
    p = self.wrong[0][0]    # 获取错词中的第一个单词
    c = 1   # 设出现次数为1
    for w in range(1, len(self.wrong)):    # 从第二个单词开始对单词表进行遍历
        if self.wrong[w][0] == p:   # 如果单词与第一个单词相同
            c += 1  # 将次数加1
        else:
            tree.insert('', 'end', values=(self.wrong[w-1][0], self.wrong[w-1][1], c))
            print('{}\t{}\t{}'.format(self.wrong[w][0], self.wrong[w][1], c))
            c = 1   # 将次数修改为1
            p = self.wrong[w][0]    # 第一个单词的变量值改为当前单词
    self.wt.protocol('WM_DELETE_WINDOW', self.back)  # 将添加的符号删除，以防止下次对它进行统计
# 7．返回设计
"""
关闭（销毁前一个）destroy（），更新、显示原隐藏主界面update（）、deiconify（）。代码如下：
"""
def back(self):
    self.wt.destroy()
    self.root.update()
    self.root.deiconify()
