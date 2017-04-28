# 题目说明#

这题的关键是做好进制变换，由于使用的Python，直接使用其`int`和`bin`这两个内置函数进行使用，详细用法另外Google搜索，实现代码如下：

```python
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        at = int(a, 2)
        bt = int(b, 2)
        sb = bin(at + bt)
        return sb[2:]
    
if __name__ == '__main__':
    a = '11'
    b = '1'
    print Solution().addBinary(a, b)
```

