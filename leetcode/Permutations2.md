# 题目说明

这题的情况基本与前一题一样，这里存在重复元素的情况，所以只需要在执行前一版代码是添加一个条件判断即可，实现代码如下：

```python
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(nums, [], res)
        return res
        
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            else:
                self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
```

