import sys, socket, struct


class TCPClient():
    def __init__(self, server_address, port):
        self.server_address = server_address
        self.port = port
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # self.client.bind((self.server_address, self.port))


    def setup_connection(self):
        self.client.connect((self.server_address, self.port))

    def teardown_connection(self):
        self.client.close()

    def send(self, instruction, data):
        concat_string = instruction + data
        byte_msg = bytes(concat_string, 'utf-8')
        send_msg = struct.pack('>I', len(byte_msg)) + byte_msg
        self.client.sendall(send_msg)
