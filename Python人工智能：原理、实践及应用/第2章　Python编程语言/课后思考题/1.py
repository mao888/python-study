"""
1.编写isprime（）函数，参数为整数，并且需要有异常处理功能。此函数的功能是检测接收的整数是否为质数，如果整数是质数，则返回True，否则返回False。
"""
def isprime(n):
    try:
        n = int(n) #尝试将输入转换为整数
    except ValueError: #如果无法转换为整数，抛出异常
        print("输入必须是整数")
        return False

    if n <= 1: #1和0都不是质数
        return False
    elif n <= 3: #2和3是质数
        return True
    elif n % 2 == 0 or n % 3 == 0: #能被2或3整除的不是质数
        return False
    i = 5
    while i * i <= n: #只需检查到sqrt(n)，节省计算资源
        if n % i == 0 or n % (i + 2) == 0: #如果n能被i或i+2整除，则n不是质数
            return False
        i += 6 #只检查6n+1和6n-1的形式，节省计算资源
    return True

# 测试用例
print(isprime(7))  # 应返回 True，因为7是质数
print(isprime(10))  # 应返回 False，因为10不是质数
print(isprime(-5))  # 应返回 False，并显示错误消息
print(isprime(1))  # 应返回 False，并显示错误消息
