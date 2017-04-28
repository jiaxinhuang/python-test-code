# 题目说明#

这题是求爬梯子的方案，因为每次只能爬1或者2阶，所以到达n阶，只有两种可能，第一种是从$n-1$来的，另外一种就是从$n-2$阶来的，这就转变成一个递归的问题了，有关系式如下：

$$f(n) = f(n-1) + f(n-2)$$

实现版本如下：

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n
        return self.climbStairs(n-1) + self.climbStairs(n-2)

if __name__ == '__main__':
    n = 35
    print Solution().climbStairs(n)
```

但是提交的结果是超时了，递归的效率很差，需要改进。可参照尾递归的实现思路进行改进，将递归改为循环迭代取值：

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 1
        for i in range(n):
            a, b = b, a+b
        return a

if __name__ == '__main__':
    n = 35
    print Solution().climbStairs(n)
```

还有另一种方案就是使用一个数组作为缓存内容，直接将每次计算结果存入，避免递归重复计算的步骤，实现代码如下：

```python
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        tem = [1,2]
        if n < 3:
            return tem[n-1]
        for i in range(2, n):
            tem.append(tem[i - 1] + tem[i - 2])
        return tem[-1]

if __name__ == '__main__':
    n = 35
    print Solution().climbStairs(n)
```

但是实现效率没有上一个版本好