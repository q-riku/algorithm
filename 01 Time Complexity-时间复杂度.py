"""
·时间复杂度：用来估计算法运行（时间）效率的一个式子（单位）
·一般来说，时间复杂度高的算法比复杂度低的算法慢
·常见的时间复杂度（按效率排序）：
    O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^2logn)<O(n^3)
·复杂问题的时间复杂度：
    O(n!) O(2^n) O(n^n)
·快速判断算法复杂度（适用于绝大多数简单情况）：
    确定问题规模n
    循环减半过程->logn
    k层关于n的循环->n^k
    复杂情况：根据算法执行过程判断
"""


# ========== example ==========
n = 10
print('Hello World')  # O(1)

for i in range(n):
    print('Hello World')  # O(n)

for i in range(n):
    for j in range(n):
        print('Hello World')  # O(n^2)

for i in range(n):
    for j in range(n):
        for k in range(n):
            print('Hello World')  # O(n^3)

print('Hello World')
print('Hello Python')
print('Hello Algorithm')  # O(1)

for i in range(n):
    print('Hello World')
    for j in range(n):
        print('Hello World')  # O(n^2)

while n > 1:
    print(n)
    n = n//2  # O(log2n)/O(logn) 2为底数
# 当算法过程出现循环折半的时候，复杂度式子中会出现logn
