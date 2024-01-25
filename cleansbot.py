import re

import telebot
from telebot import types

bot = telebot.TeleBot('6004814124:AAFYgMnvQahB1ZNQZTQVzQ2XfQHcsOk-SLI')

bask = []
shoe = []
cost = []
dops = []
dops_cost = []
mess2 = ""
tapok = ""
flag = 0


def clas(message):
    if message.text == "Легкие" or message.text == "Стандартные" or message.text == "Полный уход" \
            or message.text == "🎫Доп услуги:👞" or message.text == "↪️Вернуться в меню":
        print("clas = ", message.text)
        return True


def cros(message):
    if message.text == "Простые" or message.text == "Обычные" or message.text == "Глубокая чистка" \
            or message.text == "🎫Доп услуги:👟" or message.text == "↪️Вернуться в меню":
        print("cros = ", message.text)
        return True


def winter(message):
    if message.text == "Низкая обувь" or message.text == "Средняя обувь" or message.text == "Высокая обувь" \
            or message.text == "🎫Доп услуги:🥾" or message.text == "↪️Вернуться в меню":
        print("winter = ", message.text)
        return True


def premium(message):
    if message.text == "Деликатная чистка" or message.text == "Влагоотводящая пропитка" \
            or message.text == "🎫Доп услуги:👑" or message.text == "↪️Вернуться в меню":
        print("premium = ", message.text)
        return True


def dop(message):
    if message.text == "Дезодорант" or message.text == "Реставрация и покраска" \
            or message.text == "Отбеливание подошвы" or message.text == "↪️Вернуться в меню":
        print("dop = ", message.text)
        return True


@bot.message_handler(commands=['start'])
def start(message):
    a = message.chat.id
    mess = f'Здравствуйте, <b>{message.from_user.first_name} {message.from_user.last_name}</b>!\n' \
           f'Вас приветствует чат-бот компании <b>Cleans</b>!!!\n' \
           f'Для ознакомления с его функционалом нажмите \n' \
           f'/help'
    # print(message.chat.username)
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def user_help(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=4)
    cl_shoe = types.KeyboardButton(text='👞Классическая')
    sp_shoe = types.KeyboardButton(text='👟Кеды и кроссовки')
    wr_shoe = types.KeyboardButton(text='🥾Зимняя')
    premium_shoe = types.KeyboardButton(text='👑Премиальная')
    bak = types.KeyboardButton(text='🛒Корзина')
    delbak = types.KeyboardButton(text='❌Очистить корзину')
    sendbak = types.KeyboardButton(text='📦Оформить заказ')
    markup.add(cl_shoe, sp_shoe, wr_shoe, premium_shoe, bak, sendbak, delbak)
    bot.send_message(message.chat.id, 'Выберите тип обуви', reply_markup=markup)
    get_user_text(message)


