#-*- coding:utf-8 -*-
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
from PIL import Image
import string
import bz2
import keyword


def main():
    im = Image.open('zigzag.gif')
    imdata = im.tobytes()
    p = im.palette.getdata()[1][::3]
    frm = ''.join([chr(i) for i in range(256)])
    table = string.maketrans(frm, p)
    imdata_trans = imdata.translate(table)
#     print imdata[:20]
#     print imdata_trans[:20]
    newIm = Image.new('1', im.size)
    newIm.putdata([i[0] == i[1] for i in zip(imdata[1:], imdata_trans[:-1])])
    newIm.save('out27.png')
    diff = filter(lambda p: p[0] != p[1], zip(imdata[1:], imdata_trans[:-1]))
    diff = [''.join(p[i] for p in diff) for i in range(2)]
    text = bz2.decompress(diff[0])
    print len(text)
    words = text.split(' ')
    for w in set(words):
        if not keyword.iskeyword(w):
            print w
    

if __name__ == '__main__':
    main()