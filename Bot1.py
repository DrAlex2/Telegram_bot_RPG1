import random

import telebot
from telebot import types

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

# Основные переменные
hp = max_hp = damage = exp = 0
race = ""
level = 1
victim = None


# Выход в главное меню
def main_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Начать игру")
    button2 = types.KeyboardButton("Об игре...")
    markup.add(button1, button2)
    bot.send_message(
        message.chat.id, "Вы вернулись в главное меню",
        reply_markup=markup
    )


# Функция для старта игры
def start_game(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Человек")
    button2 = types.KeyboardButton("Эльф")
    button3 = types.KeyboardButton("Гном")
    markup.add(button1, button2, button3)
    bot.send_message(
        message.chat.id,
        "Перед путешествием выберите расу",
        reply_markup=markup
    )


# Функция информации об игре
def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("В главное меню")
    markup.add(button1)
    bot.send_message(message.chat.id,
                     "В данной игре вы будете путешествовать по миру, который населен разными монстрами. \n"
                     "Убивая их, вы будете повышать свой уровень, а так же получать с них медикаменты, которые лечат вас, и оружие, которое увеличивает ваш урон. \n"
                     "Но не спешите радоваться, так как с повышением вашего уровня монстры тоже будут становиться сильнее. \n",
                     reply_markup=markup
                     )


#Создание монстра
def create_enemy():
    monsters = ["Орк", "Вампир", "Разбойник", "Скелет", "Троль"]
    monster_name = random.choice(monsters)
    monster_hp = random.randint(120, 170)
    monster_damage = random.randint(30, 50)
    return [monster_name, monster_hp, monster_damage]

#Запуск квеста
def start_quest():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("В путь")
    button2 = types.KeyboardButton("В главное меню")
    markup.add(button1, button2)
    return markup

#Действия после атаки монстра
def what_do():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Атаковать")
    button2 = types.KeyboardButton("Тактическое отступление")
    button3 = types.KeyboardButton("В главное меню")
    markup.add(button1, button2, button3)
    return markup

# Начальное меню
@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Начать игру")
    button2 = types.KeyboardButton("Об игре...")
    markup.add(button1, button2)
    bot.send_message(
        message.chat.id, "Здравствуйте, вы очутились в мире \"85-ded\" \n"
                         "Этот мир полон опасностей. Готовы ли вы начать свое путешествие?",
        reply_markup=markup
    )

# Информация о боте
@bot.message_handler(commands=["help"])
def help(message):
    bot.send_message(message.chat.id, "Информация о боте: \n"
                                      "Данный бот предназначен для игры \"Название\"."
                     )


@bot.message_handler(content_types=["text"])
def answer(message):
    global hp, max_hp, damage, exp, race, level, victim
    if message.text == "Начать игру":
        hp = damage = exp = 0
        race = ""
        level = 1
        start_game(message)

    elif message.text == "Об игре...":
        info(message)

    elif message.text == "В главное меню":
        hp = damage = exp = 0
        race = ""
        level = 1
        main_menu(message)

    if message.text == "Эльф":
        hp = damage = exp = 0
        race = ""
        level = 1
        hp += 100
        damage += 40
        race = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Лучник")
        button2 = types.KeyboardButton("Рыцарь")
        button3 = types.KeyboardButton("Охотник")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id,
                         f"Вы выбрали {race}а. \n"
                         f"Ваше здоровье -> {hp}\n"
                         f"Ваш урон -> {damage}\n"
                         f" \n"
                         f"Осталось выбрать класс...",
                         reply_markup=markup
                         )

    if message.text == "Человек":
        hp = damage = exp = 0
        race = ""
        level = 1
        hp += 120
        damage += 35
        race = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Лучник")
        button2 = types.KeyboardButton("Рыцарь")
        button3 = types.KeyboardButton("Охотник")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id,
                         f"Вы выбрали {race}а. \n"
                         f"Ваше здоровье -> {hp}\n"
                         f"Ваш урон -> {damage}\n"
                         f" \n"
                         f"Осталось выбрать класс...",
                         reply_markup=markup
                         )

    if message.text == "Гном":
        hp = damage = exp = 0
        race = ""
        level = 1
        hp += 160
        damage += 20
        race = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Лучник")
        button2 = types.KeyboardButton("Рыцарь")
        button3 = types.KeyboardButton("Охотник")
        markup.add(button1, button2, button3)
        bot.send_message(message.chat.id,
                         f"Вы выбрали {race}а. \n"
                         f"Ваше здоровье -> {hp}\n"
                         f"Ваш урон -> {damage}\n"
                         f" \n"
                         f"Осталось выбрать класс...",
                         reply_markup=markup
                         )

    if message.text == "Лучник":
        hp += 10
        damage += 25
        max_hp = hp
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("В путь")
        button2 = types.KeyboardButton("В главное меню")
        markup.add(button1, button2)
        bot.send_message(message.chat.id,
                         f"Теперь вы - {race} {message.text}. \n"
                         f"Ваше здоровье -> {hp}\n"
                         f"Ваш урон -> {damage}\n",
                         reply_markup=markup
                         )

    if message.text == "Рыцарь":
        hp += 20
        damage += 15
        max_hp = hp
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("В путь")
        button2 = types.KeyboardButton("В главное меню")
        markup.add(button1, button2)
        bot.send_message(message.chat.id,
                         f"Теперь вы - {race} {message.text}. \n"
                         f"Ваше здоровье -> {hp}\n"
                         f"Ваш урон -> {damage}\n",
                         reply_markup=markup
                         )

    if message.text == "Охотник":
        hp += 15
        damage += 20
        max_hp = hp
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("В путь")
        button2 = types.KeyboardButton("В главное меню")
        markup.add(button1, button2)
        bot.send_message(message.chat.id,
                         f"Теперь вы - {race} {message.text}. \n"
                         f"Ваше здоровье -> {hp}\n"
                         f"Ваш урон -> {damage}\n",
                         reply_markup=markup
                         )

    if message.text == "В путь":
        event = random.randint(0, 2)
        if event == 0 or event == 1:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("В путь")
            button2 = types.KeyboardButton("В главное меню")
            markup.add(button1, button2)
            bot.send_message(message.chat.id,
                             "Вы никого не встретили, идем дальше?",
                             reply_markup=markup)
        elif event == 2:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            button1 = types.KeyboardButton("Атаковать")
            button2 = types.KeyboardButton("Тактическое отступление")
            button3 = types.KeyboardButton("В главное меню")
            markup.add(button1, button2, button3)
            victim = create_enemy()
            bot.send_message(message.chat.id,
                             f"Вы встретили монстра.\n"
                             f"Его характеристики:\n"
                             f"Имя: {victim[0]}\n"
                             f"Здоровье: {victim[1]}\n"
                             f"Урон: {victim[2]}\n"
                             f"Ваши действия?",
                             reply_markup=markup)
    if message.text == "Атаковать":
        victim[1] -= damage
        bot.send_message(message.chat.id, f"Вы нанесли врагу урон: {damage}")
        if victim[1] <= 0:
            bot.send_message(message.chat.id, f"{victim[0]} был повержен.\n")
            random_exp = random.randint(20, 36)
            exp += random_exp * level
            if exp >= 100 * level:
                level += 1
                damage += 5 * level
                max_hp += 10 * level
                hp = max_hp
                exp = 0
                bot.send_message(message.chat.id, f'Твой уровень повышен!\n'
                         f'Теперь у тебя {level} уровень!\n'
                         f'Твоё здоровье -> {hp}\n'
                         f'Твой урон -> {damage} \n'
                         f'Для следующего уровня требуется {100 * level} опыта! \n',
                         reply_markup=start_quest())
            else:
                bot.send_message(message.chat.id, f"Ты получаешь {random_exp * level} очков опыта!\n"
                         f"Твой опыт: {exp}.\n"
                         f"Твоё здоровье -> {hp}\n"
                         f"Твой урон -> {damage} \n"
                         f"Продолжаем путешествие?",
                         reply_markup=start_quest())

        elif victim[1] > 0:
            bot.send_message(message.chat.id, f"Вас атаковал {victim[0]}, нанеся {victim[2]} урона")
            hp -= victim[2]
            if hp <= 0:
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                button1 = types.KeyboardButton("В главное меню")
                markup.add(button1)
                bot.send_message(message.chat.id, f"Вы были поверженны врагом {victim[0]}", reply_markup=markup)
            elif hp > 0:
                bot.send_message(message.chat.id, f"Здоровье монстра: {victim[1]}\n"
                                                  f"Ваше здоровь: {hp}\n"
                                                  f"Что предпримите дальше?", reply_markup=what_do())

    elif message.text == "Тактическое отступление":
        bot.send_message(message.chat.id,
                         "Вы тактически отступили. Что предпримите дальше?",
                         reply_markup=start_quest())




bot.polling(none_stop=True)

# @bot.message_handler(content_types=["text"])
# def repeat(message):
#     bot.send_message(message.chat.id, message.text)
#
#
# @bot.message_handler(content_types=["photo"])
# def img(message):
#     file_id = message.photo[-1].file_id
#     print(file_id)
#     file_info = bot.get_file(file_id)
#     print(file_info)
#     download_file = bot.download_file(file_info.file_path)
#     with open("image", "wb") as new_file:
#         new_file.write(download_file)
#         photo = open("image", "rb")
#         bot.send_photo(message.chat.id, photo)
#         photo.close()
#         remove("image")
