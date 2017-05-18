# 题目说明

这题是要删除一个列表最后第$n$个元素，这里使用快、慢两个指针做差异化处理，等快指针走到第$n$个元素时，慢指针再出发，等到快指针走到终点时，慢指针刚好走到要被删除元素的前一个位置，等式关系为$L-(L-n)$，其中$L$代表的是列表的总长度，注意当$n=L$时需要特别出力，因为`head`并没有`pre`点，直接返回`head.next`即可。实现代码如下：

```python
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = slow = head
        for i in range(n):
            fast = fast.next
        if not fast:
            return head.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return head
```

