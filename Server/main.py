import time
from Connection.serverConnection import TCPServer
from Commandhandler.commandhandler import CommandHandler

path_to_dir = "/home/emil/Programming/Pexip/Assignment/DirToInsert"

def main():
	commandHandler = CommandHandler(path_to_dir)
	tcpServer = TCPServer("127.0.0.1", 2000)
	tcpServer.setup_connection()
	try:
		while True:
			recv_message = tcpServer.receive()
			if(recv_message != None):
				commandHandler.handleCommand(recv_message)

	except KeyboardInterrupt:
		tcpServer.teardown_connection()

if __name__ == '__main__':
    main()
