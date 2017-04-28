# 题目说明#

这题可以化成是`SameTree`中问题，将比较的左右更换一下即可，这题遇到的问题是处理递归的一个逻辑，需要自己再定义一个函数，使用该函数进行递归。实现代码如下：

```python
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
```

