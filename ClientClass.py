from openai import OpenAI
import os
class Client:
    def __init__(self,api_key,base_url):
        self.__api_key = api_key
        self.__base_url = base_url
    def make_client(self):
        client = OpenAI(api_key=os.getenv(self.__api_key),base_url=self.__base_url)
        return client



