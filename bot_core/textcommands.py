# Here you write your command handlers
# the format should be func(bot, chat_id) with a proper decorator
import telepot.namedtuple

from bot_core.decorators import html_text_response
from models import User
from utils.permissions.decorators import permission_class


@html_text_response
@permission_class("base")
def start(bot, chat_id, msg):
    user_data = bot.getChat(chat_id)
    User.create(tg_id=chat_id, tg_username=user_data["username"],
                first_name=user_data["first_name"], last_name=user_data["last_name"])
    return f'<strong>Hello, {user_data["first_name"]}!</strong> I am a bot. How can I help you?'

@html_text_response
@permission_class("active")
def help(bot, chat_id, msg):
    return 'HALP!'

@html_text_response
@permission_class("admin")
def admin(bot, chat_id, msg):
    return "HEY ADMIN!"

@html_text_response
@permission_class("active")
def submit(bot, chat_id, msg):
    return "<strong>SUBMIT!</strong> I am a bot. How can I help you?"