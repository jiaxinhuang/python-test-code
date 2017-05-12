#-*- coding:utf-8 -*-
'''
Created on 2017年5月12日

@author: huangjiaxin
'''
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        root = l3
        val = 0
        while l1 or l2 or val:
            tempval = 0
            if l1:
                tempval += l1.val
                l1 = l1.next
            if l2:
                tempval += l2.val
                l2 = l2.next
            val, nowval = divmod(tempval + val, 10)
            tempList = ListNode(nowval)
            l3.next = tempList
            l3 = l3.next
        return root.next