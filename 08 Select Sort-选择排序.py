"""
·选择排序（Select Sort）
    一趟排序记录最小的数，放到第一个位置
    再一趟排序记录列表无序区最小的数，放到第二个位置
    ……
    算法关键点：有序区和无序区、无序区最小数的位置
    时间复杂度：O(n^2)
"""


# ========= example ==========
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


li = [3, 2, 4, 1, 5, 6, 8, 7, 9]
print(select_sort_simple(li))


def select_sort(li):
    for i in range(len(li) - 1):  # 第i躺
        min_loc = i
        for j in range(i+1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        if min_loc != i:
            li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [3, 4, 2, 1, 5, 6, 8, 7, 9]
print(li)
select_sort(li)
