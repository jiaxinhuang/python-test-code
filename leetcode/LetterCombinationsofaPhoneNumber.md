# 题目说明

给定数字字符串，给出所有可能的字母字符串数组。这里是一个遍历所有可能的解决方案，使用的广度优先搜索即`BFS`，实现代码如下：

```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nts = {'2':['a', 'b', 'c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z'],
               '0':[' ']}
        
        if len(digits) == 0:
            return []
        res = ['']
        for i in digits:
            temp = []
            for ch in nts[i]:
                for pr in res:
                    temp.append(pr+ch)
            res = temp
        return res
```

