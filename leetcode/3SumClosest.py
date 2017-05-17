#-*- coding:utf-8 -*-
'''
Created on 2017年5月17日

@author: huangjiaxin
'''
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
        
if __name__ == '__main__':
    S = [1,1,1,1]
    target = 3
    print Solution().threeSumClosest(S, target)     