#!/usr/bin/python
# -*- coding: utf8 -*-
import socket, string, time, ssl
import urllib, re
import sys

network = 'irc.freenode.net'
nick = sys.argv[1]
chan = sys.argv[2]
password = sys.argv[3]
port = 6697

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def main(network, nick, chan, port, password):
  socket.connect((network,port))
  irc = ssl.wrap_socket(socket)
  def speak(message):
    irc.send(('PRIVMSG #%s :%s\r\n' % (chan,message)).encode('utf-8'))
  irc.send(('NICK %s\r\n' % nick).encode('utf-8'))
  time.sleep(1)
  print (irc.recv(4096))
  irc.send(('USER %s %s %s :My bot\r\n' % (nick,nick,nick)).encode('utf-8'))
  print (irc.recv(4096))
  time.sleep(1)
  irc.send(('PRIVMSG NickServ :IDENTIFY %s\r\n' % password).encode('utf-8'))
  print (irc.recv(4096))
  time.sleep(3)
  irc.send(('JOIN #%s\r\n' % chan).encode('utf-8'))
  print (irc.recv(4096))
  time.sleep(1)
  while True:
    try:  
      data = (irc.recv(4096)).decode('utf-8')
    except UnicodeDecodeError :
      print ('Warning: Received bytes cannot be decoded via utf-8!!!\r\n')
    print (data)
    if data.find('PING') != -1:
      irc.send(('PONG '+data.split()[1]+'\r\n').encode('utf-8'))
    if (data.find('摸摸') != -1 and data.find('摸摸') <3):
      speak('不哭不哭 站起来撸')
    if data.find('`嚎吧') != -1:
      speak('嗷呜~嗷呜~~~嗷呜~~~~~~~~~~~~~\r\n')
    if data.find('`poi') != -1:
      speak('❀(っ•∇•c)❀ ~poi ~poi ~poi\r\n')
    if (data.find('逃~') != -1) or (data.find('( 逃') != -1) or (data.find('(逃') != -1) :
      speak('逃什么逃！你丫就是一个没对象的野指针，哪会有人追你！\r\n')
    if data.find('`Shut up tjmbot!\r\n') != -1:
      irc.send('QUIT :吾去矣 \r\n'.encode('utf-8'))
      time.sleep(1)
      exit()
	  
if __name__=='__main__':
  main(network, nick, chan, port, password)
