# 题目说明#

这题求的是一个最大的子集之和，并不需要求出相应的子集，这里第一次采用的滑动窗口的思路，限定一个子集长度，不断地滑动和增加该值，代码如下：

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsum = nums[0]
        for le in range(1, len(nums) + 1):
            for i in range(len(nums)-le + 1):
                temp = sum(nums[i:i+le])
                if temp > maxsum:
                    maxsum = temp
        return maxsum
    
if __name__ == '__main__':
    nums = [-1]
    print Solution().maxSubArray(nums)
```

但是最后的结果是超时了，从时间效率来算是$$O(n^2)$$，需要修改相应细节。

修改思路为：从头加到尾，出现负值就舍弃（置为0），因为负值只会让更小，但是需要加上比较步骤，免得获取的值是更小。实现代码如下：

```python
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        maxsum = nums[0]
        Sum = 0
        for i in range(len(nums)):
            if Sum < 0:
                Sum = 0
            Sum += nums[i]
            maxsum = max(Sum, maxsum)
        return maxsum
    
if __name__ == '__main__':
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    print Solution().maxSubArray(nums)
```

