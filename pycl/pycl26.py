#-*- coding:utf-8 -*-
'''
Created on 2017年4月19日

@author: huangjiaxin
'''
import urllib
import StringIO
import wave
from PIL import Image

def main():
    url = 'http://butter:fly@www.pythonchallenge.com/pc/hex/lake%i.wav'
    Im = Image.new('RGB', (300, 300))

    for i in range(25):
        print '%i%i' % (i + 1, 25)
        data = wave.open(StringIO.StringIO(urllib.urlopen(url % (i+1)).read()))
        patch = Image.frombytes('RGB', (60, 60), data.readframes(data.getnframes()))
        pos = (60 * (i % 5), 60 * (i // 5))
        Im.paste(patch, pos)

    Im.save('wav.jpg')
    Im.show()
    

if __name__ == '__main__':
    main()