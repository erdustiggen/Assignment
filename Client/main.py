import time, sys
from Connection.clientconnection import TCPClient
from Directorywatcher.directorywatcher import DirectoryWatcher, FileHandler


def main(argv):

	tcpClient = TCPClient("127.0.0.1", 2000)
	tcpClient.setupConnection()

	dirWatcher = DirectoryWatcher(argv[0])
	fileHandler = FileHandler()

	try:
		while True:
			# Checking if any file or directory have been removed or added, if so, send information to Server.
			new_dirs, removed_dirs, new_files, removed_files = dirWatcher.checkForDirChanges()
			if(new_dirs):
				for data in new_dirs:
					tcpClient.sendNames("A_D", data[50:])
			if(removed_dirs):
				for data in removed_dirs:
					tcpClient.sendNames("D_D", data[50:])
			if(new_files):
				for data in new_files:
					file_contents = fileHandler.getFileContents(data)
					tcpClient.sendNames("A_F", data[50:])
					byte_prefix = "INS".encode("utf-8") +  "!".encode("utf-8") + data[50:].encode("utf-8") + "|".encode("utf-8")
					print(data[50:])
					tcpClient.sendBytes(byte_prefix + file_contents)
			if(removed_files):
				for data in removed_files:
					tcpClient.sendNames("D_F", data[50:])

			# Checking if any of the files have been altred, if yes, send it again.
			changed_files = dirWatcher.checkForChanges()
			for cf in changed_files:
				file_contents = fileHandler.getFileContents(cf)
				byte_prefix = "INS".encode("utf-8") +  "!".encode("utf-8") + cf[50:].encode("utf-8") + "|".encode("utf-8")
				print(cf[50:])
				tcpClient.sendBytes(byte_prefix + file_contents)
			time.sleep(5)

	except KeyboardInterrupt:
		tcpClient.teardownConnection()

if __name__ == '__main__':
	main(sys.argv[1:])
