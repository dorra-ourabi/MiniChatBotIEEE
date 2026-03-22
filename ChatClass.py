
class ChatBot:

    def __init__(self, chatbotconfig):
        self.__chatbotconfig = chatbotconfig
    def get_config(self):
        return self.__chatbotconfig
    def get_input(self):
        n = input("-")
        return n
    def ask_LLM(self):
        client = self.__chatbotconfig.get_client()
        response = client.chat.completions.create(
            model=self.__chatbotconfig.get_model(),
            max_tokens=self.__chatbotconfig.get_max_tokens(),
            messages=self.__chatbotconfig.get_messages().get_message(),
            temperature=self.__chatbotconfig.get_temperature(),

        )


        return response.choices[0].message.content

    def deliver_output(self,response):
        print("-"+response)

    def talk(self):
        # code that declares the client object:



        messages = self.__chatbotconfig.get_messages()

        conversation = []

        print("- Hello is there anything you want to know about IEEE INSAT?")
        while True:
            n=self.get_input()
            if n in ["Goodbye","bye","quit","goodbye"]:
                print("Goodbye")
                break

            messages.add_message("user", n)
            conversation.append([{"role": "user", "content": n}])
            LLM_response=self.ask_LLM()



            x = {"role": "assistant", "content": LLM_response}
            messages.add_message("assistant",LLM_response)
            conversation.append(x)
            self.deliver_output(LLM_response)
        return conversation


