import socket

class ChessServer:
    def __init__(self, host="localhost", port=12345):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        self.server.listen(2)
        print("Chess server started...")

    def accept_connections(self):
        conn, addr = self.server.accept()
        print(f"Connected by {addr}")
        return conn

if __name__ == "__main__":
    server = ChessServer()
    server.accept_connections()
