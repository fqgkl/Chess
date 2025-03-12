import socket

class Client:
    """
    Класс Client представляет клиента для подключения к серверу.
    """
    def __init__(self, server_ip="127.0.0.1", server_port=5555):
        """
        Инициализация клиента.
        
        :param server_ip: IP-адрес сервера
        :param server_port: Порт сервера
        """
        self.server_ip = server_ip
        self.server_port = server_port

    def connect(self):
        """
        Подключается к серверу и получает сообщение.
        """
        print("Подключение к серверу...")
