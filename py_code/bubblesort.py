# -*- coding: utf-8 -*-

def bubble_sort(seq):
    for j in range(len(seq)-1, 0, -1):
        for i in range(j):
            if seq[i] > seq[i+1]:
                seq[i], seq[i+1] = seq[i+1], seq[i]
    return seq


if __name__ == "__main__":
    # 冒泡排序

    # 比较相邻的两个元素,如果第一个比第二个大
    # 就交换他们两个

    # 对第0个到第n-1个数据做同样的工作，这样最大的数就
    # 浮到了数组的最后面

    # 针对所有的元素重复上面的步骤，除了最后一个
    # 持续每次对越来越少的元素重复上面的步骤，
    # 直到没有任何一对数字需要比较

    seq = input("please input a seq: ")
    print bubble_sort(seq)

