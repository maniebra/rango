from time import sleep

from bot_core.bothandlers import generate_listener_text
from models import User
from utils.database import connect_to_database, db
from dotenv import load_dotenv

from utils.settings import ADMIN_USERNAME, ADMIN_TGID

load_dotenv(".env")

connect_to_database(db)
db.drop_tables([User])
db.create_tables([User])
for tg_id, tg_username in zip(ADMIN_TGID, ADMIN_USERNAME):
    User.create(tg_id=tg_id, tg_username=tg_username, is_admin=True)

print(generate_listener_text())


while 1:
    sleep(0.2)