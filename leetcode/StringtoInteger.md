# 题目说明

这题的要求是把字符串转变为数字，需要注意的是将不符合的情况去除，但是这里有个问题是它的测试用例把前部分符合的也要识别并输出。这里有两种方案，第一种是用正则匹配的形式，匹配一个字符串前面部分是否符合`(^[\+\-0]*\d+)\D*`这种格式；第二种是逐一字符识别，并添加限定条件进行判断。这里使用的是第二种方案，实现代码如下：

```pytho
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if len(str) == 0:
            return 0
        tmp ='0'
        result = 0
        i = 0
        if str[0] in '+-':
            tmp = str[0]
            i = 1
        MAX = 2147483647
        MIN = -2147483648
        for i in range(i, len(str)):
            if str[i].isdigit():
                tmp += str[i]
            else:
                break
        if len(tmp) > 1:
            temp = int(tmp)
            if temp > MAX:
                result = MAX
            elif temp < MIN:
                result = MIN
            else:
                result = temp
        return result
    
if __name__ == '__main__':
    print Solution().myAtoi('-0012a42')
```

注意：这里需要注意`int`的最大最小值