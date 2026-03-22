import speech_recognition as sr
import pyttsx3
from ChatClass import *


class VoiceChatBot(ChatBot):
    def __init__(self, chatbot):
        super().__init__(chatbot.get_config())
        self.__chatbot = chatbot
        self.__engine = pyttsx3.init()
        self.__recognizer = sr.Recognizer()
        self.__microphone = sr.Microphone()
        with self.__microphone as source:
            self.__recognizer.adjust_for_ambient_noise(source)

    def get_input(self):
        with self.__microphone as source:
            while True:
                print("Listening...")
                try:
                    audio = self.__recognizer.listen(source, phrase_time_limit=10)
                    text = self.__recognizer.recognize_google(audio)
                    print("-" + text)
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Please repeat.")

    # try again recursively

    def deliver_output(self, response):
        print("-" + response)


    # speech output

    def ask_LLM(self):
        return self.__chatbot.ask_LLM()