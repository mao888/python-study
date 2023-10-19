"""
从前面的案例中我们发现函数可以通过封装实现代码复用。函数是程序的一种抽象，可以利用函数对程序进行模块化设计。
程序是由一系列代码组成的，如果代码只有顺序而没有组织，不仅不利于阅读和理解，也很难进行升级和维护。因此，需要对代码进行抽象，形成易于理解的结构。
当代编程语言从代码层面采用函数和对象两种抽象方式，分别对应面向过程和面向对象编程思想。
函数是程序的一种基本抽象方式，它将一系列的代码组织起来，通过命名供其他程序使用。函数封装的直接好处是代码可复用。具体表现在任何其他的代码只要使用函数名，输入参数即可调用函数，从而避免了相同功能代码在调用处的重复编写。
代码复用又产生另一优势，当更新函数功能时，所有被调用处的功能都被更新。
面向过程是一种以过程描述为主要方法的编程方式，它要求程序员列出解决问题所需要的步骤，然后用函数将这些步骤一步一步地实现，使用时依次建立并调用函数或编写语句即可。面向过程编程是一种基本且自然的程序设计方法，函数通过封装步骤或子功能实现代码复用，并简化程序设计难度。
面向过程和面向对象只是编程方式不同，抽象级别不同，所有面向对象编程能实现的功能采用面向过程同样能实现。
当程序的长度较长，如超过百行以上，如果不划分模块，程序的可读性就会非常差。解决这一问题的最好方法就是将一个程序分隔成短小的程序段，每一段程序完成一个小的功能。无论面向过程还是面向对象编程，对程序合理划分功能模块并基于模块设计程序是一种常用的方法，称为“模块化程序设计”。
模块化程序设计是指通过函数或对象的封装功能将程序划分成主程序、子程序和子程序间关系的表达。模块化设计是使用函数和对象设计程序的思考方法，以功能块为基本单位，一般有两个基本要求：
（1）高内聚。尽可能地合理划分功能块，功能块内部耦合紧密。
（2）低耦合。模块间尽可能简单，功能块之间耦合度低。
耦合是指两个实体相互依赖于对方的一个量度，在程序设计结构中是指各模块之间相互关联的程序。也就是在设计系统的各个功能模块时，尽可能使模块具有较大的独立性，使得每个模块完成一个相对独立的特定子功能，并且和其他模块之间的关系很简单，以便能方便地把不同场合下写成的程序模块组合成软件系统。
衡量模块独立性的定性标准是内聚（一个模块内各个元素彼此结合的紧密程度）和耦合（一个软件结构内不同模块之间互连程度的度量）。高内聚、低耦合的模块是设计时追求的目标。尽量降低系统各个部分之间的耦合度，是应用服务层设计中需要重点考虑的问题。
模块化编程可采用以下步骤进行：
（1）分析问题，明确需要解决的任务。
（2）对任务进行逐步分解和细化，分成若干个子任务，每个子任务只完成部分完整功能，并且可以通过函数实现。
（3）确定模块（函数）之间的调用关系。
（4）优化模块之间的调用关系。
（5）在主函数中进行调用实现。
模块与模块之间可以相互调用。假设模块1、模块2的程序文件分别在同一个目录下保存为文件名 module1.py 、 module2.py ，则在模块2中调用模块1的形式有
（1）import module1。
（2）from module1 import∗。
例如创建Python文件a.py，并在文件中定义函数sum，代码如下：
def sum(a,b):
    return a+b
创建Python文件b.py，并调用sum函数，代码如下：
from a import sum
print(sum(1,2))
"""