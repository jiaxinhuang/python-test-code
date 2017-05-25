# 题目说明

这题给定一个无重复元素的数组，求出其全排列。这里使用DFS的方法，进行递归遍历，实现代码如下：

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
```

另一种思路是直接使用数学直观上的每个位置遍历组合，实现代码如下：

```python
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        perms = [[]]
        for n in nums:
            new_perms = []
            for perm in perms:
                for i in xrange(len(perm)+1):
                    new_perms.append(perm[:i]+[n]+perm[i:])
            perms = new_perms
            print perms
        return perms
```

