from distutils.log import info
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, CallbackQueryHandler, ConversationHandler
from datetime import datetime as dt
import csv

import os
print(os.getcwd())

bot_token = '5561873128:AAHMMJjfipo0ehD-MjNmuKKn53My9jRPE8E'

bot = Bot(token=bot_token)
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

VIEW_ALL, SEARCH_KID, GET_ID, GET_INFO = range(4)

variant = 0
id_kid = ''
index = ''
list_kid = []


def start(update, _):
    keyboard = [
        [
            InlineKeyboardButton("Показать полный список воспитанников", callback_data='1')],
            [InlineKeyboardButton("Поиск воспитанника по фамилии", callback_data='2')
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(
        'Добро пожаловать в информационную систему\nнашего небольшого детского сада!', reply_markup=reply_markup)


def button_start(update, context):
    query = update.callback_query
    global variant
    variant = query.data
    query.answer()
    if variant == '1':
        context.bot.send_message(update.effective_chat.id, f'Отправьте любой символ для просмотра списка всех воспитанников')
        
        return VIEW_ALL
    
    elif variant == '2':
        context.bot.send_message(update.effective_chat.id, f'Введите фамилию: ')
        
        return SEARCH_KID


def print_all_kid(update, context):
    
    with open('Seminar_10_data_kids.csv', 'r', encoding='UTF-8') as r_file:
        global list_kid
        file = list(csv.reader(r_file, delimiter=','))
        for row in file:
            context.bot.send_message(update.effective_chat.id, f'{row[1]}. {row[2]} {row[3]}')
            list_kid.append(row[1])
    time = dt.now().strftime('%H:%M')
    with open('log_seminar_10_2.csv', 'a') as file:
        file.write('{};Show the list of pupils;\n'
                        .format(time))
    
    context.bot.send_message(update.effective_chat.id, f'\nВведите номер воспитанника: ')
    
    return GET_ID


def get_id (update, context):
    global index
    global id_kid
    index = update.message.text
    
    time = dt.now().strftime('%H:%M')
    with open('log_seminar_10_2.csv', 'a') as file:
        file.write('{};Search by pupil last name;\n'
                            .format(time))
    
    if index in list_kid:
        with open('Seminar_10_data_kids.csv', 'r', encoding='UTF-8') as r_file:
            file = list(csv.reader(r_file, delimiter=','))
            id_kid = file[int(index)][0]

        context.bot.send_message(update.effective_chat.id, f'\nДля вывода информации о родителях нажмите 1\nДля вывода успеваемости нажмите 2')
    
        return GET_INFO

    else:
        context.bot.send_message(update.effective_chat.id, f'\nВведены некорректные данные!\nСпасибо что воспользовались нашей системой!')
    
        return ConversationHandler.END


def get_info (update, context):
    info = update.message.text
    
    if info == '1':
        with open('Seminar_10_data_parent.csv', 'r', encoding='UTF-8') as r_file:
            file = list(csv.reader(r_file, delimiter=','))
            for row in file:
                if id_kid == row[0]:
                    context.bot.send_message(update.effective_chat.id, f'Фамилия: {row[1]}\nИмя: {row[2]}\nТелефон: {row[3]}\nОписание: {row[4]}')

        time = dt.now().strftime('%H:%M')
        with open('log_seminar_10_2.csv', 'a') as file:
            file.write('{};Print of the pupils parents;\n'
                                .format(time))

    elif info == '2':
        with open('Seminar_10_data_progress.csv', 'r', encoding='UTF-8') as r_file:
            file = list(csv.reader(r_file, delimiter=','))
            for row in file:
                if id_kid == row[0]:
                    context.bot.send_message(update.effective_chat.id, f'{row[1]} {row[2]}')

                    time = dt.now().strftime('%H:%M')
                    with open('log_seminar_10_2.csv', 'a') as file:
                        file.write('{};Print of the pupils parents;\n'
                                            .format(time))

    else:
        context.bot.send_message(update.effective_chat.id, f'\nВведены некорректные данные!')
    context.bot.send_message(update.effective_chat.id, f'\nСпасибо что воспользовались нашей системой!')
    
    return ConversationHandler.END


def find_surname (update, context):
    global list_kid
    count = 0
    surname = update.message.text

    time = dt.now().strftime('%H:%M')
    with open('log_seminar_10_2.csv', 'a') as file:
        file.write('{};Search by pupil last name;\n'
                            .format(time))

    with open('Seminar_10_data_kids.csv', 'r', encoding='UTF-8') as r_file:
        file = list(csv.reader(r_file, delimiter=','))
        for row in file:
            if surname in row[2]:
                context.bot.send_message(update.effective_chat.id, f'{row[1]}. {row[2]} {row[3]}')
                list_kid.append(row[1])
                count = 1
    if count == 0:
        context.bot.send_message(update.effective_chat.id, f'Совпадений не найдено!\nСпасибо что воспользовались нашей системой!')
        
        return ConversationHandler.END

    else:
        context.bot.send_message(update.effective_chat.id, f'\nВведите номер воспитанника: ')

        return GET_ID


def cancel(update, context):
    return ConversationHandler.END


start_handler = CommandHandler('start', start)
button_start_handler = CallbackQueryHandler(button_start)
cancel_handler = CommandHandler('cancel', cancel)
print_all_kid_handler = MessageHandler(Filters.text, print_all_kid)
get_id_handler = MessageHandler(Filters.text, get_id)
get_info_handler = MessageHandler(Filters.text, get_info)
find_surname_handler = MessageHandler(Filters.text, find_surname)


conv_handler = ConversationHandler(
    entry_points=[start_handler, button_start_handler],

    states={
        VIEW_ALL: [print_all_kid_handler],
        SEARCH_KID: [find_surname_handler],
        GET_ID: [get_id_handler],
        GET_INFO: [get_info_handler],
    },

    fallbacks=[cancel_handler]
)

dispatcher.add_handler(conv_handler)

print('Бот запущен')
updater.start_polling()
updater.idle()
print('Бот остановлен')