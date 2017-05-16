# 题目说明

这题是要得到一个按照一定顺序重新排序后的字符串，有两种做法，第一种是找出其中的变换数量关系，每一行的数量关系是固定的，首尾两行的变化关系间隔是$2*numRows-2$，中间行的标号间隔是有点复杂但是也是有规律的；第二种是仿造其逻辑，使用$numRows$个数组（或字符串）进行存储，最后再进行合并即可。我这里出于方便直接使用第二种方法，实现代码如下：

```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or len(s) <= numRows:
            return s
        else:
            sorts = [[] for x in range(numRows)]
            step = 1
            lang = 0
            for ch in s:
                sorts[lang].append(ch)
                if lang == 0:
                    step = 1
                elif lang == numRows - 1:
                    step = -1
                lang += step
        return ''.join(''.join(row) for row in sorts)
    
if __name__ == '__main__':
    print Solution().convert('PAYPALISHIRING', 3)
```

注意：尽量使用`Python`的内置函数，运行效率比较高