#-*- coding:utf-8 -*-
'''
Created on 2017年4月13日

@author: huangjiaxin
'''
from PIL import Image
import numpy as np
import gzip
import codecs
import difflib
import re

def test1():
    im = Image.open('balloons.jpg')
    imdata = list(im.getdata())
    imdata = np.array(imdata)[:, 2]
    print len(imdata)
    imdata = imdata.reshape((335, 750))
    imdata1 = imdata[:, 0:375]
    imdata2 = imdata[:, 375:]
    difValue = imdata1 - imdata2
    difValue = np.reshape(difValue, (335, 375))
    dif = Image.fromarray(difValue)
    dif.show()

def test2():
    f = gzip.open('deltas.gz', 'rb')
    contents = f.read()
    f.close()
    
    lines = contents.strip().split('\n')
    str1 = []
    str2 = []
    for line in lines:
        str1.append(line[0:53])
        str2.append(line[56:109])
    str_diff = list(difflib.Differ().compare(str1, str2))
    png_datas = [''.join(filter(lambda l: l[0] == c, str_diff)) for c in' -+']
    print len(png_datas)
    for i in range(len(png_datas)):
        png_data = re.sub(r'[^0-9a-fA-F]', '', png_datas[i])
        png_data = codecs.getdecoder('hex')(png_data)[0]
        with open(('png%d' % i), 'wb') as handle:
            handle.write(png_data)


if __name__ == '__main__':
    test2()