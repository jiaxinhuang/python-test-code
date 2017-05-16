#-*- coding:utf-8 -*-
'''
Created on 2017年5月16日

@author: huangjiaxin
'''
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        maxArea = 0
        while i < j:
            area = min(height[i], height[j]) * (j - i)
            if area > maxArea:
                maxArea = area
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return maxArea