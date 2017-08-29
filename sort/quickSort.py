# -*- coding:utf-8 -*-
def quick_sort(alist, left, right):
    """
    快速排序
    :param alist: 无序列表, []
    :param left: int
    :param right: int
    :return: 有序列表, []
    """
    if left > right:
        return
    key = left
    for i in range(left+1, right+1):
        if alist[key] > alist[i]:
            tmp = alist[i]
            del alist[i]
            alist.insert(key, tmp)
            key = key + 1
    quick_sort(alist, left, key-1)
    quick_sort(alist, key+1, right)

if __name__ == "__main__":
    import random
    from copy import deepcopy

    li = range(100)
    random.shuffle(li)
    li2 = deepcopy(li)
    quick_sort(li, 0, len(li) - 1)
    assert li == sorted(li2)