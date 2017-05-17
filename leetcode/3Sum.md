# 题目说明

这题是找出所有三个元素的和为0的数组，不能重复。找出和为0的三元素组和去重是两个重要环节。但是在实现过程中比较容易出现超时情况。超时情况：

```python
def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        resL = []
        if len(nums) < 3:
            return resL
        else:
            nums.sort()
            
            for i in range(len(nums) - 2):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    if j > i+1 and nums[j] == nums[j-1]:
                        j += 1
                        continue
                    if k < len(nums) - 1 and nums[k] == nums[k+1]:
                        k -= 1
                        continue
                    
                    temp = nums[i] + nums[j] + nums[k]
                    if temp == 0:
                        resL.append([nums[i], nums[j], nums[k]])
                    if temp > 0:
                        k -= 1
                    else:
                        j += 1
        return resL
```

需要在将数组排好序的情况下添加更多判断条件，使用python的数据结构进行解决，实现代码如下：

```python
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        else:
            nums.sort()
            res = set()
            for i in range(len(nums) - 2):
                if i >= 1 and nums[i] == nums[i - 1]:
                    continue
                d = {}
                for x in nums[i+1:]:
                    if x not in d:
                        d[-nums[i] - x] = 1
                    else:
                        res.add((nums[i], -nums[i]-x, x))
        return map(list, res)
            
                
if __name__ == '__main__':
    S = [-1, 0, 1, 2, -1, -4]
    print Solution().threeSum(S)
```

