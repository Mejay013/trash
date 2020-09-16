import telebot
from pprint import pprint 
import random 

bot = telebot.TeleBot('1094614963:AAH_O1nbEzTYkg8uvW8xDkyfXEYrfNVuix8')

user_messages_list = list()
bot_messages_list= list()

good_answer_list = ['да','конечно','давай','согласен']
unsure_answer_list = ['не знаю','не уверен','может быть','возможно']
bad_answer_list = ['нет','не хочу','отстань']

menu = {"Водка" : '100 gr',
        "Колбаса" : '20 гривень',
        "Пиздюли" : 'бесценно',
        }

@bot.message_handler(commands=['start'])
def start_message(message):
    hello_message = "Добрый день! Приветствую вас в нашем рестаране. Желаете посмотреть меню?"
    bot_messages_list.append(hello_message)
    send_message(message.chat.id,hello_message)


def send_message(chat_id,message: str):
    bot.send_message(chat_id, message)
    bot_messages_list.append(message)

def rand_hot_menu():
    menu_for_rand = []
    for i in menu.keys():
        menu_for_rand.append(i)
    return menu_for_rand[random.randint(0,len(menu.keys())-1)]

@bot.message_handler(content_types=['text'])
def send_text(message):
    print(message.text)
    chat_id = message.chat.id
    user_message = message.text.lower()
    user_messages_list.append(user_message)

    for i in menu:
        if i.lower() in user_message:
            send_message(chat_id,f"Отличный выбор! Наша {i} самая вкусная! У нас особый рецепт на это блюдо!")

    for i in unsure_answer_list:
        if i.lower() in user_message:
            if 'Наше меню' in bot_messages_list[-1]:
                menu_for_rand = []
                for i in menu.keys():
                    menu_for_rand.append(i)
                send_message(chat_id,f' Попробуйте {rand_hot_menu()}, сегодня оно особенно вкусное')

    if user_message in good_answer_list:
        if 'меню' in bot_messages_list[-1]:
            sending_menu = ''
            for key,value in menu.items():
                sending_menu += f'{key}  -  {value} \n'
            send_message(chat_id,'\t Наше меню \n \n' + sending_menu )
    
    elif user_message in bad_answer_list:
        if 'меню' in bot_messages_list[-1]:
            menu_for_rand = []
            for i in menu.keys():
                menu_for_rand.append(i)
            send_message(chat_id,f'Хотите что-то конкретное?, сегодня у нас особенное блюдо - { rand_hot_menu()}! ')







bot.polling()