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
  irc.send('NICK %s\r\n' % nick)
  print irc.recv(4096)
  irc.send('USER %s %s %s :My bot\r\n' % (nick,nick,nick))
  print irc.recv(4096)
  irc.send('PRIVMSG NickServ :IDENTIFY %s\r\n' % password)
  print irc.recv(4096)
  time.sleep(3)
  irc.send('JOIN #%s\r\n' % chan)
  print irc.recv(4096)
  while True:
    data = irc.recv(4096)
    print data
    if data.find('`PING') != -1:
      irc.send('PONG '+data.split()[1]+'\r\n')
    if data.find('`gtfo\r\n') != -1:
      irc.send('QUIT\r\n')
      exit()
    print data
if __name__=='__main__':
  main(network, nick, chan, port, password)