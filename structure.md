# Structure of modules

## Client
### main
As there is no demand for a fast application, the main is a single while loop that iterates through different statements,
and based on the situation will execute different tasks.
First, it checks if a connection is established, if not it requests a connection.
If the connection was not established, it checks the content of the folder it watches, and sends the name and content of each folder and file in the main folder
along with a keyword that lets the Server know what needs to be done.
Then, for each file, it sends 
