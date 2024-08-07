import telebot

bot = telebot.TeleBot('7066735780:AAHuU_EszUrn1XrxOLNSfOXjnAi4grZXHQM')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, какое задание тебе не понятно?', parse_mode='Markdown')

@bot.message_handler(func=lambda message: '1' in message.text)
def help_1(message):
    bot.send_message(message.chat.id, 'https://youtu.be/12iVWZrc-rs?si=JTjB5-kSqgfQTYX6')

@bot.message_handler(func=lambda message: '2' in message.text)
def help_2(message):
    bot.send_message(message.chat.id, "https://www.youtube.com/live/SUzyjMsLhcI?si=kdKD59QknQrfcthx")

@bot.message_handler(func=lambda message: '3' in message.text)
def help_3(message):
    bot.send_message(message.chat.id, "https://youtu.be/KAiydlFeoHY?si=-b2LpU0xR-pNGsO1")

bot.infinity_polling()
