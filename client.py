import socket
import threading

HOST = '127.0.0.1'
PORT = 65432


def getMsg(conn):
	while True:
		message = s.recv(1024)
		if not message:
			print ('Disconnected')
			return
		print (message



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print ('Connecting to Server...')
s.connect((HOST,PORT))
print ('Start receive thread..')
threading.Thread(target = getMsg, args = [s]).start()

while True:
	print ('Enter msg to be echoed back: ')
	message = input('>').encode()
	s.send(message)













