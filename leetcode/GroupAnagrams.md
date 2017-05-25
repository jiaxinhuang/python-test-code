# 题目说明

这题是从给定的一个字符串数组中根据字符串含有的字符进行聚合，这题的关键在于将字符串有序化，具体步骤是将之从字符串变为列表，然后排序再变成字符串的过程，这里使用了`lambda`函数进行转化，直接变换的方式在排序一步总会出错。实现代码如下：

```python
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        res = []
        for i, str in enumerate(strs):
            str = ''.join((lambda x:(x.sort(), x)[1])(list(str)))
            if str not in m:
                m[str] = [i]
            else:
                m[str].append(i)
        
        for key in m:
            temp = []
            for i in m[key]:
                temp.append(strs[i])
            res.append(temp)
        return res 
```

