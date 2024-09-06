from models.users import *
from utils.database import db

db.create_tables([User])
