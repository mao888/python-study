"""
2.编写程序实现最大公约数和最小公倍数计算。
"""
# 方法一
import math

# 输入两个整数
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))

# 计算最大公约数
gcd_result = math.gcd(num1, num2)   # gcd: greatest common divisor

# 计算最小公倍数
lcm_result = (num1 * num2) // gcd_result    # lcm: least common multiple

# 输出结果
print(f"最大公约数是: {gcd_result}")
print(f"最小公倍数是: {lcm_result}")

print("--------------------------------------------------")
# 方法二:  也可以自己写一个函数
# 最大公约数是
def gcd(num1, num2):
    # if num1 < num2:
    #     num1, num2 = num2, num1
    while num2 != 0:
        num1, num2 = num2, num1 % num2
    return num1

# 最小公倍数是
def lcm(num1, num2):
    return (num1 * num2) // gcd(num1, num2)

# 输入两个整数
num1 = int(input("请输入第一个整数: "))
num2 = int(input("请输入第二个整数: "))
# 计算最大公约数
gcd_result = gcd(num1, num2)
# 计算最小公倍数
lcm_result = lcm(num1, num2)
# 输出结果
print(f"最大公约数是: {gcd_result}")
print(f"最小公倍数是: {lcm_result}")