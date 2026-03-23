
class ChatBotConfig:
    def __init__(self, client,model,messages,max_tokens,temperature):
        self._client = client
        self._model = model
        self._messages = messages
        self._max_tokens = max_tokens
        self._temperature = temperature
    def get_messages(self):
        return self._messages
    def get_max_tokens(self):
        return self._max_tokens
    def get_temperature(self):
        return self._temperature
    def get_client(self):
        return self._client
    def get_model(self):
        return self._model
