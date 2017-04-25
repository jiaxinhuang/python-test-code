#-*- coding:utf-8 -*-
'''
Created on 2017年4月25日

@author: huangjiaxin
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ortr = []
        if not root:
            return ortr
        else:
            node = [root]
            while node:
                ortr.insert(0, [n.val for n in node])
                node = [s for n in node for s in (n.left, n.right) if s]
            return ortr
        