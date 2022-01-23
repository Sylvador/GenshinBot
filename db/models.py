from peewee import *

db = SqliteDatabase('db/users.db')

class User(Model):
    id = PrimaryKeyField(unique=True)
    username = CharField()
    ltuid = IntegerField()
    ltoken = CharField()
    timer = BooleanField(default=False)
    resin_check = BooleanField(default=False)
    chat_id = IntegerField()
    lang = CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'users'
