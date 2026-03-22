from ChatClass import *
from Response_typeClass import *
from MessagesClass import *
from ClientClass import *


client=Client("OPENAI_API_KEY","https://openrouter.ai/api/v1")
messages=Messages()
response_type=Response_type(client,"openai/gpt-5.4-nano",messages,50,0)
chatbot=ChatBot(response_type)
chatbot.talk()