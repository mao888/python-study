
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