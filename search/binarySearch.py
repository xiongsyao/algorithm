# *-* coding:utf-8 *-*


def binary_search1(alist, item):
    """
    二分搜索.
    :param alist:有序列表, []
    :param item:待搜索目标, str
    """
    first = 0
    last = len(alist) - 1
    found = False
    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found


def binary_search2(alist, item):
    """
    二分搜索递归版
    :param alist: 有序列表, []
    :param item: 待搜索目标, str
    """
    if len(alist) == 0:
        return False
    midpoint = len(alist) // 2
    if alist[midpoint] == item:
        return True
    if item < alist[midpoint]:
        return binary_search2(alist[:midpoint], item)
    else:
        return binary_search2(alist[midpoint + 1:], item)


if __name__ == '__main__':
    import random
    sorted_list = [41, 55, 76, 87, 88, 99, 123, 432, 546, 577, 688, 786]
    target = random.choice(sorted_list)
    print("***the alist is:", sorted_list)
    print("***the target is:", target)
    print(binary_search1(sorted_list, target))
    print(binary_search2(sorted_list, target))
