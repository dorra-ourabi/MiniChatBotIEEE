from ChatClass import *
from ChatBotConfigClass import *
from MessagesClass import *
from ClientClass import *
from chatAudioClass import *

client_obj=Client("OPENAI_API_KEY","https://openrouter.ai/api/v1")
client=client_obj.get_client()
messages=Messages()
messages.add_message("system","you're a kind and friendly systemt aht answers exactly the question asked and does not put previous answers")
#messages.add_message("assistant","What is Insat?")
#messages.add_message("system","INSAT: National Institute of Applied Science and Technology The National Institute of Applied Science and Technology (INSAT) is a Tunisian engineering school located in Tunis. It is one of the most prestigious engineering schools in Tunisia. INSAT is a public institution of higher education and scientific research. It is a member of the University of Carthage..")
config =ChatBotConfig(client,"openai/gpt-5.4-nano",messages,100,0)
chatbot=ChatBot(config)
voice_chatbot = VoiceChatBot(chatbot)
conversation=voice_chatbot.talk()
#print(conversation)