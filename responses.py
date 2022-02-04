from funcs import *

#Приветствие новых пользователей
@bot.message_handler(commands=['start'])
async def start(message):
    if not await isindb(message.chat.id):
        await save_user(message)
    await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).start_message)

#Отправить пользователю данные для связи со мной
@bot.message_handler(commands=['contact'])
async def start(message):
    await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).contact_message)

#Обновить ltuid пользователя
@bot.message_handler(commands=['ltuid'])
async def ltuid(message):
    content = message.text.split()
    if len(content) > 1:
        await update_ltuid(message.chat.id, content[1])
        await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).ltuid_message)
    else:
        await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).error_message)

#Обновить ltoken пользователя
@bot.message_handler(commands=['ltoken'])
async def ltoken(message):
    content = message.text.split()
    if len(content) > 1:
        await update_ltoken(message.chat.id, content[1])
        await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).ltoken_message)
    else:
        await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).error_message)
        
#Получение инфы о смоле
@bot.message_handler(commands=['resin'])
async def get_text(message):
    await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).resin_message)
    await send_resin_info(message.chat.id)

#Включить таймер
@bot.message_handler(commands=['starttimer'])
async def timer_message(message):
    await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).starttimer_message)
    await timer_on(message.chat.id)

#Выключить таймер
@bot.message_handler(commands=['stoptimer'])
async def timer_stop(message):
    await timer_off(message.chat.id)
    task = asyncio.create_task(bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).stoptimer_message))

#Включить напоминалку
@bot.message_handler(commands=['reminderon'])
async def reminder(message):
    await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).reminderon_message)
    task = asyncio.create_task(reminder_on(message.chat.id))
    time_left = await task
    await bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).reminder_message + time_left+'!')

#Выключить напоминалку
@bot.message_handler(commands=['reminderoff'])
async def timer_stop(message):
    await reminder_off(message.chat.id)
    task = asyncio.create_task(bot.send_message(message.chat.id, getattr(response_text, await get_lang(message.chat.id)).reminderoff_message))