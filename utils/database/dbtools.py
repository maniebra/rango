# This file is used to initiate the tools and databases that are used in the project

from peewee import *
from utils.settings import DATABASE


def initiate_database():
    if DATABASE['ENGINE'] == 'postgresql':
        return PostgresqlDatabase(
            DATABASE['NAME'], user=DATABASE['USER'],
            password=DATABASE['PASSWORD'], host=DATABASE['HOST'],
            port=DATABASE['PORT'])

    elif DATABASE['ENGINE'] == 'mysql':
        return MySQLDatabase(
            DATABASE['NAME'], user=DATABASE['USER'],
            password=DATABASE['PASSWORD'], host=DATABASE['HOST'],
            port=DATABASE['PORT'])

    else:
        raise ValueError('Database engine not supported or invalid!')


def connect_to_database(db: Database):
    db = initiate_database()
    db.connect()
    return db

def close_database_connection(db: Database):
    db.close()
    return db
