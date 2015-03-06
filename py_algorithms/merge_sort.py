# -*- coding: utf-8 -*-


def merge_sort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = merge_sort(lft)
    if len(rgt) > 1: rgt = merge_sort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res


if __name__ == "__main__":
    # 归并排序工作原理如下：
    # 1. 首先将序列分分成两个序列，设定各自序列的起始和终止位置
    # 2. 比较两个序列的元素最大元素,选择相对叫大的放入到列表中
    # 3. 重复步骤２，直到所有元素排序完毕

    # 该算法的时间复杂度是O(nlogn)
    # 最优时间复杂度O(n)
    # 最差时间复杂度O(nlogn)

    # [10, 20, 17, 19, 3, 8, 18]
    seq = input("please input seq: ")
    print merge_sort(seq)
