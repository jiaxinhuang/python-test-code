# 题目说明

这题是给一个数独表，验证是否有效，注意这里并不是要判断这个表是否有解，而是判断给定的表的格式是否符合数独的规则，即行、列、小格是否有重复的元素。这里实现的方法就是按照这三种方式遍历，难点在于遍历小格子，利用函数关系数字$board[i][j]$位于第$i/3*3+j/3$个九宫格内，得到下面的循环格式：

```python
for block in range(9):
            temp = ['1','2','3','4','5','6','7','8','9']
            for i in range(block/3*3, block/3*3+3):
                for j in range(block%3*3, block%3*3+3):
                    if board[i][j] != '.':
                        if board[i][j] in temp:
                            temp.remove(board[i][j])
                        else:
                            return False
```

整体的实现代码如下：

```python
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
```

这里就是直接使用暴力地循环