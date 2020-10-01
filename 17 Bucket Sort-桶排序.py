"""
17.0 桶排序（Bucket Sort）

·在计数排序中，元素范围比较大（如在1到1亿之间）
·桶排序：首先将元素分在不同的桶中，再对每个桶中的元素排序
·桶排序的表现取决于数据的分布，也就是需要对不同数据排序时采取不同的分桶策略
·平均情况时间复杂度：O(n+k)；最坏情况时间复杂度：O(n^2k)
·空间复杂度：O(nk)

===============================================================================
===============================================================================
"""


# ========== example ==========
def bucket_sort(li, n=100, max_num=10000):  # n个桶
    buckets = [[] for _ in range(n)]  # 创建桶
    for var in li:
        i = min(var // (max_num // n), n - 1)  # i表示var放到几号桶里
        buckets[i].append(var)  # 把var加到桶里
        for j in range(len(buckets[i]) - 1, 0, -1):  # 保持桶内顺序
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


import random
li = [random.randint(0, 10000) for i in range(15)]
print(li)
li = bucket_sort(li)
print(li)