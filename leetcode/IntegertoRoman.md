# 题目说明

这题是将阿拉伯数字转换成罗马数字，且有范围限制（$\leq 3999$），构造一个常用集合进行逐步减即可，注意集合的顺序$\{1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1\}$，从大到小进行减，实现代码如下：

```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        rn = ''
        sr = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        sn = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4,1]
        i = 0
        while num > 0:
            rn += ((num // sn[i])*sr[i])
            num = num % sn[i]
            i += 1
        return rn 
```



