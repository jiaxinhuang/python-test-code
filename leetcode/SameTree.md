# 题目说明#

这题是判断两棵树是否一致，这里使用递归的想法，对多层的树就对其左右子树进行递归操作，关键是写好起始的判断，也就是分别只有一个节点的情况即可。实现代码如下：

```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if (p == None and q != None) or (p != None and q == None):
            return False
        elif p == None and q == None:
            return True
        else:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
```

