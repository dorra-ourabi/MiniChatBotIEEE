
class ChatBotConfig:
    def __init__(self, client,model,messages,max_tokens,temperature):
        self.__client = client
        self.__model = model
        self.__messages = messages
        self.__max_tokens = max_tokens
        self.__temperature = temperature
    def get_messages(self):
        return self.__messages
    def get_max_tokens(self):
        return self.__max_tokens
    def get_temperature(self):
        return self.__temperature
    def get_client(self):
        return self.__client
    def get_model(self):
        return self.__model