# 1
@bot.message_handler(func=clas)
def classik_shoe(message):
    global flag, shoe, cost, tapok
    # ==============================================================================================================
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    clas_easy = types.KeyboardButton(text='Легкие')
    clas_standart = types.KeyboardButton(text='Стандартные')
    clas_full = types.KeyboardButton(text='Полный уход')
    dop = types.KeyboardButton(text='🎫Доп услуги:👞')
    back = types.KeyboardButton(text='↪️Вернуться в меню')
    markup.add(clas_easy, clas_standart, clas_full, dop, back)
    photo = open('/Users/chertova_samsa/PycharmProjects/ProjectBotik/clas.png', 'rb')
    mess = f'<b>ОПИСАНИЕ УСЛУГ:</b>\n ' \
           f"<b>✅Легкие</b> - туфли, макасины, лоферы, стоимость - 2500 руб.\n" \
           f"<b>✅Стандартные</b> - ботинки, полусапоги, стоимость - 3000 руб.\n" \
           f"<b>✅Полный уход</b> - обувь на кожанной подошве, стоимость - +1000 руб. к стоимости заказа\n" \
           f"<b>⏱️Срок выполнения:</b> - 10 дней"
    if flag == 0:
        bot.send_photo(message.chat.id, photo, mess, parse_mode='html', reply_markup=markup)
        # bot.send_message(message.chat.id, mess, parse_mode='html', reply_markup=markup)
        flag += 1
    if message.text == 'Легкие':
        bask.append(message.text)
        cost.append(2500)
        print("bask= ", bask)
        bot.send_message(message.chat.id, "Вы выбрали: " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Стандартные':
        bask.append(message.text)
        cost.append(3000)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Полный уход':
        bask.append(message.text)
        cost.append(1000)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == '🎫Доп услуги:👞':
        tapok = "👞Классическая"
        shoe.pop()
        flag = 0
        dop_usl(message)

    if message.text == '↪️Вернуться в меню':
        user_help(message)
        flag = 0


# 2
@bot.message_handler(func=cros)
def sport_shoe(message):
    global flag, shoe, cost, tapok
    # ==============================================================================================================
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    cross_easy = types.KeyboardButton(text='Простые')
    cross_standart = types.KeyboardButton(text='Обычные')
    cross_full = types.KeyboardButton(text='Глубокая чистка')
    dop = types.KeyboardButton(text='🎫Доп услуги:👟')
    back = types.KeyboardButton(text='↪️Вернуться в меню')
    markup.add(cross_easy, cross_standart, cross_full, dop, back)
    photo = open('/Users/chertova_samsa/PycharmProjects/ProjectBotik/cross.png', 'rb')
    mess = f'<b>ОПИСАНИЕ УСЛУГ:</b>\n ' \
           f"<b>✅Простые</b> - синтетика, сетка, резина - 2000 руб.\n" \
           f"<b>✅Обычные</b> - кожа, замша, нубук, ткань, комбинированные материалы - 2500 руб.\n" \
           f"<b>✅Глубокая чистка</b> - для кроссовок, которые нужно спасать - +500 руб. к стоимости заказа\n" \
           f"<b>⏱️Срок выполнения:</b> - 10 дней"
    if flag == 0:
        bot.send_photo(message.chat.id, photo, mess, parse_mode='html', reply_markup=markup)
        flag += 1
    if message.text == 'Простые':
        bask.append(message.text)
        cost.append(2000)
        bot.send_message(message.chat.id, "Вы выбрали: " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Обычные':
        bask.append(message.text)
        cost.append(2500)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Глубокая чистка':
        bask.append(message.text)
        cost.append(500)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == '🎫Доп услуги:👟':
        tapok = "👟Кеды и кроссовки"
        shoe.pop()
        flag = 0
        dop_usl(message)

    if message.text == '↪️Вернуться в меню':
        user_help(message)
        flag = 0


# 3
@bot.message_handler(func=winter)
def winter_shoe(message):
    global flag, shoe, cost, tapok
    # ==============================================================================================================
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    wint_low = types.KeyboardButton(text='Низкая обувь')
    wint_medium = types.KeyboardButton(text='Средняя обувь')
    wint_high = types.KeyboardButton(text='Высокая обувь')
    dop = types.KeyboardButton(text='🎫Доп услуги:🥾')
    back = types.KeyboardButton(text='↪️Вернуться в меню')
    markup.add(wint_low, wint_medium, wint_high, dop, back)
    photo = open('/Users/chertova_samsa/PycharmProjects/ProjectBotik/winter.png', 'rb')
    mess = f'<b>ОПИСАНИЕ УСЛУГ:</b>\n ' \
           f"<b>✅Низкая обувь</b> - зимняя или демисезонная обувь - 3500 руб.\n" \
           f"<b>✅Средняя обувь</b> - ботинки, полуботинки - 4000 руб.\n" \
           f"<b>✅Высокая обувь</b> - высокая обувь, ботинки/сапоги/ботфорты - 5000 руб.\n" \
           f"<b>⏱️Срок выполнения:</b> - 10 дней"
    if flag == 0:
        bot.send_photo(message.chat.id, photo, mess, parse_mode='html', reply_markup=markup)
        flag += 1
    if message.text == 'Низкая обувь':
        bask.append(message.text)
        cost.append(3500)
        bot.send_message(message.chat.id, "Вы выбрали: " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Средняя обувь':
        bask.append(message.text)
        cost.append(4000)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Высокая обувь':
        bask.append(message.text)
        cost.append(5000)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == '🎫Доп услуги:🥾':
        tapok = "🥾Зимняя"
        shoe.pop()
        flag = 0
        dop_usl(message)

    if message.text == '↪️Вернуться в меню':
        user_help(message)
        flag = 0


# 4
@bot.message_handler(func=premium)
def premium_shoe(message):
    global flag, shoe, cost, tapok
    # ==============================================================================================================
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    prem_delicate = types.KeyboardButton(text='Деликатная чистка')
    prem_propitka = types.KeyboardButton(text='Влагоотводящая пропитка')
    dop = types.KeyboardButton(text='🎫Доп услуги:👑')
    back = types.KeyboardButton(text='↪️Вернуться в меню')
    markup.add(prem_delicate, prem_propitka, dop, back)
    photo = open('/Users/chertova_samsa/PycharmProjects/ProjectBotik/premium.png', 'rb')
    mess = f'<b>ОПИСАНИЕ УСЛУГ:</b>\n ' \
           f"<b>✅Деликатная чистка</b> - Для кроссовок  обуви из люкс-сегмента - 4000 руб.\n" \
           f"<b>✅Влагоотводящая пропитка</b> - Обработка верхней части кроссовка для защиты от грязи, пыли и влаги - " \
           f"500 руб.\n" \
           f"<b>⏱️Срок выполнения:</b> - 7 дней"
    if flag == 0:
        bot.send_photo(message.chat.id, photo, mess, parse_mode='html', reply_markup=markup)
        flag += 1
    if message.text == 'Деликатная чистка':
        bask.append(message.text)
        cost.append(4000)
        bot.send_message(message.chat.id, "Вы выбрали: " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Влагоотводящая пропитка':
        bask.append(message.text)
        cost.append(500)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == '🎫Доп услуги:👑':
        tapok = "👑Премиальная"
        shoe.pop()
        flag = 0
        dop_usl(message)

    if message.text == '↪️Вернуться в меню':
        user_help(message)
        flag = 0


# 5
def order_basket(message):
    global shoe, cost, dops_cost, mess2
    x = 0
    # ==============================================================================================================
    if len(bask) == 0:
        bot.send_message(message.chat.id, "<b>Ваша корзина пуста!</b>", parse_mode='html')
        return
    mess2 = f'<b>В вашей корзине:</b>\n'
    for i in range(len(bask)):
        x += cost[i]
        mess2 += shoe[i] + '\t:\t' + bask[i] + " - " + str(cost[i]) + "руб.\n"
    if dops_cost:
        mess2 += "<b>Дополнительные услуги: \n</b>"
        for i in range(len(dops)):
            x += dops_cost[i]
            mess2 += dops[i] + " - " + str(dops_cost[i]) + "руб.\n"
    mess2 += "<b>Общая стоимость: </b>" + str(x) + "руб."
    bot.send_message(message.chat.id, mess2, parse_mode='html')


# 6
def clear_basket(message):
    global shoe, cost
    # ==============================================================================================================
    bot.send_message(message.chat.id, "<b>Ваша корзина очищена!</b>", parse_mode='html')
    shoe.clear()
    bask.clear()
    cost.clear()
    dops.clear()
    dops_cost.clear()


# 7
def confirm_order(message):
    global flag, shoe, mess2
    # ==============================================================================================================
    print(123)
    if len(bask) == 0:
        bot.send_message(message.chat.id, "<b>Заказ нельзя оформить пока Ваша корзина пуста!</b>",
                         parse_mode='html')
        return
    bot.send_message(461616075, f'Оформленный заказ от <b>{message.from_user.first_name} (@{message.chat.username})'
                                f'{message.from_user.last_name}</b>:\n' + mess2, parse_mode='html')

    bot.send_message(message.chat.id, "<b>Ваша заказ</b> принят в обработку!\n "
                                      "в ближайшее время с Вами свяжется наш менеджер", parse_mode='html')


# 8
@bot.message_handler(func=dop)
def dop_usl(message):
    global flag, shoe, cost, dops, dops_cost, tapok
    print("tapok = " + tapok)
    # ==============================================================================================================
    markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    dop_dez = types.KeyboardButton(text='Дезодорант')
    dop_rest = types.KeyboardButton(text='Реставрация и покраска')
    dop_clean = types.KeyboardButton(text='Отбеливание подошвы')
    back = types.KeyboardButton(text='↪️Вернуться в меню')
    markup1.add(dop_dez, dop_rest, dop_clean, back)
    photo = open('/Users/chertova_samsa/PycharmProjects/ProjectBotik/dop.png', 'rb')
    mess = f'<b>ОПИСАНИЕ УСЛУГ:</b>\n ' \
           f"<b>✅Дезодорант</b> - Обработаем внутреннюю часть кроссовка антибактериальным средством - 400 руб.\n" \
           f"<b>✅Реставрация и покраска</b> - Локальная реставрация и покраска потертостей и царапин - 1500 руб.\n" \
           f"<b>✅Отбеливание подошвы</b> - для кроссовок, которые нужно спасать - 1000 руб. к стоимости заказа\n" \
           f"<b>⏱️Срок выполнения:</b> - 10 дней"
    if flag == 0:
        bot.send_photo(message.chat.id, photo, mess, parse_mode='html', reply_markup=markup1)
        flag += 1
    if message.text == 'Дезодорант':
        dops.append(tapok + "-" + message.text)
        dops_cost.append(400)
        bot.send_message(message.chat.id, "Вы выбрали: " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Реставрация и покраска':
        dops.append(tapok + "-" + message.text)
        dops_cost.append(1500)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == 'Отбеливание подошвы':
        dops.append(tapok + "-" + message.text)
        dops_cost.append(1000)
        bot.send_message(message.chat.id, "Вы выбрали:  " + message.text + ", добавлено в корзину")
        flag = 0
        user_help(message)

    if message.text == '↪️Вернуться в меню':
        user_help(message)
        flag = 0


@bot.message_handler()
def get_user_text(message):
    global flag, shoe
    if message.text == "👞Классическая":
        shoe.append(message.text)
        print("message.text= ", message.text)
        print("shoe= ", shoe)
        print("len(shoe)= ", len(shoe))
        classik_shoe(message)
    if message.text == "👟Кеды и кроссовки":
        shoe.append(message.text)
        print(shoe)
        print(len(shoe))
        sport_shoe(message)
    if message.text == "🥾Зимняя":
        shoe.append(message.text)
        print("message.text= ", message.text)
        print("shoe= ", shoe)
        print("len(shoe)= ", len(shoe))
        winter_shoe(message)
    if message.text == "👑Премиальная":
        shoe.append(message.text)
        print("message.text= ", message.text)
        print("shoe= ", shoe)
        print("len(shoe)= ", len(shoe))
        premium_shoe(message)
    if message.text == "🛒Корзина":
        order_basket(message)
    if message.text == "❌Очистить корзину":
        clear_basket(message)
    if message.text == "📦Оформить заказ":
        confirm_order(message)


bot.polling(none_stop=True)
