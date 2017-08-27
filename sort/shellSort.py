# *-* coding; utf-8 *-*
def shell_sort(alist):
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

    origin_list = [i + random.randint(0, 500) for i in range(50)]
    print("origin_list is:", origin_list)
    print("insertion_sort:", shell_sort(origin_list))
