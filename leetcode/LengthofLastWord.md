# 题目说明#

这题主要是做好非字符字符的删除和分词就好了，这里直接使用Python的内置函数`strip`去除头部和尾部的空格等，再使用`split`进行分词成数组，然后再直接计算最后一个词的长度即可，实现代码如下：

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        sList = s.strip().split()
        if len(sList) <= 0:
            return 0
        L = len(sList[-1])
        return L
    
if __name__ == '__main__':
    s = "        "
    print Solution().lengthOfLastWord(s)
```

上面这么写还是不够优雅，而且实现效率会比较慢，因为中间环节有较多的处理内容，下面是一种优雅的处理方式：

```python
class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return 0 if len(s.split()) == 0 else len(s.split()[-1])
```

处理效率提升了$30\%$，虽然Python不能太讲究效率，这个提升也是很高的了。