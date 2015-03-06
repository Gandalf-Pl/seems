# -*- coding: utf-8 -*-

def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i-1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            i -= 1
    return seq



if __name__ == "__main__":
    # 地精排序算法，只有ｙｉ层循环，
    # 默认情况下前进冒泡，
    # 一旦遇到冒泡的情况发生就往回冒泡,
    # 直到所有的排序完成，时间复杂度是O(n**2)
    # [10, 20, 17, 19, 3, 8, 18]
    seq = input("please input a seq: ")
    print gnomesort(seq)

