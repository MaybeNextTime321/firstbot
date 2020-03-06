# -*- coding: utf-8 -*-
import this_week
import next_week
import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['now'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе  
    bot.send_message(message.chat.id, str(this_week.week))
@bot.message_handler(commands=['next'])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе  
    bot.send_message(message.chat.id, str(next_week.week))
if __name__ == '__main__':
     bot.infinity_polling()
