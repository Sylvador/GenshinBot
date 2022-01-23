import responses

if __name__ == '__main__':
    responses.asyncio.run(responses.bot.polling(none_stop=True, interval=0))