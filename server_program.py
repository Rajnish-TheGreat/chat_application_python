import socket

import threading

import time

# IPV4
address_family = socket.AF_INET

# UDP
protocol = socket.SOCK_DGRAM

# socket

ip = '127.0.0.1'
port = 5000


server_socket = socket.socket(address_family, protocol)


# bind

server_socket.bind((ip, port))


# send and receive function


def send_msg(address):
    data = input("Server: ").encode()
    if len(data) < 0:
        return
    server_socket.sendto(data, address)


def receive_msg():
    while True:
        message, address = server_socket.recvfrom(1024)
        message = message.decode()
        print(f"{address[0]} : {message}")
   
        data = input("Server: ").encode()
       
        if len(data) < 0:
            return
        server_socket.sendto(data, address)
      
        


# send and recv message


threading.Thread(target=receive_msg).start()
# time.sleep(20)
# threading.Thread(target=send_msg,args=(address,)).start()
