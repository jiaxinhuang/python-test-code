# 题目说明#

这题是给定`target`的值，寻找在数组中适合的插入位置，我这里就是使用这么个方法，更多是通过条件语句判断，但是效率似乎怎么修改也得不到好的提升，代码如下：

```python
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums and target:
            return 0
        if nums[0] > target:
            return 0
        if nums[-1] < target:
            return len(nums)
        for i in range(len(nums)):
            if nums[i] >= target:
                return i


if __name__ == '__main__':
    nums = [1,3,5,6]
    target = 3
    print Solution().searchInsert(nums, target)
```

