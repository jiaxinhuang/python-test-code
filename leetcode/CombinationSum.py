#-*- coding:utf-8 -*-
'''
Created on 2017年5月23日

@author: huangjiaxin
'''
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
    
        
        
if __name__ == '__main__':
    S = [2,3,6,7]
    print Solution().combinationSum(S, 7)