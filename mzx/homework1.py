#/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random
import string

def main():
    mengzhaoxin=list(string.ascii_letters)
    mengzhaoxin.extend(range(10))
    mengzhaoxin=list(map(lambda x: str(x),mengzhaoxin))
    for i in range(200):
        random.shuffle(mengzhaoxin)
	print ''.join(mengzhaoxin[:20])

if __name__=='__main__':
    main()

