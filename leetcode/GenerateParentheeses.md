# 题目说明

给定数字$n$，返回一个含有全部可能的$n$组`()`的数组。这里采用的是`left`和`right`两个数来判断是否继续生成以及如何生成，使用递归持续生成发散，最后得到答案，这种方法的缺点是计算效率比较差。实现代码如下：

```python
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(s, left, right, res=[]):
            if left:
                generate(s+'(', left-1, right)
            if right > left:
                generate(s+')', left, right-1)
            if right == 0:
                res.append(s)
            return res
        return generate('', n, n) 
```

