# 1．属性
"""
属性用于描述事物的特征，如颜色、大小、数量等。可以分为类属性和对象属性。
类的属性存储了类的各种数据，定义位置有类的内部和方法的外部，由该类所有的对象共同拥有。类属性可以通过类名访问，也可以通过对象名访问，但只能通过类名修改。
对象属性是对象特征的描述，定义非常灵活，可在方法内部定义，也可在调用实例时添加。如给上面的冰箱类定义两个属性：冰箱编号、物品编号，再定义一个对象属性：物品名称，代码如下：
"""


class Fridge():
    No = 0  # 类属性--冰箱编号
    Num = 0  # 类属性--物品编号

    def pack(self, goods):
        self.Num += 1
        self.goods = goods  # 对象属性--物品名称


"""
在开发过程中经常会遇到不想让对象的某些属性不被外界访问和随意修改的情况，这时可将这些属性定义为私有属性，再添加一个公有方法，用于私有属性的操作。私有属性定义以“__”开头，如__age。
"""
# 2．构造方法
"""
在类的方法中，有两种特殊方法，分别在类创建时和销毁时自动调用，分别是构造方法__init__（）和析构方法__del__（）。
使用类名（）可以创建对象，但实际上，每次创建对象后，系统会自动调用__init__（）方法。每个类都有一个默认的构造方法，如果在自定义类时显示已经定义了，则创建对象时调用定义的__init__（）方法。
__init__（）方法的第一个参数是self，即代表对象本身，不需要显式传递实参。但是在创建类时传入的参数实际上都传递给了__init__（）方法。代码如下：
"""


class Fridge():
    No = 0
    Num = 0

    def __init__(self):  # 自定义构造方法
        Fridge.No += 1

# 3．对象方法
"""
对象方法是在类中定义的，以关键字self作为第一个参数。在对象方法中可以使用self关键字定义和访问对象属性，同时对象属性会覆盖类属性。
冰箱类中的开门、装物品、关门都是对象方法，代码如下：
"""
class Fridge():
    No = 0  # 类属性 -- 冰箱编号
    Num = 0 # 类属性 -- 物品编号

    def __init__(self): # 自定义构造方法
        Fridge.No += 1  # 冰箱编号自动加1

    def open(self): # 冰箱方法 -- 开门
        print("打开 %d 号冰箱门" % Fridge.No)

    def pack(self, goods):  # 冰箱方法 -- 装物品
        self.Num += 1
        self.goods = goods  # 对象属性 -- 物品名称
        print("在 %d 号冰箱中装入第 %d 件物品：%s" % (self.No, self.Num, self.goods))
    def close(self):    # 冰箱方法 -- 关门
        print("关闭 %d 号冰箱门" % Fridge.No)
Fridge1 = Fridge()  # 创建冰箱对象1
Fridge1.open()  # 调用对象方法 -- 开门
Fridge1.pack("大象")  # 调用对象方法 -- 装物品
Fridge1.pack("狮子")  # 调用对象方法 -- 装物品
Fridge1.close()  # 调用对象方法 -- 关门