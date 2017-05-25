#-*- coding:utf-8 -*-
'''
Created on 2017年5月25日

@author: huangjiaxin
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        L = len(matrix)
        for i in range(L):
            for j in range(L-i-1):
                print matrix[i][j],matrix[L-j-1][L-i-1]
                tmp = str(matrix[i][j])
                matrix[i][j] = matrix[L-j-1][L-i-1]
                matrix[L-j-1][L-i-1] = int(tmp)
        for i in range(L/2):
            for j in range(L):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[L-i-1][j]
                matrix[L-i-1][j] = tmp
        return

if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    Solution().rotate(matrix)
    print matrix