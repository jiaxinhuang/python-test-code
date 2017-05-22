# 题目说明

这题是从一个给定的数组序列，得到一个新的比这个数组序列大的数的数组，用其连起来的代表的数值进行比较。具体的算法思路如下：

> 有如下数组
>
> 1 2 7 4 3 1
>
> 下一个排列为
>
> 1 3 1 2 4 7
>
> 先从末尾往前看，数字逐渐变大，到2时才减小，然后再从后往前找一个比2大的数字，是3，此时交换2和3，再把此时3后面的所有数字转置一下即可，详细步骤如下：
>
> 1　　2　　7　　4　　3　　1
>
> 1　　2　　7　　4　　3　　1
>
> 1　　3　　7　　4　　2　　1
>
> 1　　3　　1　　2　　4　　7

有几种特殊情况需要注意，一种是已经是最大，一种是在遍历到数组最后一个元素的情况，实现代码如下：

```python
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return
        L = len(nums)
        for i in range(L-1, 0, -1):
            if nums[i] > nums[i-1]:
                break
        if nums[i] > nums[i-1]:
            tempVal = nums[i-1]
            tempState = i-1
            for j in range(i, L):
                if nums[j] <= tempVal:
                    break
            print j
            if j == L-1 and nums[j] > tempVal:
                nums[tempState] = nums[j]
                nums[j] = tempVal
            else:
                nums[tempState] = nums[j-1]
                nums[j-1] = tempVal
            
            tempNums = nums[tempState+1:L]
            tempNums.sort()
            for i in range(len(tempNums)):
                nums[tempState+1+i] = tempNums[i]
        else:
            nums.sort()
        return
```

注意：我这里是直接使用原来的`nums`，所以不能返回具体对象，另外在改变数组时需要对位元素进行替换，不然都会出现以下错误`Do not return anything, modify nums in-place instead.`

