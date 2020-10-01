"""
18.0 基数排序（Radix Sort）

·多关键字排序
    假如现在有一个员工表，要求按照薪资排序，年龄相同的员工按照年龄排序（先按照年龄进行排序，再按照薪资进行稳定的排序）
·时间复杂度：O(kn) k表示数字位数
·空间复杂度：O(k+n)

===============================================================================
===============================================================================
"""


# ========== example ==========
def radix_sort(li):
    max_num = max(li)  # 最大值 99->2 888->3 10000->5
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        # 分桶
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        li.clear()
        # 把数重新写回li
        for buc in buckets:
            li.extend(buc)
        it += 1


li = list(range(10))
import random
random.shuffle(li)
print(li)
radix_sort(li)
print(li)
