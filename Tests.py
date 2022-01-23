from peewee import *

db = SqliteDatabase("testdb.db")

class Test(Model):
    id = PrimaryKeyField(unique=True)
    test_user = CharField()
    condition = CharField()

    class Meta:
        database = db
        order_by = 'id'
        db_table = 'tests'

with db:
    res = Test.get(Test.condition=='lol')

print(type(res.id))
