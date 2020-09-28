"""
n个盘子时
    把n-1个圆盘从A经过C移动到B
    把第n个圆盘从A移动到C
    把n-1个小圆盘从B经过A移动到C

汉诺塔移动次数的递推式：h(x)=2h(x-1)+1
"""


def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print('moving from %s to %s' % (a, c))
        hanoi(n-1, b, a, c)


hanoi(3, 'A', 'B', 'C')
