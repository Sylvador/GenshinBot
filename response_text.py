class ru:
    start_message = '''Приветствую тебя, путешественник!
Паймон будет твоим лучшим проводником! Я буду стараться изо всех сил.

Чтобы я тебе смогла помочь, скажи мне свой ltuid и ltoken.
Для этого Паймон подготовила для тебя инструкцию.

*Вы раскрываете свиток, который Вам передала Паймон*:
1. Путешественник, ты должен быть залогинен в сообществе HoyoLab в твоём браузере
2. Нужно нажать кнопку F12, далее, нажать на стрелочку сверху и выбрать вкладку Applicaion. Затем, нажать на Cookies. В них ты должен быть на вкладке hoyolab.
3. Ищем в табличке колонку "Name". Нам нужно найти ltoken и ltuid. Напротив этих значений в колонке "Value" копируем и отправляем коды в чат. Выглядеть это должно таким образом, в 2 сообщения:

/ltoken fefDFSFfDMC902feFMENBC90734433
/ltuid 11111111
4. Используй команду "/resin" для отображения смолы на твоем аккаунте в данный момент

Если команда "/resin" не работает, проверь правильность отправленных ltuid и ltoken!

Еще больше команд:
1. "/reminderon" - напоминает о заполнении смолы до максимума, если до этого осталось меньше часа
2. "/starttimer" - запустить таймер, по которому я буду тебя уведомлять о количестве смолы на данный момент
3. "/stoptimer" - остановить таймер "starttimer"'''

    ltoken_message = "ltoken сохранён"

    ltuid_message = "ltuid сохранён"

    resin_message = "Проверяю смолу..."

    reminderon_message = "Напоминалка включена"

    reminderoff_message = "Напоминалка выключена"

    reminder_message = "Твоя смола заполнится через "

    starttimer_message = "Таймер включен"

    stoptimer_message = "Таймер выключен"

    error_message = "Что-то пошло не так!"

    database_error_message = "Не удалось получить данные о смоле. Убедись, что ты ввел правильные ltuid и ltoken"

class en:
    start_message = '''Greetings traveler!
Paimon will be your best guide! I'll try my best.

So that I can help you, tell me your ltuid and ltoken.
To do this, Paimon has prepared instructions for you.

*You open the scroll Paimon gave you*:
1. Traveler, you must be logged into the HoyoLab community in your browser
2. You need to press the F12 button, then click on the arrow on top and select the Application tab. Then, click on Cookies. In them you should be on the hoyolab tab.
3. We are looking for the column "Name" in the plate. We need to find ltoken and ltuid. Opposite these values ​​in the "Value" column, copy and send the codes to the chat. It should look like this, in 2 messages:

/ltoken fefDFSFfDMC902feFMENBC90734433
/ltuid 11111111
4. Use the command "/resin" to display the resin on your account at the moment

If the "/resin" command doesn't work, check if the ltuid and ltoken sent are correct!

Even more commands:
1. "/reminderon" - reminds you if your resin is about to cap, when it's less than an hour is left before it does
2. "/starttimer" - start a timer, by which I will notify you about the amount of resin at the moment
3. "/stoptimer" - stop the timer "starttimer"'''

    ltoken_message = "ltoken saved"

    ltuid_message = "ltuid saved"

    resin_message = "Checking resin..."

    reminder_message = "Your resin will cap in "

    reminderon_message = "Reminder on"

    reminderoff_message = "Reminder off"

    starttimer_message = "Timer on"

    stoptimer_message = "Timer off"

    error_message = "Something went wrong!"

    database_error_message = "Failed to get resin data. Please make sure you entered the correct ltuid and ltoken"
