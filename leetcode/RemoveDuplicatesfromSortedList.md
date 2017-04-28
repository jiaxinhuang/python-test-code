# 题目说明#

这题是删除对象数组中重复的元素，使用链表的特性，直接将当前元素的`next`改为`next.next`即可。实现代码如下：

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        while temp and temp.next:
            if temp.val == temp.next.val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head
```

