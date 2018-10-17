from watchdog.events import FileSystemEventHandler

class FileHandler():
	def getFileContents(self, path):
		f = open(path, 'rb')
		content = f.read()
		f.close()
		return content
