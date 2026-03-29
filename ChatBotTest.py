from ChatClass import *
from ChatBotConfigClass import *
from MessagesClass import *
from ClientClass import *
from chatAudioClass import *
from DynamicScraperClass import *
from HtmlScraperClass import *

client_obj=Client("OPENAI_API_KEY","https://openrouter.ai/api/v1")
client=client_obj.get_client()
messages=Messages()
messages.add_message("system","you're a kind and friendly systemt aht answers exactly the question asked and does not put previous answers")

config =ChatBotConfig(client,"openai/gpt-5.4-nano",messages,100,0)
scraper = HtmlScraper("https://insat.ieee.tn/#/who-are-we")
scraper.scrape_to_file("IEEE_website.txt")
#chatbot=ChatBot(config)
#voice_chatbot = VoiceChatBot(chatbot)
#conversation1=voice_chatbot.talk()
#conversation2=chatbot.talk()
#print(conversation)