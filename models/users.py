from peewee import *
from utils.database import db
import utils.settings as settings

class User(Model):
    tg_id = BigIntegerField(unique=True)
    tg_username = CharField(max_length=50, unique=True)
    is_admin = BooleanField(constraints=[SQL('DEFAULT FALSE')])
    is_staff = BooleanField(constraints=[SQL('DEFAULT FALSE')])
    is_active = BooleanField(constraints=[SQL('DEFAULT TRUE')])
    locale = None
    if len(settings.LOCALES) > 1:
        locale = CharField(max_length=5, constraints=[SQL("DEFAULT 'en'")])
    created_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])
    updated_at = DateTimeField(constraints=[SQL('DEFAULT CURRENT_TIMESTAMP')])

    class Meta:
        database = db

