# 题目说明

这题的要求是给定一个目标值，在给定的一个数组中找出三个数的和与这个目标值最接近。这题与前面的一个求最大面积的题目类似，将数组排序，然后进行夹逼求和，使用两个指针，根据判断条件移动指针。实现代码如下：

```python
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        tmin = abs(sum(nums[:3]) - target)
        sumc = sum(nums[:3])
        if len(nums) == 3:
            return sumc
        else:
            if tmin == 0:
                return sumc
            for i in range(len(nums) - 2):
                j = i + 1
                k = len(nums) - 1
                while j < k:
                    tempsum = nums[i] + nums[j] + nums[k]
                    temp = tempsum - target
                    if temp == 0:
                        return tempsum
                    if temp < 0:
                        if abs(temp) >= tmin:
                            j += 1
                        else:
                            tmin = abs(temp)
                            sumc = tempsum
                            j += 1
                    else:
                        if abs(temp) >= tmin:
                            k -= 1
                        else:
                            tmin = abs(temp)
                            sumc = tempsum
                            k -= 1
            return sumc
```

注意：这里的逻辑有点杂乱，有能力需要再进行整理