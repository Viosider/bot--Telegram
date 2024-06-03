import telebot
import serial

bot = telebot.TeleBot('6470785825:AAGq0v2yZZ0OCBH8FJgID5FIfQ68MByMAFc')

arduino = serial.Serial('COM3', 9600)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, "Ласкаво просимо! Відправте '1' щоб увімкнути LED, '0' щоб вимкнути LED.")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == '1':
        arduino.write(b'1')
        bot.reply_to(message, "Світло увімкнено")
    elif message.text == '0':
        arduino.write(b'0')
        bot.reply_to(message, "Світло вимкнено")
    else:
        bot.reply_to(message, "Невідома команда. Відправте '1' щоб увімкнути LED, '0' щоб вимкнути LED.")


bot.infinity_polling()
