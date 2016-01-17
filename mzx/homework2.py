#/usr/bin/env python3.4
# -*- coding: utf-8 -*-
import random
import string
import mysql.connector
import sys

def main(u,p,d):
    mengzhaoxin=list(string.ascii_letters)
    mengzhaoxin.extend(list(map(lambda x: str(x),range(10))))
    conn=mysql.connector.connect(user=u,password=p,database=d)
    cursor=conn.cursor()
    cursor.execute('drop table if exists verycode')
    cursor.execute('create table verycode (id int primary key, verification varchar(20))')
    for i in range(1,201):
        random.shuffle(mengzhaoxin)
        cursor.execute('insert into verycode (id, verification) values (%d, \'%s\')' % (i, ''.join(mengzhaoxin[:20])))
        cursor.rowcount
    conn.commit()
    cursor.close()
		
if __name__=='__main__':
    main(sys.argv[1],sys.argv[2],sys.argv[3])
