# 题目说明#

这题是求平方根，选择求平方根的算法是关键，这里选择牛顿迭代法求平方根。

牛顿迭代法如下：

> 设$A$为实数，且$A>0$，而且令$p_0 > 0$为$\sqrt A$的初始近似值。使用下列递归规则
>
> $p_k = \frac{p_{k-1} + \frac{A}{p_{k-1}}}{2}, \text{k=1,2, ...}$
>
> 定义序列$\{p_k\}_{k=0} ^\infty$，则序列$\{p_k\}_{k=0} ^\infty$收敛到$\sqrt A$，也可表示为$\lim _{n \rightarrow \infty} p_k = \sqrt A$。

具体实现代码如下：

```python
class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        p = x / 2
        eps = 0.0003
        while abs(p ** 2 - x) > eps:
            p = (p + (x * 1.0 / p)) / 2.0
        return int(p)
    
if __name__ == '__main__':
    x = 1
    print Solution().mySqrt(x)
```

这题比较奇葩，对精度没有要求，只要返回一个整数就好，所以最后需要加一步`int（p）`作为最终值。



