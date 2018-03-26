# !/usr/bin/python3
# -*- coding:utf-8 -*-

class Node:
    """二叉树结点"""
    def __init__(self, value=None):
        self.data = value
        self.lchild = None   # 左子结点
        self.rchild = None   # 右子结点


class BiThrNode:
    """线索二叉树结点"""
    def __init__(self, value=None):
        self.data = value
        self.lchild = None   # 左子结点
        self.rchild = None   # 右子结点
        self.ltag = False    # 左标志位
        self.rtag = False    # 右标志位


class Tree:
    """
    二叉树
    """
    def __init__(self, tree_chain):
        self.root = self.create_tree(tree_chain)

    def create_tree(self, tree_chain):
        """前序创建tree"""
        l = 0
        r = len(tree_chain) - 1
        if l > r:
            return None
        if l == r:
            return Node(tree_chain[l])
        mid = (l+r)//2
        root = Node(tree_chain[mid])
        root.lchild = self.create_tree(tree_chain[:mid])
        root.rchild = self.create_tree(tree_chain[mid+1:])
        return root

    def preorder(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.data, end="")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return 
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.data, end="")

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        print(node.data, end="")
        self.postorder(node.rchild)
