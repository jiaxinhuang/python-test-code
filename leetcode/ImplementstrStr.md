# 题目说明#

这题使用`Python`的时候不要想着使用其语法糖就好，将之看成数组，用其“片段”化处理比较就好，多次提交是在不同特殊情况下的输出应该是`0`还是`-1`，多试几次就好了，代码如下：

```python
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        hlen, nlen = len(haystack), len(needle)
        if nlen == 0:
            return 0
        if hlen == 0 or hlen < nlen:
            return -1
        for i in range(hlen - nlen + 1):
            if haystack[i:i+nlen] == needle:
                return i
        return -1


if __name__ == '__main__':
    haystack = ''
    needle = ''
    print Solution().strStr(haystack, needle)
```

