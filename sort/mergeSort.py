# -*- coding:utf-8 -*-
def merge_sort(alist):
    """
    归并排序
    :param alist: 无序列表, []
    :return: 有序列表, []
    """
    if len(alist) < 2:
        return alist
    result = []
    mid = len(alist) // 2

    left = merge_sort(alist[:mid])
    right = merge_sort(alist[mid:])

    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))

    result.extend(left + right)
    return result


if __name__ == "__main__":
    import random

    li = range(10000)
    random.shuffle(li)
    assert merge_sort(li) == sorted(li)
