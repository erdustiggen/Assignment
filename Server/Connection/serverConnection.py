import sys, socket, struct


class TCPServer():
    '''A class responsible for connecting with the client and receiving changes'''
    def __init__(self, client_address, port):
        self.client_address = client_address
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.client_address, self.port))


    def setup_connection(self):
        self.socket.listen(1)
        self.connection, client_address = self.socket.accept()
        print("Received connection")

    def teardown_connection(self):
        self.socket.close()

    def read_message(self, msg_len):
        '''Helper function for receiving messages of unknown length'''
        data = b''
        while len(data) < msg_len:
            packet = self.connection.recv(msg_len - len(data))
            if not packet:
                return None
            data += packet
        return data

    def receive(self):
        ''' For receiving messages'''

        # The first four bytes is always the message length
        raw_msglen = self.read_message(4)
        if not raw_msglen:
            return None
        msg_len = struct.unpack('>I', raw_msglen)[0]
        # Read the whole message
        return self.read_message(msg_len)
