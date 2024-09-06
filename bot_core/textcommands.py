# Here you write your command handlers
# the format should be func(bot, chat_id) with a proper decorator
from bot_core.decorators import html_text_response

@html_text_response
def start(bot, chat_id):
    return '<strong>Hello!</strong> I am a bot. How can I help you?'

@html_text_response
def help(bot, chat_id):
    return 'HALP!'