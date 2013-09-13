import socket


#Create a TCP socket
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


#Connect the socket to port 3336 on our machine
tcp_socket.connect(("localhost", 3335))


#Send a message to the server
tcp_socket.send(raw_input("Enter a message: "))


#Await for a reply from the server
print "Server says:", tcp_socket.recv(1024)


#Close our connection
tcp_socket.close()