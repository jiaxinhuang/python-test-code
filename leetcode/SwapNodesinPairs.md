# 题目说明

这里是纯链表的操作，注意取一个中间量以及起始的表头来保存对应的点即可，实现代码如下：

```python
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        pre = ListNode(0)
        h2 = head.next
        while head and head.next:
            t1 = head.next
            t2 = head.next.next
            head.next = t2
            pre.next = t1
            t1.next = head
            head = t2
            pre = t1.next
        return h2
```

