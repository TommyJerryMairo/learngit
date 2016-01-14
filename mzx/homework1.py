#/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random
import string

def main():
    mengzhaoxin=[]
    for i in string.ascii_letters:
        mengzhaoxin.append(i)
    for i in range(10):
        mengzhaoxin.append(str(i))
    for i in range(200):
        mzx_gf=[]
        for j in range(20):
            mzx_gf.append(random.choice(mengzhaoxin))
        print "".join(mzx_gf)

if __name__=='__main__':
    main()

