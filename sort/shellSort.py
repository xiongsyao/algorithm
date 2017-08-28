# -*- coding:utf-8 -*-
def shell_sort(alist):
    """
    希尔排序(当最终步长为1时极为插入排序)
    :param alist: 无序列表, []
    :return: 有序列表, []
    """
    step = len(alist) // 2  # 定义步长
    while step > 0:
        for index in range(step, len(alist)):
            while index > step-1 and alist[index] < alist[index - step]:
                alist[index], alist[index - step] = alist[index - step], alist[index]
                index = index - step
        step = step // 2
    return alist


if __name__ == "__main__":
    import random

    li = range(10000)
    random.shuffle(li)
    print("origin_list is:", li)
    print("insertion_sort:", shell_sort(li))
