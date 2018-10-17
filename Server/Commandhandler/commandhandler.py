import os, shutil


class DirModifier():
	''' Class used for Creating files and folders.'''
	def __init__(self, folder_path):
		self.folder_path = folder_path

	def makeDir(self, path):
		path = self.folder_path + path
		if not (os.path.exists(path)):
			os.mkdir(path)

	def removeDir(self, path):
		path = self.folder_path + path
		if (os.path.exists(path)):
			shutil.rmtree(path, ignore_errors = True)

	def makeFile(self, path):
		path = self.folder_path + path
		f = open(path, "w+")
		f.close()

	def removeFile(self, path):
		path = self.folder_path + path
		if os.path.exists(path):
  			os.remove(path)
		else:
			pass

class FileModifier():
	''' Class used for altering files.'''
	def __init__(self, folder_path):
		self.folder_path = folder_path

	def insertToFile(self, path, data):
		path = self.folder_path + path.decode("utf-8")
		if (type(data) == bytes):
			f = open(path, "wb")
			f.write(data)
			f.close()
		else:
			f = open(path, "w")
			f.write(data)
			f.close()

class CommandHandler():
	def __init__(self, folder_path):
		self.dirHandler = DirModifier(folder_path)
		self.fileHandler = FileModifier(folder_path)

	def handleCommand(self,recv_message):
		if(recv_message[:3] == b'A_D'):
			path = recv_message[3:].decode("utf-8")
			self.dirHandler.makeDir(path)
		if(recv_message[:3] == b'D_D'):
			path = recv_message[3:].decode("utf-8")
			self.dirHandler.removeDir(path)
		if(recv_message[:3] == b'A_F'):
			path = recv_message[3:].decode("utf-8")
			self.dirHandler.makeFile(path)
		if(recv_message[:3] == b'D_F'):
			path = recv_message[3:].decode("utf-8")
			self.dirHandler.removeFile(path)
		if(recv_message[:3] == b'INS'):
			path = recv_message[recv_message.find(b"!")+1:recv_message.find(b"|")]
			data = recv_message[recv_message.find(b"|")+1:]
			self.fileHandler.insertToFile(path, data)
