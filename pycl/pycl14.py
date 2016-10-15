# -*- coding: utf-8 -*-
'''
Created on 2016年10月13日

@author: huangjiaxin
'''
import Image

l = [[i, i-1, i-1, i-2] for i in xrange(100, 1, -2)]
print l 
# l = reduce(lambda x, y: x+y, l)

im = Image.open("wire.png")
org = im.load()
print org[0,0]
im_new = Image.new(im.mode, (100, 100))
org_new = im_new.load()
print im.size

start_loca = (0,0)
now_loca = start_loca
org_loca = 0
for l_ele in l:
    for i in xrange(l_ele[0]): #(x+1,y)
        print now_loca
        org_new[now_loca] = org[(org_loca,0)]
        org_loca +=1
        now_loca = (now_loca[0]+1,now_loca[1])
    now_loca = (now_loca[0]-1,now_loca[1]+1)
    
    for j in xrange(l_ele[1]):#(x,y+1)       
        print now_loca
        org_new[now_loca] = org[(org_loca,0)]
        org_loca +=1
        now_loca = (now_loca[0],now_loca[1]+1)
    now_loca = (now_loca[0]-1,now_loca[1]-1)
    
    for k in xrange(l_ele[2]):#(x-1,y)   
        print now_loca     
        org_new[now_loca] = org[(org_loca,0)]
        org_loca +=1
        now_loca = (now_loca[0]-1,now_loca[1])
    now_loca = (now_loca[0]+1,now_loca[1]-1)
    
    for l in xrange(l_ele[3]):#(x,y-1) 
        print now_loca      
        org_new[now_loca] = org[(org_loca,0)]
        org_loca +=1
        now_loca = (now_loca[0],now_loca[1]-1)
    now_loca = (now_loca[0]+1,now_loca[1]+1)
        
im_new.save('wire_second_new.png')