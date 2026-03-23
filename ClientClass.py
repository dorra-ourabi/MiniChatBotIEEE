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
        self._api_key = api_key
        self._base_url = base_url

        if  not self.client_created:
            self._client = OpenAI(api_key=os.getenv(self._api_key), base_url=self._base_url)
            self.client_created=True

    def get_client(self):

        return self._client

"""this class uses the design pattern sigleton the connection to the LLM only happens once"""

