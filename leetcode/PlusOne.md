# 题目说明#

这题的要求的是将一个数字数组看做是一个正数，将这个正数加1，然后再以同样的形式返回一个数组，中间的过程为将数组转换为整数，整数+1，再把整数变为数组，可以使用Python的内置函数进行简单转换。实现代码如下：

```python
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = 0
        L = len(digits)
        for i in range(L):
            num = num + digits[i] * pow(10, L - i - 1)
        return [int(i) for i in str(num+1)]
    

if __name__ == '__main__':
    digits = [1, 2, 3, 4]
    print Solution().plusOne(digits)
```

