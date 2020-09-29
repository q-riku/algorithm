"""
06.0 二分查找（Binary Search）

·又叫折半查找，从【有序】列表的初始候选区li[0:n]开始，通过对待查找的值与候选区中间值的比较，可以使候选区减少一半
·时间复杂度：O(logn)

===============================================================================
===============================================================================
"""


# ========== example ==========
def binary_search(li, val):
    left = 0
    right = len(li) - 1
    while left <= right:  # 候选区有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:  # 待查找的值在mid左侧
            right = mid - 1
        else:  # li[mid]<val
            left = mid + 1
    else:
        return None


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(li, 3))
