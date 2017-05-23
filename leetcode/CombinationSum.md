# 题目说明

这题是从一个给定数组中得到和为给定`target`的序列组，这里的元素可以重复使用，使用的深度优先搜索的方法，结合判断条件进行回溯。实现代码如下：

```python
class Solution(object):
    def combinationSum(self, candidates, target):
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
                res.append(list(oneComb))
            else:
                for i in range(index, len(nums)):
                    tmp.append(nums[i])
                    helper(nums, target - nums[i], i, tmp)
                    tmp.pop()
        
        res = []
        tmp = []
        candidates.sort()
        helper(candidates, target, 0, tmp)
        return res
```

注意：这里需要注意Python的浅复制，所以有了下面这句

```python
oneComb = tmp
res.append(list(oneComb))
```

