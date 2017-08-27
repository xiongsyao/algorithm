# *-* coding:utf-8 *-*
import copy


def bubble_sort(alist):
    """
    冒泡排序
    :param alist: 无序列表, list
    :return: 排序后的列表, list
    """
    copy_list = copy.deepcopy(alist)  # 深拷贝传入的列表，防止污染下一个排序
    passnum = len(copy_list) - 1
    count = 0
    while passnum > 0:
        for i in range(passnum):
            if copy_list[i] > copy_list[i + 1]:
                copy_list[i], copy_list[i + 1] = copy_list[i + 1], copy_list[i]
        count = count + 1
        passnum = passnum - 1
    print("bubble_sort count is:", count)
    return copy_list


def short_bubble_sort(alist):
    """
    短路冒泡
    :param alist: 无序列表, list
    :return: 排序后的列表, list
    """
    copy_list = copy.deepcopy(alist)
    exchange = True
    passnum = len(copy_list) - 1
    count = 0
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if copy_list[i] > copy_list[i + 1]:
                copy_list[i], copy_list[i + 1] = copy_list[i + 1], copy_list[i]
                exchange = True
        count = count + 1
        passnum = passnum - 1
    print("short_bubble_sort count is:", count)
    return copy_list


if __name__ == "__main__":
    import random

    origin_list = [i + random.randint(0, 500) for i in range(50)]
    print("origin_list is:", origin_list)
    print("bubble_sort:", bubble_sort(origin_list))
    print("origin_list is:", origin_list)
    print("short_bubble_sort:", short_bubble_sort(origin_list))
