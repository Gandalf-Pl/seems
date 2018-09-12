# coding: utf8


def quick_sort(list_a):
    """
    quick sort
    """
    if len(list_a) <= 1:
        return list_a

    point = list_a[0]

    return quick_sort(filter(lambda x: x <= point, list_a[1:])) \
           + [point] + quick_sort(filter(lambda x: x > point, list_a[1:]))


if __name__ == "__main__":

    # 快速排序
    # 1: 从列表中选出一个元素作为基准point
    # 2: 重新排序列表,所有比这个元素小的都摆在前面,比这个元素大的摆在后面,这个称为分治
    # 3: 递归地把小于基准值和大于基准值的子数列排序
    # 最差时间复杂度为n * n, 最优时间复杂度为nlogn 平均时间复杂度为nlogn
    tmp_list = input("please input list: ")
    print quick_sort(tmp_list)
