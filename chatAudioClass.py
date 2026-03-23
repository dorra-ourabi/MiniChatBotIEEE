import speech_recognition as sr
import pyttsx3
from ChatClass import *


class VoiceChatBot(ChatBot):
    def __init__(self, chatbot):
        super().__init__(chatbot.get_config())
        self._chatbot = chatbot
        self._engine = pyttsx3.init()
        self._recognizer = sr.Recognizer()
        self._microphone = sr.Microphone()
        with self._microphone as source:
            self._recognizer.adjust_for_ambient_noise(source)

    def get_input(self):
        with self._microphone as source:
            while True:
                print("Listening...")
                try:
                    audio = self._recognizer.listen(source, phrase_time_limit=10)
                    text = self._recognizer.recognize_google(audio)
                    print("-" + text)
                    return text
                except sr.UnknownValueError:
                    print("Sorry, I didn't catch that. Please repeat.")

    # try again recursively

    def deliver_output(self, response):
        print("-" + response)


    # speech output

    def ask_LLM(self):
        return self._chatbot.ask_LLM()