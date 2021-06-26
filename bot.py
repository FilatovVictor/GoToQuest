import telebot
from telebot import types
import time
import json

token = "1844870300:AAEH12SWpLnZP3Mlfl87Mnc9r2rngT2CrYg"
bot = telebot.TeleBot(token)
def togo2(message):
    user = message.chat.id
    bot.send_message(user, "Ты сильно напуган")
    time.sleep(2)
    bot.send_message(user, "Нужно бежать.....")
    time.sleep(2)
    bot.send_message(user, "Ты начинаешь бежать и....падаешь")
    time.sleep(2)
    bot.send_message(user, "И тут ты просыпаешься и понимаешь, что это был всего лишь сон.....")
    time.sleep(2)
    bot.send_message(user, "Если вы это читаете, то это значит, что вы завершили наш тест, и мы очень рады, что он не оказался таким бесполезным")
def togo1(message):
    user = message.chat.id
    bot.send_message(user, "Звучит как странный, дешёвый розыгрыш...")
    time.sleep(2)
    bot.send_message(user, "Вы возвращаетесь в комнату к началу пары.")
    time.sleep(2)
    bot.send_message(user, "Спустя некоторое время, вы понимаете, что никто не возвращается в аудиторию.")
    time.sleep(2)
    bot.send_message(user, "Очень странно...")
    time.sleep(2)
    bot.send_message(user, "Вы решаете выйти и поискать их на территории.")
    time.sleep(2)
    bot.send_message(user, "Вы выходите из учебки и направляетесь в сторону жилих домиков.")
    time.sleep(2)
    bot.send_message(user, "По непонятной причине в домах никого нет...")
    time.sleep(2)
    bot.send_message(user, "Вы паникуете.")
    time.sleep(2)
    bot.send_message(user, "Спустя полтора часа...")
    time.sleep(2)
    bot.send_message(user, "Отчаившись в своих поисках вы идёте в столовую.")
    time.sleep(2)
    bot.send_message(user, "Подходя к столовой, вы слышите разговоры людей внутри")
    time.sleep(2)
    bot.send_message(user, "В замешательстве, вы заходите внутрь, и обнаруживаете, что все преподаватели и ученики находятся здесь.")
    time.sleep(2)
    bot.send_message(user, "Вы садитесь за стол со своими товарищами, бурно обсуждающими свои дела.")
    time.sleep(2)
    bot.send_message(user, "На выходе из столовой вы замечаете, что у одного из преподавателей из кармана выпала бумажка.")
    msg = bot.send_message(user,"Вам нужно найти эту бумажку и написать слово боту")
    bot.register_next_step_handler(msg, check_cipher2)


def check_cipher2(message):
    user = message.chat.id

    if message.text == "У тебя минута.Беги!":
        togo2(message)
    else:
        msg = bot.send_message(user, "Нее")
        bot.register_next_step_handler(msg, check_cipher2)

def togo(message):
    user = message.chat.id
    bot.send_message(user,"Судя по часам завтрак уже начался, соответственно нужно направляться в столовую для первого приёма пищи")
    time.sleep(2)
    bot.send_message(user,"Зайдя в помещение столовой вы моете руки и садитесь за свой стол за которым уже сидят другие участники лагеря.")
    time.sleep(2)
    bot.send_message(user, "Позавтракав вы возвращаетесь в свою комнату забрать ноутбук.")
    time.sleep(2)
    bot.send_message(user, "**10:00, 12 учебка, КМБ 1.5, Первая пара**")
    time.sleep(2)
    bot.send_message(user, "Вы сидите на 1-ой паре КМБ 1.5 у Тимофея")
    time.sleep(2)
    bot.send_message(user, "На паре вам рассказывают про библиотеки Pillow")
    time.sleep(2)
    bot.send_message(user, "Через полтора часа вы выходите на перерыв.")
    time.sleep(2)
    bot.send_message(user,"Все решают выйти через дверь на улицу и разойтись по своим делам, но вы выходите на балкон учебки.")
    time.sleep(2)
    bot.send_message(user, "И тут вы замечаете бумажку, лежащую в углу балкона....")
    time.sleep(2)
    msg = bot.send_message(user, "Вам нужно расшифровать послание, которое находится на балконе 12 учебки. Для этого воспользуйтесь гугл переводчиком, выставив функцию ОПРЕДЕЛИТЬ ЯЗЫК")
    bot.register_next_step_handler(msg, check_cipher1)


def check_cipher1(message):
    user = message.chat.id

    if message.text == "Это просто фантазия, симуляция реального мира":
        togo1(message)
    else:
        msg = bot.send_message(user, "Нее")
        bot.register_next_step_handler(msg, check_cipher1)


@bot.message_handler(commands=['id'])
def get_id(message):
    bot.send_message(message.chat.id, "Ваш ID - {}".format(message.chat.id))


@bot.message_handler(commands=['start'])
def start(message):
    user = message.chat.id

    try:
        USERS = json.load(open('USERS.json'))
    except:
        USERS = []

    if user not in USERS:
        bot.send_message(user, "Чтобы приобрести доступ к игре, скажите @VictorFilatov ваш ID, узнать его можно через команду /id. Для перезапуска - /start.")
        return
    time.sleep(2)
    bot.send_message(user, "Яркий свет ударил в Ваши глаза, а уши пронзила громкая музыка.")
    time.sleep(2)
    bot.send_message(user, "Вы проснулись в комнате лагеря GoTo с двумя другими ребятами.")
    time.sleep(2)
    bot.send_message(user, "Вожатый заходит в Вашу комнату, дабы убедиться, что все уже встали.")
    time.sleep(2)
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    # добавляем на нее две кнопки
    button1 = types.KeyboardButton(text="Нужно пойти, это же полезно.")
    button2 = types.KeyboardButton(text="Да ну, можно же полежать.")
    keyboard.add(button1)
    keyboard.add(button2)
    # отправляем сообщение пользователю
    msg = bot.send_message(message.chat.id,"Вы встали, оделись, умылись и оказались перед выбором: идти или не идти на зарядку?",reply_markup=keyboard)
    bot.register_next_step_handler(msg, answer1)


def answer1(message):
    user = message.chat.id
    if message.text == "Да ну, можно же полежать.":
        bot.send_message(user, "К вам зашел вожатый и ещё раз попросил прийти на зарядку - всё-таки прийдется идти.")

    msg = bot.send_message(user,"Вам нужно расшифровать послание, которое записано на ёлке, которая находится между 10 и 11 домиками. Для этого нужно перейти по ссылке http://base64.ru/, расшифровать сообщение и ввести его в ответном письме")
    bot.register_next_step_handler(msg, check_cipher)


def check_cipher(message):
    user = message.chat.id

    if message.text == "Run away from this place!":
        togo(message)
    else:
        msg = bot.send_message(user, "Нее")
        bot.register_next_step_handler(msg, check_cipher)


bot.polling(none_stop=True)
