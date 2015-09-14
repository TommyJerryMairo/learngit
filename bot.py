while True:
	# 导入socket库:
	import socket
	#读取话语
	say = input()
	# 创建一个socket:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# 建立连接:
	s.connect(('198.2.252.181', 80))
	# 发送数据:
	s.send(b'GET /bot/bot.php?msg='+say.encode('utf-8')+b' HTTP/1.1\r\nHost: 198.2.252.181\r\nConnection: close\r\n\r\n')
	#接收数据:
	buffer = []
	while True:
		# 每次最多接收1k字节:
		d = s.recv(1024)
		if d:
			buffer.append(d)
		else:
			break
	data = b''.join(buffer)
	# 关闭连接:
	s.close()
	header, html = data.split(b'\r\n\r\n', 1)
	print(html.decode('utf-8'))
