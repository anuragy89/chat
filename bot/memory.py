from bot.database import memory

def save_message(chat_id, user_id, text):
    memory.insert_one({
        "chat_id": chat_id,
        "user_id": user_id,
        "text": text[:200]
    })
