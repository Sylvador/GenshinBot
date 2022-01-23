import asyncio
import genshinstats as gs
from genshinstats.hoyolab import get_record_card
from datetime import timedelta, datetime
from telebot.async_telebot import AsyncTeleBot
from db.dbcrud import *
from dotenv import load_dotenv
import os
import response_text

load_dotenv()

bot = AsyncTeleBot(os.getenv("API_KEY"))

#Получение инфы о смоле
async def get_resin_info(user_id):
    try:
        cookies = await get_ltuid_and_ltoken(user_id)
        gs.set_cookie(ltuid=cookies[0], ltoken=cookies[1])
        record_card = get_record_card(cookies[0])
        uid = record_card['game_role_id']
        notes = gs.get_notes(uid)
        return {'resin': notes['resin'], 'max_resin': notes['max_resin'], 'until_resin_limit':str(timedelta(seconds=int(notes['until_resin_limit'])))}
    except:
        await bot.send_message(user_id, getattr(response_text, await get_lang(user_id)).database_error_message)

#Отправка инфы о смоле пользователю
async def send_resin_info(user_id):
    task = asyncio.create_task(get_resin_info(user_id))
    resin_info = await task
    task1 = asyncio.create_task(bot.send_message(user_id, f"Current resin: {resin_info['resin']}/{resin_info['max_resin']}\nTime until resin limit: {resin_info['until_resin_limit']}"))

#Проверка не осталось ли до заполнения смолы меньше часа. Если да, то отправить пользователю предупреждение
async def reminder_on(user_id):
    await reminder_switch(user_id, 1)
    while User.get(User.chat_id==user_id).reminder:
        info = await get_resin_info(user_id)
        t = datetime.strptime(info['until_resin_limit'], "%H:%M:%S")
        t = timedelta(hours=t.hour,minutes=t.minute,seconds=t.second)
        if t < timedelta(seconds=3600):
            return info['until_resin_limit']
        await asyncio.sleep(1800)

#Выключение напоминалки
async def reminder_off(user_id):
    await reminder_switch(user_id, 0)

#Включение уведомлений о количестве смолы по таймеру
async def timer_on(user_id):
    await timer_switch(user_id, 1)
    while User.get(User.chat_id==user_id).timer:
        await send_resin_info(user_id)
        await asyncio.sleep(1800)

#Выключение таймера
async def timer_off(user_id):
    await timer_switch(user_id, 0)