from .models import *

#Проверить есть ли пользователь в базе банных
async def isindb(id):
    with db:
        return True if User.get_or_none(User.chat_id==id) is not None else False

#Добавить username и chat.id пользователя
async def save_user(message):
    with db:
        User.create(username=message.chat.username, chat_id=message.chat.id, lang=message.from_user.language_code)

#Обновить ltuid пользователя
async def update_ltuid(id, ltuid):
    with db:
        User.update(ltuid=ltuid).where(User.chat_id==id).execute()

#Обновить ltoken пользователя
async def update_ltoken(id, ltoken):
    with db:
        User.update(ltoken=ltoken).where(User.chat_id==id).execute()

#Переключить таймер
async def timer_switch(id: int, switch: bool):
    with db:
        User.update(timer=switch).where(User.chat_id==id).execute()

#Переключить напоминалку
async def reminder_switch(id: int, switch: bool):
    with db:
        User.update(reminder=switch).where(User.chat_id==id).execute()

#Получить ltuid и ltoken
async def get_ltuid_and_ltoken(id):
    with db:
        res = User.get(User.chat_id==id)
        return (res.ltuid, res.ltoken)

#Получить язык пользователя
async def get_lang(id):
    with db:
        if User.get(User.chat_id==id).lang == 'ru':
            return 'ru'
        else: return 'en'

#Сменить язык пользователя
async def change_lang(id, lang):
    with db:
        User.update(lang=lang).where(User.chat_id==id).execute()