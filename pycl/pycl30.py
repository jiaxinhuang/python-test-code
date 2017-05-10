#-*- coding:utf-8 -*-
'''
Created on 2017年5月9日

@author: huangjiaxin
'''
import csv
from PIL import Image
import numpy as np

def test1():
    data = np.genfromtxt('yankeedoodle.csv', delimiter=',')
    data = data[:, :-1]
    data = data.reshape((-1,))
    data = data[:-1]
    data = data.reshape((139, 53)).transpose().reshape((-1,))
    
    im = Image.new('L', (139, 53))
    im.putdata(data*255)
    im.show()
    
    data = data.reshape((53, 139)).transpose().reshape((-1,))
    data_str = ["%.5f" % i for i in data]
    msg = []
    for i in range(0, 7365, 3):
        msg.append(chr(int(data_str[i][5] + data_str[i+1][5] + data_str[i+2][6])))
    print ''.join(msg)


def test2():
    tempList = []
    tempSList = []
    with open('yankeedoodle.csv', 'rb') as f:
        file = csv.reader(f)
        for row in file:
            if row[-1] == '':
                tempList += [float(x) for x in row[:-1]]
                tempSList += row[:-1]
            else:
                tempList += [float(x) for x in row[:]]
                tempSList += row[:]
    tempArray = np.array(tempList).reshape(139, 53)
    im = Image.new('L', (53, 139))
    im.putdata(tempArray)
    im.show()
    
    print len(tempSList)
    msg = []
    for i in range(0, 7365, 3):
        msg.append(chr(int(tempSList[i][-2] + tempSList[i+1][-2] + tempSList[i+2][-1])))
    print ''.join(msg)
    

if __name__ == '__main__':
    test2()