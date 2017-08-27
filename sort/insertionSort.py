# *-* coding; utf-8 *-*
def insertion_sort(alist):
    """
    插入排序
    :param alist: 无序列表, [] 
    :return: 有序列表, []
    """
    for index in range(1, len(alist)):
        while index > 0 and alist[index - 1] > alist[index]:
            alist[index], alist[index - 1] = alist[index - 1], alist[index]
            index = index - 1
    return alist


if __name__ == "__main__":
    import random

    origin_list = [i + random.randint(0, 500) for i in range(50)]
    print("origin_list is:", origin_list)
    print("insertion_sort:", insertion_sort(origin_list))
