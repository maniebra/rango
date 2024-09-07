import telepot
from functools import wraps

def html_text_response(func):
    def wrapper(*args, **kwargs):
        bot: telepot.Bot = args[0]
        chat_id = args[1]
        response = func(*args, **kwargs)
        bot.sendMessage(chat_id, response, parse_mode='HTML')
        return response
    return wrapper

def normal_text_response(func):
    def wrapper(*args, **kwargs):
        bot: telepot.Bot = args[0]
        chat_id = args[1]
        response = func(*args, **kwargs)
        bot.sendMessage(chat_id, response)
        return response
    return wrapper
