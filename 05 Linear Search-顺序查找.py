"""
·查找：在一些数据元素中，通过一定的方法找出与给定关键字相同的数据元素的过程
·列表查找（线性表查找）：从列表中查找指定元素
    输入：列表、待查找元素
    输出：元素下标（未找到元素时一般返回None或-1）
·内置列表查找函数：index()

===============================================================================
·顺序查找（Linear Search）
    也叫线性查找，从列表第一个元素开始，顺序进行搜索，直到找到元素或搜索到列表最后一个元素为止
    时间复杂度：O(n)
"""


# ========== example ==========
def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


def linear_search2(data_set, value):
    for i in range(len(data_set)):
        if data_set[i] == value:
            return i
    return
