import telepot
from telepot.loop import MessageLoop
from . import textcommands
from utils.settings import BOT_TOKEN

bot = telepot.Bot(BOT_TOKEN)

def generate_listener_text():
    bot_info = bot.getMe()
    return 'Listening to [@' + bot_info['username'] + '] bot ...'

def send_message(chat_id, message):
    bot.sendMessage(chat_id, message)


def on_chat_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type == 'text':
        command_text = msg['text'].replace("/","").lower()

        try:
            command = getattr(textcommands, command_text)
        except AttributeError:
            send_message(chat_id, 'I do not understand you. please try again!')

        if callable(command):
            command(bot, chat_id, msg)
        else:
            send_message(chat_id, 'This command it not available. Please try again.')

handler = {
    'chat': on_chat_message
}

MessageLoop(bot, handler).run_as_thread()