# -*- coding: utf-8 -*-
import time

def insert_sort_by_recusive(seq, i):
    """
    插入排序的递归实现,
    默认从第一个开始排序
    :param i 排序到哪个位置
    :param seq 待排序的序列
    :return seq
    """
    if i == 0: return seq
    insert_sort_by_recusive(seq, i-1)
    j = i
    while j > 0 and seq[j-1] > seq[j]:
        seq[j-1], seq[j] = seq[j], seq[j-1]
        j -= 1

    return seq


def insert_sort_by_loop(seq):
    """
    通过对列表进行循环，进行列表的排序
    插入排序，默认第一个元素是排序Ok的，
    取出下一个元素，在已经排序的元素列表中从后往前扫描
    如果该元素大于新元素，则将元素移到下一个位置
    """
    if len(seq) <= 1: return seq

    for i in xrange(len(seq)-1):
        j = i
        while j > 0 and seq[j-1] > seq[j]:
            seq[j-1], seq[j] = seq[j]
            j -= 1
    return seq


if __name__ == "__main__":
    seq = input("please input a seq: ")
    i = len(seq) - 1

    x1 = time.time()
    print insert_sort_by_recusive(seq, i)
    print "recusive cost time is %s" % (time.time() - x1)

    x2 = time.time()
    print insert_sort_by_loop(seq)
    print "sort by loop cost time is %s" % (time.time() - x2)


