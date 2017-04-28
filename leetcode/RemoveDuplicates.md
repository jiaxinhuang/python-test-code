# 题目解释#

这题的要求是统计给定数组中的不同元素个数，我一开始给的代码如下：

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        newlen = len(nums)
        if newlen <= 1:
            return newlen
        for i in range(len(nums) - 1):
            if nums[i+1] == nums[i]:
                newlen -= 1
        return newlen
    
if __name__ == '__main__':
    nums = [1, 1, 2]
    print Solution().removeDuplicates(nums)
```

但是提交的结果却是`Wrong Answer`，提示的内容如下：

```
Input: [1,1,2]
Output: [1,1]
Excepted: [1,2]
```

题目要求的返回结果是一个`int`类型的数据，这里不明白为什么这里的`Output`是数组。

从讨论中看到，这里的合理的设想是代码检查中是检查`nums[:n]`，从你的放回数值到数组中取值，回到题目中的`remove`字眼，所以还是需要对原数组进行操作的。

我这里使用了两个标志，来对原数组进行修改，一个作为对修改后的数组的排序（也是计数）， 一个则是原数组的序数，修改后的代码入下：

```python
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        i = 0
        j = len(nums)
        for num in range(1, j):
            if nums[num] != nums[num-1]:
                i += 1
                nums[i] = nums[num]
        return i + 1
    
if __name__ == '__main__':
    nums = [1, 1]
    print Solution().removeDuplicates(nums)
```