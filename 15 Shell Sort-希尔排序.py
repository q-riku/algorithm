"""
15.0 希尔排序（Shell Sort)

·希尔排序是一种分组插入排序
·首先取一个整数d1=n/2，将元素分为d1个组，每组相邻两元素之间的距离为d1，在各组内进行直接插入排序
-->取第二个整数d2=d1/2，重复上述分组排序过程，直到di=1，即所有元素在同一组内进行直接插入排序
·希尔排序每趟并不使某些元素有序，而是使整体数据越来越接近有序，最后一趟排序使得所有数据有序
·希尔排序的时间复杂度比较复杂，且和选取的gap序列有关

===============================================================================
===============================================================================
"""


# ========== example ==========
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):  # i表示摸到的牌的下标
        tmp = li[i]
        j = i - gap  # j表示手里的牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


li = list(range(10))
import random
random.shuffle(li)
print(li)
shell_sort(li)
print(li)
