from foodForModel import BASE_MESSAGES


class Messages:
    def __init__(self):
       self.__messages=BASE_MESSAGES
    def add_message(self,role,content):
        if role not in {"user","assistant","system"}:
            print("ERROR: the role should be either user or assistant")
            return False
        self.__messages.append({"role":role,"content":content})
        return self.__messages

    def get_message(self):
        return self.__messages
    def get_messages_by_role(self,role):
        msg_by_role=[]
        for message in self.__messages:
            if message["role"] == role:
                 msg_by_role.append(message)
        return msg_by_role
