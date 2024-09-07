# Here you write your command handlers
# the format should be func(bot, chat_id) with a proper decorator
import telepot.namedtuple

from bot_core.decorators import html_text_response
from main import tg_id, tg_username
from models import User
from utils.permissions.decorators import permission_class


@html_text_response
@permission_class("active")
def start(bot, chat_id, msg):
    User.create(tg_id=chat_id, tg_username=telepot)
    return '<strong>Hello!</strong> I am a bot. How can I help you?'

@html_text_response
@permission_class("active")
def help(bot, chat_id, msg):
    return 'HALP!'

@html_text_response
@permission_class("admin")
def admin(bot, chat_id, msg):
    return "HEY ADMIN!"