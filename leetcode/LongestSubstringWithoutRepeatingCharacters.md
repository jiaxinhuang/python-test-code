# 题目说明

给定一个字符串，返回其中不重复子串的长度。

这里的解法是使用一个字典在保存字符和位置信息，使用逐个加入的方式记录字符串中的字符最后的位置的信息，因为连续字符的长度信息保存为另外一个数，所以不会有相应的改变，不会保存相应的字符串内容。

```python
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLen = 0
        usedChar = {}
        
        for i in range(len(s)):
            if s[i] in usedChar and usedChar[s[i]] >= start:
                start = usedChar[s[i]] + 1
            else:
                maxLen = max(maxLen, i - start + 1)
            usedChar[s[i]] = i
        return maxLen
```

