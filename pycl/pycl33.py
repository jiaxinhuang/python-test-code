#-*- coding:utf-8 -*-
'''
Created on 2017年5月10日

@author: huangjiaxin
'''
from PIL import Image
import numpy as np
from scipy.stats import itemfreq
from pprint import pprint

def main():
    im = Image.open('beer2.png')
    im_data = np.array(list(im.getdata()))
    im_data_stat = itemfreq(im_data)
    pprint(im_data_stat)
    pprint([np.sqrt(i) for i in np.cumsum(im_data_stat[:, 1])])
    
    for i in range(im_data_stat.shape[0] - 2, 0, -2):
        newIm_data = im_data[np.where(im_data < im_data_stat[i, 0])]
        idx_0 = np.where(newIm_data == newIm_data.max())
        idx_1 = np.where(newIm_data != newIm_data.max())
        newIm_data[idx_0] = 0
        newIm_data[idx_1] = 1
        size = int(np.sqrt(len(newIm_data)))
        newIm = Image.new('1', (size, size))
        newIm.putdata(newIm_data)
        newIm.save('level33_%i.png' % i)
        
if __name__ == "__main__":
    main()