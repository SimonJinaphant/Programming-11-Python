import socket

#Create a UDP socket with socket.SOCK_DGRAM
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#Bind the socket to listen for anything on port 3335
udp_socket.bind(("localhost", 3335))
print "Awaiting for any messages..."

#Print the message we got from the UDP client
message, client_address = udp_socket.recvfrom(1024)
print "Message recived from", client_address
print "Client says: ", message


#Don't forget to close the socket now
udp_socket.close()
