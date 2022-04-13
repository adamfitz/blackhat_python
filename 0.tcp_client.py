import socket

target_host = f"www.google.com"
target_port = 80

# create the socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
# only bytes are put on the wire by default python3 does not automatically encode the message so a step to encode 
# the data is required
message = ("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
tcp_message = message.encode('utf-8')
client.send(tcp_message)

# receive the response data, 4096 bytes is the buffer size eg: receive up to 4096 bytes from this buffer
response = client.recv(4096)

print(response)

# Python3 socket library docs
# https://docs.python.org/3/library/socket.html