#/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import random
import string
import mysql.connector
import sys

def main(u,p,d):
    mengzhaoxin=list(string.ascii_letters)
    mengzhaoxin.extend(range(10))
	conn=mysql.connector.connect(user=u,password=p,database=d)
	cursor=conn.cursor()
	cursor.execute('create table user (id int primary key, verification varchar(20))')
    for i in range(200):
        random.shuffle(mengzhaoxin)
	cursor.execute('insert into user (id, name) values (%s, %s)', [i, ''.join(mengzhaoxin[:20])])
	cursor.rowcount
	conn.commit()
	cursor.close()
		
if __name__=='__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])
