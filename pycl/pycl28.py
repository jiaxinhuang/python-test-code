#-*- coding:utf-8 -*-
'''
Created on 2017年5月9日

@author: huangjiaxin
'''
from PIL import Image
import numpy as np

def main():
    im = Image.open('bell.png')
    imdata = list(im.getdata())
    imdata = np.array(imdata)
    size = im.size
    imdata = imdata.reshape((size[1], size[0], -1))
    imdata_g = imdata[:, :, 1]
    diff = np.abs(imdata_g[:, 0::2] - imdata_g[:, 1::2])
    idx = np.where(diff != 42)
    msg = diff[idx]
    print ''.join(chr(i) for i in msg)
    print 'Guido van Rossum'.split()[0]
    
if __name__ == '__main__':
    main()