# 题目说明#

这题是要遍历二叉树的节点，并返回其节点值，关键在于构造遍历的序组，实现代码如下：

```python
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
```

