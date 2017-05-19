# 题目说明

直接使用减法求解，即用被除数逐个减去除数，统计次数，结果超时

```python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor:
            return -1
        res = 0
        sign = 0
        if dividend < 0:
            sign = 1
            dividend = abs(dividend)
        while (dividend - divisor) >= 0:
            res += 1
            dividend -= divisor
        if sign == 1:
            res = -res
        return res
```

因为不能使用其他的运算，网上的基本解法都是使用`移位运算`处理，`左移`一位相当于$x * 2 $，`右移`一位相当于$x/2$，所以可以更快地迭代，我这里使用的是近似于等式$x = a_{0}*2^{0}+a_{1}*2^{1} + a_{2}*2^{2}+ \cdots +a_{n}*2^{n}$，然后再把$2^n$累加起来即可，类似一种辗转相除法的变形。实现关键在于处理内外逻辑和变量的迭代上，实现代码如下：

```python
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if not divisor:
            return -1
        sign = ((dividend >= 0) == (divisor >= 0))
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp = 1
            tempdivisor = divisor
            while dividend >= tempdivisor:
                tempdivisor = (divisor << temp)
                if dividend >= tempdivisor:
                    temp += 1
            res += 2 ** (temp - 1)
            dividend -= (tempdivisor >> 1)
        if sign == False:
            res = -res
        return min(max(res, -2147483648), 2147483647)
```

