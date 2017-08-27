# *-* coding:utf-8 *-*
import time


def python_search(arg, item):
    """
    利用python内置列表的函数index实现搜索
    复杂度取决于list.index(),为O(1)
    :param arg: 生成的有序列表长度, int
    :param item: 待搜索目标, int
    :return: True or False
    """
    print("******generate alist******")
    alist = [i for i in range(arg)]
    print("*******start search*******")
    start_time = time.time()
    try:
        index = alist.index(item)
        end_time = time.time()
        print("pythonSearch spend:", end_time - start_time)
        return True
    except ValueError:
        end_time = time.time()
        print("pythonSearch spend:", end_time - start_time)
        return False

if __name__ == "__main__":
    print(python_search(3000, 1994))
