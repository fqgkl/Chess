class Chat:
    """
    Класс Chat реализует систему обмена сообщениями между игроками.
    """
    def __init__(self):
        """
        Инициализация чата.
        """
        self.messages = []

    def send_message(self, user, message):
        """
        Отправляет сообщение в чат.
        
        :param user: Имя пользователя
        :param message: Текст сообщения
        """
        self.messages.append(f"{user}: {message}")
        print(f"{user}: {message}")