from openai import OpenAI
from foodForModel import BASE_MESSAGES
import os


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


conversation=[]
print("- Hello is there anything you want to know about IEEE INSAT?")
while True:
     n=input("- ")
     if n in ["Goodbye","quit"]:
         print("- Goodbye")
         break

     m={"role":"user","content":n}
     messages=BASE_MESSAGES+[m]
     conversation.append(m)
     response = client.chat.completions.create(
        model="mistralai/mistral-7b-instruct",
        messages= messages,
        temperature=0,

        )

     print ("-"+response.choices[0].message.content)
     x={"role":"assistant","content":n}
     conversation.append(x)

