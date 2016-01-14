#/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random
import string

def main():
    mengzhaoxin=list(string.ascii_letters)
    mengzhaoxin.extend(list(map(lambda x: str(x),range(10))))
    for i in range(200):
        random.shuffle(mengzhaoxin)
	print ''.join(mengzhaoxin[:20])

if __name__=='__main__':
    main()

