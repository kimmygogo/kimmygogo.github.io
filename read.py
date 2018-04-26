#! /usr/bin/env python
x = 0 
fh = open('/home/my-site/index.html','r')
while 1:
    line2 = fh.readline()
    if (len(line2) == 0):
        break
    print(line2)
    x += 1
fh.close()
