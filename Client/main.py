import time
from Connection.clientConnection import TCPClient
from DirectoryWatcher.directoryWatcher import DirectoryWatcher
from FileHandler.fileHandler import FileHandler



def main():
	# Simple tcp connection and send
	tcpClient = TCPClient("127.0.0.1", 2000)
	tcpClient.setup_connection()
	# tcpClient.send("lel", "hihi")
	# tcpClient.teardown_connection()

	# Checking for directory changes
	dirWatcher = DirectoryWatcher("/home/emil/Programming/Pexip/Assignment/DirToWatch")
	fileHandler = FileHandler()

	try:
		while True:
			new_dirs, removed_dirs, new_files, removed_files = dirWatcher.check_for_updates()
			if(new_dirs):
				for data in new_dirs:
					tcpClient.send("A_D", data[50:])
			if(removed_dirs):
				for data in removed_dirs:
					tcpClient.send("D_D", data[50:])
			if(new_files):
				for data in new_files:
					file_contents = fileHandler.getFileContents(data)
					tcpClient.send("A_F", data[50:])
					byte_prefix = "INS".encode("utf-8") +  "!".encode("utf-8") + data[50:].encode("utf-8") + "|".encode("utf-8")
					tcpClient.sendBytes(byte_prefix + file_contents)
			if(removed_files):
				for data in removed_files:
					tcpClient.send("D_F", data[50:])

			dirWatcher.checkForChanges()
			time.sleep(5)
	except KeyboardInterrupt:
		tcpClient.teardown_connection()
		pass

if __name__ == '__main__':
	main()
