# -*- coding: utf-8 -*-
# 链表


class Node(object):
    def __init__(self, value, next=None):
        self.value = value
        self._next = next

    def __repr__(self):
        return str(self.value)


class LinkList(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.is_empty():
            return ''
        current_node = self.head
        node_list = ''
        while current_node:
            if current_node._next:
                node_list += repr(current_node) + '-->'
            else:
                node_list += repr(current_node)
            current_node = current_node._next
        return node_list

    def __len__(self):
        return self.length

    def __getitem__(self, index):
        return self.get_item(index)

    def __setitem__(self, index, value):
        return self.update(index, value)

    def is_empty(self):
        return self.length == 0

    def append(self, item):
        if not isinstance(item, Node):
            item = Node(item)
        if self.is_empty():
            self.head = item
        else:
            current_node = self.head
            while current_node._next:
                current_node = current_node._next
            current_node._next = item
        self.length += 1

    def insert(self, index, item):
        if not isinstance(index, int):
            raise ValueError("Index must be int")
        if index < 0:
            raise IndexError("Index is out of range")
        if not isinstance(item, Node):
            item = Node(item)
        if index >= self.length:
            self.append(item)
            return 
        current_node = self.head
        if index == 0:
            self.head = item
            item._next = current_node
        else:
            while index-1:
                current_node = current_node._next
                index -= 1
            item._next, current_node._next = current_node._next, item
        self.length += 1

    def delete(self, index):
        if not isinstance(index, int):
            raise ValueError("Index must be int")
        if index > self.length-1 or index < 0:
            raise IndexError("Index is out of range")
        if index == 0:
            self.head = self.head._next
        else:
            current_node = self.head
            while index-1:
                current_node = current_node._next
                index -= 1
            current_node._next = current_node._next._next
        self.length -= 1

    def update(self, index, value):
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range")
        current_node = self.head
        while index:
            current_node = current_node._next
            index -= 1
        current_node.value = value

    def clear(self):
        self.head = None
        self.length = 0

    def get_item(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index is out of range")
        current_node = self.head
        while index:
            current_node = current_node._next
            index -= 1
        return current_node.value
        


if __name__ == "__main__":
    lst = LinkList()
    print lst
    lst.append(5)
    print lst
    lst.append(6)
    print lst
    lst.insert(7, 7)
    print lst
    lst.delete(1)
    print lst
    lst[1] = 99
    print len(lst)
    print lst
    print lst[1]
    lst.clear()
    print lst
        
        

