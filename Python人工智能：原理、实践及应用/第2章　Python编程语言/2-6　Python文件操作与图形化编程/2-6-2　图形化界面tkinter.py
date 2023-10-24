"""
tkinter是使用Python进行窗口视窗设计的模块。
tkinter模块（＂Tk接口＂）是Python的标准Tk GUI工具包的接口。
作为Python特定的GUI界面，它是一个图像的窗口，并且tkinter是Python自带的模块，可以编辑GUI界面，并且可以用GUI实现很多直观的功能，例如开发一个计算器或者开发一个有交互功能的小系统。
由于tkinter是Python内置的库，不用安装，所以只需在使用时导入tkinter模块：import tkinter，或者from tkinter import∗。
需要说明的是，虽然tkinter很好用，但是如果要开发一些大型的应用，tkinter提供的功能还是太少了，需要使用wxPython、PyQt这些第三方库。
"""
# 1．主窗体创建与运行
"""
图形用户界面程序都需要一个根窗口，也叫主窗口，它就好像绘画时需要的画纸一样，tkinter提供创建主窗口的构造函数Tk（），创建语句代码如下：
"""
from tkinter import *

root = Tk()
"""
窗口和组件都创建好后，需要运行，程序要不停地告诉窗口管理对象GM（Geometry Manager）有一个组件产生，其方法代码如下：
"""
root.mainloop()

# 2．tkinter的组件
"""
tkinter提供了许多组件，其中较常用的组件如表2-18所示。
"""
"""
表2-18　tkinter常用组件
组件	    元素      描述
Frame	框架	    用于在屏幕上显示一个矩形区域，多用于作为容器
Label	标签	    用于显示文本或图像
Button	按钮	    用于触发事件
Entry	输入框	    用于显示简单的文本内容
Text	文本框	    用于显示多行文本内容
Checkbutton	复选框	用于显示一个复选框
Radiobutton	单选框	用于显示一个单选框
Canvas	画布	    用于绘制图形
Listbox	列表框	    用于显示一个列表
Menu    菜单	    用于显示一个菜单
Menubutton	菜单按钮	用于显示一个菜单按钮
Message	消息框	    用于显示多行文本内容
Scale	滑块	    用于显示一个滑块
Scrollbar	滚动条	用于显示一个滚动条
Toplevel	窗口	用于显示一个顶级窗口
messagebox	消息框	用于显示一个消息框
"""

# 3．组件属性
"""
标准属性也是所有组件的共同属性，如大小、字体、颜色等，除此之外，还有各组件自己特有的属性，常用的组件属性如表2-19所示。
"""
"""
表2-19　tkinter组件常用属性
选项(别名)    说明
background(bg)	设置组件的背景色
borderwidth(bd)    设置组件的边框宽度
cursor	设置鼠标在组件上的样式
font	设置组件的字体
foreground(fg)	设置组件的前景色
width	设置组件的宽度
height	设置组件的高度
anchor	设置组件的对齐方式   
command	设置组件的回调函数
image	设置组件的图像
pady    设置组件的内部高度
padx    设置组件的内部宽度
"""