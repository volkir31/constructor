import telebot
    
token = '213'
bot = telebot.TeleBot(token=token)
    

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, " Hello, thanks for starting me")
    

@bot.message_handler(content_types=['text'])
def text_response(message):
    
    if message.text.upper() == 'hello'.upper():
        bot.send_message(message.from_user.id, 'hi')
    if message.text.upper() == 'hi'.upper():
        bot.send_message(message.from_user.id, 'hello')

    
bot.polling(none_stop=True, interval=0)
