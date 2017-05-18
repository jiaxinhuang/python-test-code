# 题目说明

这题是找出和为给定`target`的四数字组，并且是不重复的组合，这里复用前面`3Sum`的代码，添加一个`target`的值限定范围，实现代码如下：

```python
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        if len(nums) < 4:
            return res
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            tempT = target - nums[i]
            tempL = self.threeSum(nums[i+1:], tempT)
            if tempL:
                for tl in tempL:
                    tl.insert(0, nums[i])
                    res.append(tl)
        return res
    
    def threeSum(self, nums, target):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        else:
            res = set()
            for i in range(len(nums) - 2):
                if i >= 1 and nums[i] == nums[i - 1]:
                    continue
                d = {}
                for x in nums[i+1:]:
                    if x not in d:
                        d[target-nums[i] - x] = 1
                    else:
                        res.add((nums[i], target-nums[i]-x, x))
        return map(list, res)
```

