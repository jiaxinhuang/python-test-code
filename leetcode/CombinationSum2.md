# 题目说明

这题与`CombinationSum`基本一致，这里的元素不能重复使用。实现代码如下：

```python
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        def helper(nums, target, index, tmp):
            if target < 0:
                return
            elif target == 0:
                oneComb = tmp
                if list(oneComb) not in res:
                    res.append(list(oneComb))
            else:
                for i in range(index, len(nums)):
                    tmp.append(nums[i])
                    helper(nums, target - nums[i], i+1, tmp)
                    tmp.pop()
        
        res = []
        tmp = []
        candidates.sort()
        helper(candidates, target, 0, tmp)
        return res
```

注意：这里需要注意去重和不要重复使用同一个值