#-*- coding:utf-8 -*-
'''
Created on 2017年4月13日

@author: huangjiaxin
'''
from PIL import Image
import numpy as np

im = Image.open('mozart.gif')
imdata = list(im.getdata())
imdata = np.array(imdata)
imdata = imdata.reshape((480, 640))
imdata2 = np.zeros(imdata.shape)
# print imdata[13][73]
for row in range(imdata.shape[0]):
    idx = np.where(imdata[row,:] == 195)
    idx = idx[0][0] - 1
    imdata2[row, :] = np.r_[imdata[row, idx:640], imdata[row, 0:idx]]

imdata2.shape = (480 * 640, )
im.putdata(imdata2)
im.show()
