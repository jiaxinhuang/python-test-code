# 题目说明

这题是找出围成的最大面积，给定一个数组，以数组中两个数值中较小一个为宽，以两个数值标号之间的差为长，计算面积。首先想到的是穷举法，遍历一遍，将全部的面积值算一遍，再比较，结果超时了，使用其他语言或许不会超时，超时情况实例：

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        hL = len(height)
        for i in range(0, hL-1):
            if height[i] == 0:
                continue
            area = 0
            for j in range(i+1, hL):
                area = min(height[i], height[j]) * (j - i)
                if area > maxArea:
                    maxArea = area
        return maxArea
```

使用另一种遍历方式，保持两个指针`i`和`j`；分别指向长度数组的首尾。如果$a[i]$小于$a[j]$，则移动`i`向后（$i++$）。反之，移动`j`向前（$j--$）。如果当前的area大于了所记录的area，替换之。这个想法的基础是，如果`i`的长度小于`j`，无论如何移动`j`，短板在`i`，不可能找到比当前记录的area更大的值了，只能通过移动`i`来找到新的可能的更大面积。实现代码如下：

```python
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > maxArea:
                maxArea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea
```

这种方式虽然不超时，但是效率也一般，可以在这上面再进行改进，加入分治的思想，在比较`a[i]`和`a[j]`值的时候进行分治，可大幅度提高效率，实现代码如下：

```python
while left < right:
    l, r = height[left], height[right]
    if l < r:
        area = (right - left) * l
        while height[left] <= l:
            left += 1
    else:
        area = (right - left) * r
        while height[right] <= r and right:
            right -= 1
    if area > max_area:
        max_area = area
```

