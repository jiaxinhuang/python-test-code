# 题目说明

这题可以理解为是求一个矩阵顺时针旋转$90^\circ$，这里的难点在于找到交换元素的顺序，这里采用的一种二段翻转方法，先沿着两条对角线中的一条交换元素，再沿着一条中线翻转即可。实现代码如下：

```python
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
```

注意：这里有一个更直接和直观的方法，就是直接重新构造一个矩阵，提取每一列的数据构造一个新的行，但是这里需要不使用其他内存和其他放回地址，所以只能使用交换原矩阵对应位置元素的值。