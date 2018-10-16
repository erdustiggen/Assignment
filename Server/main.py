import time
from Connection.serverConnection import TCPServer


def main():
    tcpServer = TCPServer("127.0.0.1", 2000)
    tcpServer.setup_connection()
    try:
        while True:
            recv_message = tcpServer.receive()
            if(recv_message != None):
                # Here is where we need to do something
                print(recv_message)
    except KeyboardInterrupt:
        pass

    tcpServer.teardown_connection()

if __name__ == '__main__':
    main()
