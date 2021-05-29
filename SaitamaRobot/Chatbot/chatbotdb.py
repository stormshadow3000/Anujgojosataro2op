from SaitamaRobot import db 

chatbotdb = db.chatbot


def add_chat(chat_id):
    stark = chatbotdb.find_one({"chat_id": chat_id})
    if stark:
        return False
    else:
        chatbotdb.insert_one({"chat_id": chat_id})
        return True


def remove_chat(chat_id):
    stark = chatbotdb.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        chatbotdb.delete_one({"chat_id": chat_id})
        return True


def get_all_chats():
    r = list(chatbotdb.find())
    if r:
        return r
    else:
        return False


def get_session(chat_id):
    stark = chatbotdb.find_one({"chat_id": chat_id})
    if not stark:
        return False
    else:
        return stark
