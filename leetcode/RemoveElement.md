# 题目说明#

这题的要求与`RemoveDuplicates`类似，都是在不新增内存的情况下删除给定的元素，返回一个数值，进而得到新的数组，需要对原数组的序列进行重新排序，代码如下：

```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0
        newlen = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[newlen] = nums[i]
                newlen += 1
        return newlen
    
if __name__ == '__main__':
    nums = [4,4,0,1,0,2]
    val = 0
    print Solution().removeElement(nums, val)
```

这里需要注意几个问题：

- 使用一个数值作为新数组的标记，也作为长度计数
- 注意特殊值，在python中0与none是等同的