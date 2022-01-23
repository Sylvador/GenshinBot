from peewee import *

db = SqliteDatabase('../dbs/GenshinBotDB/users.db')

class User(Model):
    id = PrimaryKeyField(unique=True)
    username = CharField()
    ltuid = IntegerField()
    ltoken = CharField()
    timer = BooleanField(default=False)
    reminder = BooleanField(default=False)
    chat_id = IntegerField()
    lang = CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'users'
