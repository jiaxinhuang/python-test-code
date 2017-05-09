#-*- coding:utf-8 -*-
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
from PIL import Image
import numpy as np

def BFS(imdata, startPos, endPos):
    visited = np.zeros(imdata.shape[0:2], dtype=np.False_)
    visited[0, 639] = True
    visited[640, 1] = True
    father = -np.ones(imdata.shape[0:2], dtype=np.int8)
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    bfs_queue = []
    bfs_queue.append(startPos)
    while bfs_queue:
        cur_pos = bfs_queue.pop(0)
        if cur_pos == endPos:
            break
        for i in range(4):
            x = cur_pos[0] + dx[i]
            y = cur_pos[1] + dy[i]
            if imdata[x, y, 1] == imdata[x, y, 2] == 0 and not visited[x, y]:
                father[x, y] = i
                bfs_queue.append([x, y])
        visited[cur_pos[0], cur_pos[1]] = True
    return father


def mapXY(pre, pos):
    if pre == 0:
        pos[0] += 1
    elif pre == 1:
        pos[1] -= 1
    elif pre == 2:
        pos[0] -= 1
    elif pre == 3:
        pos[1] += 1
    else:
        raise Exception("Invalid Father Pos!")
    return pos

def getdata(imdata, father, startPos, endPos):
    data = []
    curPos = endPos[:]
    while curPos != startPos:
        data.append(chr(imdata[curPos[0], curPos[1], 0]))
        imdata[curPos[0], curPos[1]] = [0, 255, 0, 255]
        curPos = mapXY(father[curPos[0], curPos[1]], curPos)
    data.append(chr(imdata[startPos[0], startPos[1], 0]))
    return data, imdata

def solve():
    im = Image.open('maze.png')
    w, h = im.size
    imdata = list(im.getdata())
    imdata = np.array(imdata)
    imdata = imdata.reshape((h, w, -1))
    print "BFS"
    fatherMat = BFS(imdata, [1, 639], [639, 1])
    print "Get Path and data"
    data, nimdata = getdata(imdata, fatherMat, [1, 639], [639, 1])
    open('maze.rar', 'w').write(''.join(data[::-2]))
    nimdata = nimdata.reshape((-1, 4)).tolist()
    nimdata = [tuple(x) for x in nimdata]
    im.putdata(nimdata)
    im.save('mazeSolve.jpg')
    
if __name__ == '__main__':
    solve()