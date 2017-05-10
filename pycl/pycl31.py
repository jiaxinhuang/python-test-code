#-*- coding:utf-8 -*-
'''
Created on 2017年5月10日

@author: huangjiaxin
'''
from PIL import Image
import numpy as np

def mapIdx(c, maxIter=128):
    z = 0
    for k in range(maxIter):
        z = z * z + c
        if np.abs(z) > 2:
            break
    return k

def solve():
    left = 0.34
    bottom = 0.57
    width = 0.036
    height = 0.027
    
    im = Image.open('mandelbrot.gif')
    imdata = np.array(list(im.getdata()))
    im_w, im_h = im.size
    dw = width / im_w
    dh = height / im_h
    xx = np.linspace(left, left + width - dw, im_w)
    yy = np.linspace(bottom, bottom + height - dh, im_h)
    yy = yy[::-1]
    xx.shape = (1, im_w)
    yy.shape = (im_h, 1)
    grids = xx + 1j * yy
    
    for i in range(im_h):
        for j in range(im_w):
            grids[i, j] = mapIdx(grids[i, j])
    
    im.putdata(grids.reshape((-1,)))
#     im.show()
    
    imdata.shape = (480, 640)
    diffs = imdata - grids
    msg = diffs[np.where(np.abs(diffs) == 16)]
    newIm = Image.new('1', [23, 73])
    newIm.putdata([i<0 for i in msg])
    newIm.save('level31_out.png')
    
if __name__ == "__main__":
    solve()