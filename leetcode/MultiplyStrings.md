# 题目说明

这题说白了就是大整数的乘法，这里需要对乘法运算进行一个解析，有$AB * CD = AC(AD+BC)BD$的格式，这里记得相应的进位处理，实现代码如下：

```python
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        L1 = len(num1)
        L2 = len(num2)
        temp = [0 for i in range(L1+L2-1)]
        for i in range(L1):
            for j in range(L2):
                temp[i+j] += int(num1[i])*int(num2[j])
        res = ''
        d = 0
        for k in range(len(temp)-1, 0, -1):
            num = temp[k] + d
            res = str(num % 10) + res
            d = num / 10
        return str(temp[0]+d)+res
```

注意：这里的中间临时数组大小为$L1+L2-1$，原因是起始的$0+0$取值为0