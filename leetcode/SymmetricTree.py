#-*- coding:utf-8 -*-
'''
Created on 2017年4月24日

@author: huangjiaxin
'''
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def judge(Left, Right):
            if not Left and not Right:
                return True
            elif Left and Right and Left.val == Right.val:
                return judge(Left.left, Right.right) and judge(Left.right, Right.left)
            else:
                return False
        return judge(root.left, root.right)
                