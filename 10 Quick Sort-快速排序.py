"""
10.0 快速排序（Quick Sort）

·取一个元素p（第一个元素），使元素p归位
-->列表被p分成两部分，左边都比p小，右边都比p大
-->递归完成排序
·快速排序框架:
    def quick_sort(data, left, right):
        if left < right:
            mid = partition(data, left, right)
            quick_sort(data, left, mid - 1)
            quick_sort(data, mid + 1, right)
·时间复杂度：O(nlogn)
·快速排序的问题：最坏情况（e.g.倒序列表的情况O(n^2)），递归最大深度

===============================================================================
===============================================================================
"""


# ========== example ==========
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右边找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边的空位上
        print(li)
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边的空位上
        print(li)
    li[left] = tmp  # 把tmp归位
    return left


def quick_sort(li, left, right):
    if left < right:  # 至少两个元素
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = [5, 7, 4, 6, 3, 1, 2, 9, 8]
li2 = [7, 2, 8, 4, 6, 7, 5, 6, 4, 9]
# print(li2)
partition(li, 0, len(li) - 1)
# quick_sort(li2, 0, len(li2) - 1)
print(li)
