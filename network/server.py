import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 5555))
server.listen(2)

print("Сервер запущен. Ожидание игроков...")

while True:
    conn, addr = server.accept()
    print(f"Игрок подключился: {addr}")
    conn.send("Добро пожаловать в сетевую шахматную игру!".encode())
    conn.close()
