# -*- coding: utf-8 -*-
import zipfile
# import re

z_file = zipfile.ZipFile('channel.zip')

# findnum = re.compile(r'\d+$').findall

z_comment = []

name = '90052.txt'
while True:
    zinfo = z_file.getinfo(name)
    z_text = z_file.open(name)
    data=z_text.read().split()[-1]
#     data = findnum(z_text.read())
    z_text.close()
    z_comment.append(zinfo.comment)
    if len(data)<6:
        name = '%s.txt' % data
        print name,data,zinfo.comment
    else:
        break
    
print ''.join(z_comment)