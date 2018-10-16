# import os, time
# path_to_watch_list = ["/home/erdustiggen/Programming/Pexip/Assignment/DirToWatch/"]
# for path_to_watch in path_to_watch_list:
#     before = dict ([(f, None) for f in os.listdir (path_to_watch)])
#
# while 1:
#   time.sleep (10)
#   for path_to_watch in path_to_watch_list:
#       after = dict ([(f, None) for f in os.listdir (path_to_watch)])
#       added = [f for f in after if not f in before]
#       removed = [f for f in before if not f in after]
#       if added: print ("Added: ", ", ".join (added))
#       if removed: print ("Removed: ", ", ".join (removed))
#       before = after
#       root, dirs, files = next(os.walk(path_to_watch))
#       print ('directories:', dirs)
#       print ('files:', files)
import os, time

# file_paths = []
# directory_paths = []
# root_dir_to_watch = "/home/erdustiggen/Programming/Pexip/Assignment/DirToWatch/"
# while 1:
#     time.sleep(5)
#     for dirpath,dir_name,filenames in os.walk(root_dir_to_watch):
#         for d in dir_name:
#             new_dir = os.path.abspath(os.path.join(dirpath, d))
#             if new_dir not in directory_paths:
#                 directory_paths.append(new_dir)
#
#         for f in filenames:
#             new_file = os.path.abspath(os.path.join(dirpath, f))
#             if new_file not in file_paths:
#                 file_paths.append(new_file)
#
#     print(file_paths)
#     print(directory_paths)

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
