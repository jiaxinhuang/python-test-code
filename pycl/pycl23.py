#-*- coding:utf-8 -*-
'''
Created on 2017年4月17日

@author: huangjiaxin
'''
import numpy as np
from PIL import Image, ImageSequence

def  draw(im, origin, offsetCoords, value):
    for c in offsetCoords:
        im.putpixel(origin, value)
        dx = (c[0] - 100) // 2
        dy = (c[1] - 100) // 2
        origin[0] += dx
        origin[1] += dy


def main():  
    im = Image.open('white.gif')
    coords = []
    for i in ImageSequence.Iterator(im):
        idata = list(i.getdata())
        idx = idata.index(8)
        x = idx % 200
        y = idx // 200
        coords.append((x, y))
    
    coords = np.array(coords)
    interval = np.where(np.all(coords == [100, 100], axis=1) == True)
    interval = interval[0].tolist()
    interval.append(coords.shape[0])

    imOut = Image.new(im.mode, im.size)
    x, y = 30, 50
    for i in range(len(interval) - 1):
        draw(imOut, [x, y], coords[interval[i] + 1:interval[i+1]], 200)
        x += 30
    imOut.show()
    
if __name__ == '__main__':
    main()