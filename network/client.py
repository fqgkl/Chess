import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

message = client.recv(1024).decode()
print(message)
client.close()
