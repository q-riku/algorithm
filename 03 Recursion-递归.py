"""
递归的两个特点：调用自身，结束条件
"""


# ========== example ==========
def func1(x):
    print(x)
    func1(x-1)  # wrong


def func2(x):
    if x > 0:
        print(x)
        func2(x+1)  # wrong


def func3(x):
    if x > 0:
        print(x)
        func3(x-1)  # x=3时输出3 2 1


def func4(x):
    if x > 0:
        func4(x-1)
        print(x)  # x=3时输出1 2 3
