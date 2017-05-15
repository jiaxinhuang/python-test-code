# 题目说明

这题是找出题目中最长的回文字符串，一开始想的方法是使用移动窗口，判断窗口内的字符串是否是回文，这个方案计算效率太差，后来看到一种改进的方法，以找中心，遍历n次即可，分为两种情况进行获取并比较，`aba`和`abba`这两种情况，实现代码如下：

```python
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        for i in range(len(s)):
            res = max(self.withmiddle(s, i, i), self.withmiddle(s, i, i+1), res, key=len)
        return res
        
    def withmiddle(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
if __name__ == '__main__':
    s = 'abbaddddd'
    print Solution().longestPalindrome(s)
```

