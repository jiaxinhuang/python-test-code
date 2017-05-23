#-*- coding:utf-8 -*-
'''
Created on 2017年5月23日

@author: huangjiaxin
'''
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if not board or len(board) != 9 or len(board[0]) != 9:
            return False
        for i in range(9):
            temp = ['1','2','3','4','5','6','7','8','9']
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in temp:
                        temp.remove(board[i][j])
                    else:
                        return False
        
        for j in range(9):
            temp = ['1','2','3','4','5','6','7','8','9']
            for i in range(9):
                if board[i][j] != '.':
                    if board[i][j] in temp:
                        temp.remove(board[i][j])
                    else:
                        return False
        
        for block in range(9):
            temp = ['1','2','3','4','5','6','7','8','9']
            for i in range(block/3*3, block/3*3+3):
                for j in range(block%3*3, block%3*3+3):
                    if board[i][j] != '.':
                        if board[i][j] in temp:
                            temp.remove(board[i][j])
                        else:
                            return False
        
        return True
    
if __name__ == '__main__':
    board = [".87654321",
             "2........",
             "3........",
             "4........",
             "5........",
             "6........",
             "7........",
             "8........",
             "9........"]
    print Solution().isValidSudoku(board)
                