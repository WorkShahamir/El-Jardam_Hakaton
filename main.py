import telebot

bot = telebot.TeleBot(token='6674258422:AAGkOtubs5sJP2YIr6Nl5BU4idbTKScsd74')


@bot.message_handler(commands=['start'])
def start(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(telebot.types.KeyboardButton('Задать вопрос'))
    keyboard.add(telebot.types.KeyboardButton('Записаться на прием'))
    keyboard.add(telebot.types.KeyboardButton('Голосование'))
    bot.send_message(message.chat.id, 'Привет! Вот что я могу сделать:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Задать вопрос')
def ask_question(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(telebot.types.KeyboardButton('Как получить паспорт'))
    keyboard.add(telebot.types.KeyboardButton('Как оформить жилье'))
    keyboard.add(telebot.types.KeyboardButton('Как застраховать машину'))
    keyboard.add(telebot.types.KeyboardButton('Назад'))
    bot.send_message(message.chat.id, 'Какой вопрос вы хотите задать?', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'Как получить паспорт')
def get_passport(message):
    bot.send_message(message.chat.id, 'Для получения паспорта вам необходимо:')
    bot.send_message(message.chat.id, '1. Подать заявление в отделение ФМС')
    bot.send_message(message.chat.id, '2. Предоставить документы, подтверждающие вашу личность и гражданство')
    bot.send_message(message.chat.id, '3. Оплатить госпошлину')


@bot.message_handler(func=lambda message: message.text == 'Как оформить жилье')
def get_housing(message):
    bot.send_message(message.chat.id, 'Для оформления жилья вам необходимо:')
    bot.send_message(message.chat.id, '1. Найти подходящее жилье')
    bot.send_message(message.chat.id, '2. Договориться с собственником о цене и условиях аренды')
    bot.send_message(message.chat.id, '3. Заключить договор аренды')


@bot.message_handler(func=lambda message: message.text == 'Как застраховать машину')
def get_insurance(message):
    bot.send_message(message.chat.id, 'Для страхования машины вам необходимо:')
    bot.send_message(message.chat.id, '1. Обратиться в страховую компанию')
    bot.send_message(message.chat.id, '2. Оформить договор страхования')
    bot.send_message(message.chat.id, '3. Оплатить страховую премию')


@bot.message_handler(func=lambda message: message.text == 'Записаться на прием')
def book_appointment(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    # Добавьте свободные записи и дни
    keyboard.add(telebot.types.KeyboardButton('12.09.2023, 10:00'))
    keyboard.add(telebot.types.KeyboardButton('12.09.2023, 11:00'))
    keyboard.add(telebot.types.KeyboardButton('12.09.2023, 12:00'))
    keyboard.add(telebot.types.KeyboardButton('Назад'))
    bot.send_message(message.chat.id, 'Выберите день и время приема:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text in ['12.09.2023, 10:00', '12.09.2023, 11:00', '12.09.2023, 12:00'])
def confirm_appointment(message):
    # Сохраните запись
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    bot.send_message(message.chat.id, 'Запись на прием успешно создана!')
    keyboard.add(telebot.types.KeyboardButton('Назад'))


@bot.message_handler(func=lambda message: message.text == 'Голосование')
def voting(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(telebot.types.KeyboardButton('Да'))
    keyboard.add(telebot.types.KeyboardButton('Нет'))
    keyboard.add(telebot.types.KeyboardButton('Назад'))
    bot.send_message(message.chat.id, 'Хотите поддержать предмент патриотизма в школах?', reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text in ['Да', 'Нет'])
def vote(message):
    # Сохраните ответ пользователя
    answer = message.text
    # Отправьте сообщение об успешной отправке голоса
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(telebot.types.KeyboardButton('Назад'))
    bot.send_message(message.chat.id, 'Спасибо за ваш голос!')


@bot.message_handler(func=lambda message: message.text == 'Назад')
def back(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=2)
    keyboard.add(telebot.types.KeyboardButton('Задать вопрос'))
    keyboard.add(telebot.types.KeyboardButton('Записаться на прием'))
    keyboard.add(telebot.types.KeyboardButton('Голосование'))
    bot.send_message(message.chat.id, 'Вы вернулись в начало', reply_markup=keyboard)


bot.polling(none_stop=True)
