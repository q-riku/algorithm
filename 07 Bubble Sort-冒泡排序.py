"""
·排序：将一组“无序”的记录序列调整为“有序”的记录序列
·列表排序：将无序列表变为有序
    输入：列表
    输出：有序列表
·升序与降序
·内置排序函数：sort()
·常见排序算法
    冒泡排序、选择排序、插入排序 ---> 时间复杂度都是O(n^2)，都是原地排序（即不增加新列表）
    快速排序、堆排序、归并排序
    希尔排序、计数排序、基数排序

===============================================================================
·冒泡排序（Bubble Sort）
    列表每两个相邻的数，如果前面比后面大，则交换这两个数
    一趟排序完成后，则无序区减少一个数，有序区增加一个数
    代码关键点：趟、无序区范围
    时间复杂度：O(n^2)
·冒泡排序的优化
    如果冒泡排序中的一趟排序没有发生交换，则说明列表已经有序，可以直接结束算法
"""


# ========== example ==========
def bubble_sort(li):
    for i in range(len(li) - 1):  # 第i趟
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:  # >升序，<降序
                li[j], li[j + 1] = li[j + 1], li[j]
        print(li)


li = [3, 2, 4, 6, 5, 9, 8, 7, 1]
print(li)
bubble_sort(li)
print('===========================')


def bubble_sort2(li):
    for i in range(len(li) - 1):  # 第i趟
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:  # >升序，<降序
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        print(li)
        if not exchange:
            return


li = [9, 8, 7, 1, 2, 3, 4, 5, 6]
print(li)
bubble_sort2(li)