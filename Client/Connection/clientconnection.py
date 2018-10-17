import sys, socket, struct


class TCPClient():
	def __init__(self, server_address, port):
		self.server_address = server_address
		self.port = port
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		# self.client.bind((self.server_address, self.port))


	def setupConnection(self):
		self.client.connect((self.server_address, self.port))

	def teardownConnection(self):
		self.client.close()

	def sendNames(self, instruction, data):
		'''Function used for sending folder and file names'''
		concat_string = instruction + data
		print(len(concat_string))
		byte_msg = bytes(concat_string, 'utf-8')
		send_msg = struct.pack('>I', len(byte_msg)) + byte_msg
		self.client.sendall(send_msg)

	def sendBytes(self, data):
		'''Function used for sending data'''
		print(len(data))
		send_msg = struct.pack('>I', len(data)) + data
		self.client.sendall(send_msg)
