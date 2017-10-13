class JimMessage:
    def __init__(self):
        pass


class Chat:
    def __init__(self):
        self.clients = []
        self.messages = []


class ChatController:
    def __init__(self):
        pass



class ChatView:
    def __init__(self):
        pass

    def get_message(self):
        pass

    def show_message(self):
        pass


class ConsoleChatView(ChatView):
    def __init__(self):
        super().__init__()
        pass


class Storage:
    def __init__(self):
        pass


class FileStorage(Storage):
    def __init__(self):
        super().__init__()
        pass

    def save_chat(self):
        pass

    def load_chat(self):
        pass


class Server:
    def __init__(self):
        self.clients = []
        self.chats = []
        self.storage


class Client:
    def __init__(self):
        self.server
        self.chat_view
