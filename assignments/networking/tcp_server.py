import socket


#Create a TCP socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Bind the socket to port 3336 on our machine and listen for connections
tcp_socket.bind(("localhost", 3335))
tcp_socket.listen(1)    #Serve only 1 connection at a time


#Await for connection from client
print "Awaiting for connection from client..."
client_socket, client_address = tcp_socket.accept()    #Blocking line


#Connection acknowledge, printing the message we got from the client
print "Connection received from", client_address
print "Client says:", client_socket.recv(1024)   #Blocking line


#Sending a response back to the client
client_socket.send("Server has acknowledge your connection :D")


#Close the connection between the server and the client
client_socket.close()


#Close our binded socket
tcp_socket.close()