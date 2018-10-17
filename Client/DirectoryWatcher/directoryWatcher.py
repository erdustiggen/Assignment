import os, time, hashlib

class DirectoryWatcher():
	def __init__(self, root_dir_to_watch):
		self.root_dir_to_watch = root_dir_to_watch
		self.directory_paths = []
		self.file_paths = []
		self.new_dirs = []
		self.new_files = []
		self.current_dirs = []
		self.current_files = []
		self.removed_dirs = []
		self.removed_files = []
		self.checksum = []

	def check_for_updates(self):
		self.new_dirs = []
		self.new_files = []
		self.removed_dirs = []
		self.removed_files = []
		self.current_dirs = []
		self.current_files = []
		for dirpath,dir_name,filenames in os.walk(self.root_dir_to_watch):
			for d in dir_name:
				new_dir = os.path.abspath(os.path.join(dirpath, d))
				self.current_dirs.append(new_dir)
				if new_dir not in self.directory_paths:
					self.directory_paths.append(new_dir)
					self.new_dirs.append(new_dir)
			for f in filenames:
				new_file = os.path.abspath(os.path.join(dirpath, f))
				self.current_files.append(new_file)
				if new_file not in self.file_paths:
					self.file_paths.append(new_file)
					self.new_files.append(new_file)

		for d in self.directory_paths:
			if d not in self.current_dirs:
				self.directory_paths.remove(d)
				self.removed_dirs.append(d)

				for f in self.file_paths:
					if f not in self.current_files:
						self.file_paths.remove(f)
						self.removed_files.append(f)


		return self.new_dirs, self.removed_dirs, self.new_files, self.removed_files


	def file_as_bytes(self, file):
		with file:
			return file.read()

	def checkForChanges(self):
		checksum = [(fname, hashlib.sha256(self.file_as_bytes(open(fname, 'rb'))).digest()) for fname in self.file_paths]

		if(len(self.checksum) < len(checksum)):
			for i in range(len(self.checksum), len(checksum)):
				self.checksum.append(checksum[i])

		for i in range(0, len(checksum)):
			print (self.checksum[i])
			print (checksum[i])
			if (self.checksum[i] != checksum[i]):
				print("Checksum altered")
				self.checksum[i] = checksum[i]
