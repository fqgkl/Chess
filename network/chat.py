class Chat:
    def __init__(self):
        self.messages = []

    def send_message(self, user, message):
        self.messages.append(f"{user}: {message}")
        print(f"{user}: {message}")

chat = Chat()
chat.send_message("Игрок1", "Привет, удачи в партии!")
chat.send_message("Игрок2", "Спасибо! Тебе тоже.")
