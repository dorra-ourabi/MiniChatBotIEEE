from foodForModel import BASE_MESSAGES

from Response_typeClass import *


class ChatBot:

    def __init__(self, response_type):
        self.__response_type = response_type

    def talk(self):
        # code that declares the client object:

        client = self.__response_type.get_client()

        messages = self.__response_type.get_messages()

        conversation = []

        print("- Hello is there anything you want to know about IEEE INSAT?")
        while True:
            n = input("-")
            if n in ["Goodbye", "quit"]:
                print("- Goodbye")
                break

            messages.add_message("user", n)
            conversation.append([{"role": "user", "content": n}])
            response = client.chat.completions.create(
                        model=self.__response_type.get_model(),
                        max_tokens=self.__response_type.get_max_tokens(),
                        messages=self.__response_type.get_messages().get_message(),
                        temperature=self.__response_type.get_temperature(),

            )

            print("-" + response.choices[0].message.content)

            x = {"role": "assistant", "content": response.choices[0].message.content}
            messages.add_message("assistant",response.choices[0].message.content)
            conversation.append(x)
        return conversation


