import socket

#Create a UDP socket with socket.SOCK_DGRAM
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


#Since UDP doesn't need to connect we can start sending away
udp_socket.sendto(raw_input("Enter a message: "), ("localhost", 3335))


#Don't forget to close the socket now :)
udp_socket.close()