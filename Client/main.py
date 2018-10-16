import time
from Connection.clientConnection import TCPClient
from DirectoryWatcher.directoryWatcher import DirectoryWatcher


def main():
    # Simple tcp connection and send
    tcpClient = TCPClient("127.0.0.1", 2000)
    tcpClient.setup_connection()
    # tcpClient.send("lel", "hihi")
    # tcpClient.teardown_connection()

    # Checking for directory changes
    dirWatcher = DirectoryWatcher("/home/erdustiggen/Programming/Pexip/Assignment/DirToWatch")

    try:
        while True:
            new_dirs, removed_dirs, new_files, removed_files = dirWatcher.check_for_updates()
            if(new_dirs):
                for data in new_dirs:
                    tcpClient.send("AD_-_", data)
            time.sleep(5)
    except KeyboardInterrupt:
        pass

if __name__ == '__main__':
    main()
