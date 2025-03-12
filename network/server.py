import socket

class Server:
    """
    Класс Server реализует сервер для сетевой игры.
    """
    def __init__(self, host="0.0.0.0", port=5555):
        """
        Инициализация сервера.
        
        :param host: Адрес сервера
        :param port: Порт сервера
        """
        self.host = host
        self.port = port

    def start(self):
        """
        Запускает сервер и ожидает подключения игроков.
        """
        print("Сервер запущен. Ожидание игроков...")
