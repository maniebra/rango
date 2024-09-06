from peewee import *
from utils.database import db


class User(Model):
    tg_username = CharField(max_length=50)
    is_admin = BooleanField(constraints=[SQL('DEFAULT FALSE')], unique=True)
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    updated_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db

