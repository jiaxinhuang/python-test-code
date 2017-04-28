# 题目说明#

这题是合并两个有序数组为一个新的有序数组，给的输入`nums1`的长度实际为$n+m$，将`nums1`从尾到头重新插入值的方式进行重新构建即可，实现代码如下：

```python
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:n]
        else:
            while m > 0 and n > 0:
                if nums1[m-1] >= nums2[n-1]:
                    nums1[m + n -1] = nums1[m-1]
                    m -= 1
                else:
                    nums1[m + n -1] = nums2[n - 1]
                    n -= 1 
        if n > 0:
            nums1[:n] = nums2[:n]

if __name__ == '__main__':
    a = [2,0]
    b = [1]
    Solution().merge(a, 1, b, 1)
    print a
```

