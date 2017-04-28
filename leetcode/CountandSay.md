# 题目说明#

这题就是不断循环下去，我这里借用了两个中间数，一个保存计数，一个用来记录新的字符串，通过循环来迭代，通过与后一个字符进行比较来作为判断标准。要注意越界问题，其次就是起始位为`1`，实现代码如下：

```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        s = '1'
        if n == 1:
            return s
        for i in range(n-1):
            num = 1
            snew = ''
            for ch in range(len(s)):
                if ch+1 == len(s):
                    snew = snew + str(num) + s[ch]
                else:
                    if s[ch] != s[ch+1]:
                        snew = snew + str(num) + s[ch]
                        num = 1
                    else:
                        num += 1
            s = snew
        return s
    
if __name__ == '__main__':
    n = 2
    print Solution().countAndSay(n)
```

