from openai import OpenAI
import os
class Client:
    instance=None
    client_created=False
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls)
        return cls.instance
    def __init__(self,api_key,base_url):
        self.__api_key = api_key
        self.__base_url = base_url

        if  not self.client_created:
            self.__client = OpenAI(api_key=os.getenv(self.__api_key), base_url=self.__base_url)
            self.client_created=True

    def get_client(self):

        return self.__client



