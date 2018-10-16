# What needs to be done:

## Client

### Communication
- Needs to request a TCP/IP connection to a server
- Once established, it needs to keep it open
- Needs to detect if the connection is lost, if it is, go into reconnect mode
- If a folder is added, it will send a notification to the server, which then needs to create the file with the same relative path. Same with deleted.
- If a file is altered, it needs to send line by line what needs to be edited, and what line number it is. Can create a checksum for each line.
### Detection of change in folder
- If a file is added or removed, it needs to know that, can check it periodically, e.g., every 10 seconds.
### Detection of change in file
- Might have line by line checksum

## Server

### Communication
- Needs to accept a connection over TCP/IP.
- Once established, it needs to keep it open.
- Needs to detect if the connection is lost, if it is, go into reconnect mode

### Inserting file into folder
- If message is received with the "Add file" key, add the file
- If a message is received with the "Remove file" key, remove the file
### Inserting into single file
- Create checksum for file


## Problems
- When something is e.g., altered in a file, how does it know it will be synchronized?
    - Line by line scanning and comparing? Replace the lines that are changed?
    - Having some kind of checksum for each file?
- How to deal with weird files, such as pictures?


## Approach
1. Set up a connection, and send simple messages
2. Detect if a file/folder was added.
3. Send the path to the server.
4. Create a file/ with the same name on the server side.
