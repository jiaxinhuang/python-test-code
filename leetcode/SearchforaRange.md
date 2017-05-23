# 题目说明

这题是在一个给定数组中找到值为`target`的序号，如果不存在就返回$[-1,-1]$。解决的思路是使用二分法找到左右边界，实现代码如下：

```python
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]
        def search(left, right):
            if nums[left] == target and nums[right] == target:
                return [left, right]
            elif nums[left] <= target and nums[right] >= target:
                mid = (left + right) / 2
                l, r = search(left, mid), search(mid+1, right)
                if -1 in l+r:
                    return max(l, r)
                else:
                    return [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)
```

算法复杂度为$O(n)$

