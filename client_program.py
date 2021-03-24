import socket

import threading

import time

# IPV4
address_family = socket.AF_INET

# UDP
protocol = socket.SOCK_DGRAM

# socket

server_ip = '127.0.0.1'
server_port = 5000


client_socket = socket.socket(address_family, protocol)


server_address = (server_ip,server_port)

# send and receive function


def send_msg():
   
    while True:
        
        data = input("Me: ").encode()
        if len(data) < 0:
            return
        client_socket.sendto(data, server_address)
        time.sleep(5)

def receive_msg():
    time.sleep(10)
    while True:
        
        message, address = client_socket.recvfrom(1024)
            
        message = message.decode()
        print(f"Server : {message}")
  



# send and recv message

threading.Thread(target=send_msg).start()

threading.Thread(target=receive_msg).start() 
  
  
