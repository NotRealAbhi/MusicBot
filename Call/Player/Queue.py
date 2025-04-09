"""
Telegram @NotRealBhi
Copyright ©️ 2025
"""

queues = {}  # In-memory Queue: {chat_id: [dict(song info), ...]}


def add_to_queue(chat_id, song_data):
    if chat_id not in queues:
        queues[chat_id] = []
    queues[chat_id].append(song_data)


def get_queue(chat_id):
    return queues.get(chat_id, [])


def clear_queue(chat_id):
    queues[chat_id] = []


def remove_from_queue(chat_id, index):
    if chat_id in queues and len(queues[chat_id]) > index:
        return queues[chat_id].pop(index)
    return None
  
