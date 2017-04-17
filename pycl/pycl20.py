#-*- coding:utf-8 -*-
'''
Created on 2017年4月14日

@author: huangjiaxin
'''
import base64
import wave

def test1():
    with open('hexbin.txt', 'r') as f:
        msg = f.read()
    open('indian.wav', 'wb').write(base64.decodestring(msg))


def test2():
    india = wave.open('indian.wav', 'r')
    india_frames = india.readframes(india.getnframes())
    india_swap = wave.open('indian_swap.wav', 'w')
    india_swap.setnchannels(1)
    india_swap.setframerate(india.getframerate())
    india_swap.setsampwidth(india.getsampwidth())
    
    india_swap_frames = []
    for i in range(0, len(india_frames), 2):
        india_swap_frames.append(india_frames[i+1])
        india_swap_frames.append(india_frames[i])
        
    india_swap_frames = ''.join(india_swap_frames)
    india_swap.writeframes(india_swap_frames)
    india_swap.close()
    india.close()
    
    
if __name__ == '__main__':
    test2()