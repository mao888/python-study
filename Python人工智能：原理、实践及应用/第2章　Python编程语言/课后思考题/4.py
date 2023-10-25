"""
4.编写程序实现随机密码生成。要求在26个大小写字母和10个数字组成的列表中随机生成10个8位密码。
"""
import random
import string

# 定义密码生成函数
def generate_password(length=8):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# 生成10个密码
num_passwords = 10
passwords = [generate_password() for _ in range(num_passwords)]

# 输出生成的密码
for i, password in enumerate(passwords, 1):
    print(f"Password {i}: {password}")

"""
这个程序首先定义了一个generate_password函数，用于生成指定长度的密码。密码由大写字母、小写字母和数字组成，使用random.choice()函数从这些字符中随机选择字符生成密码。

然后，程序生成10个8位密码，并将它们存储在一个列表中。最后，它循环遍历生成的密码并输出它们。

运行程序后，你将获得10个不同的随机密码。
"""