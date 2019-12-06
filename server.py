import socket
import threading

HOST = '127.0.0.1'
PORT = 65432

def echo(conn):
	while True:
		print ('Waiting for  message: ')
		message = conn.recv(1024)
		if not message:
			print('closing connection')
			return
		print ('message received!')
		conn.send(message)
		print ('message was echoed back')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)						 #Initiates the socket with IPV4 and TCP connection
s.bind((HOST,PORT)) 				     						 # binds socket to HOST and PORT on local host
s.listen(5) 					     						 # listens for incoming connections with max of 5  clients

while True:
	print('waiting for incoming conn: ')
	(conn,addr) = s.accept()
	print ('Connection received.. Connected to: ', addr)
	conn.send(b'Thanks for connecting to the server...Init THREAD')
	threading.Thread(target = echo, args = [conn]).start()




