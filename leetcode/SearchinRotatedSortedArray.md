# 题目说明

在一个存有循环排序的数组中找某个数的序号，直接使用暴力法遍历，结果却可以通过，估计是设计有误，暴力法实现代码如下：

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        return -1
```

如果是这样实现就没多大意思，下面用其他方法解决。

用一种改进的二分搜索法，取中间值，比较大小，判断左、右有序，进行循环查找，实现代码如下：

```python
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) / 2
            if target == nums[mid]:
                return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target and nums[mid] >= target:
                    high = mid -1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
```

