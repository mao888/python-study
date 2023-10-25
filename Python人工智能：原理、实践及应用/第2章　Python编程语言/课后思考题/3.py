"""
3.汉诺塔是一个数学难题，其问题描述为如何将所有圆盘从A盘借助B盘移动到C盘。请用Python编写程序实现汉诺塔的移动。要求输入汉诺塔的层数，输出整个移动的流程。
"""
def hanoi_tower(n, source, auxiliary, target):
    if n == 1:
        print(f"移动圆盘 {n} 从 {source} 到 {target}")
        return
    hanoi_tower(n - 1, source, target, auxiliary)
    print(f"移动圆盘 {n} 从 {source} 到 {target}")
    hanoi_tower(n - 1, auxiliary, source, target)

def main():
    try:
        num_disks = int(input("请输入汉诺塔的层数: "))
        if num_disks < 1:
            print("汉诺塔的层数必须大于等于1")
        else:
            hanoi_tower(num_disks, 'A', 'B', 'C')
    except ValueError:
        print("请输入一个有效的整数")

if __name__ == "__main__":
    main()
