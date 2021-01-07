def make_conditions(response, request):
    condition = f'''
    if message.text.upper() == '{request}'.upper():
        bot.send_message(message.from_user.id, '{response}')'''
    return condition


def text_response(res, req):
    conditions = ''
    for i in range(len(req)):
        conditions += make_conditions(res[i].strip(), req[i].strip())

    body = f"""

@bot.message_handler(content_types=['text'])
def text_response(message):
    {conditions}

    """
    return body


def start_message(message):
    greetings = f'''
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "{message}")
    '''
    return greetings


def get_start(token):
    start = f'''import telebot
    
token = '{token}'
bot = telebot.TeleBot(token=token)
    
'''
    return start


end = '''
bot.polling(none_stop=True, interval=0)
'''
text_res = []


def bot_creating(res, req, token, file_name):
    with open('src/Instructions Example.txt', 'r') as instructions:
        with open('src/bots/'+file_name+'.py', 'w+') as f:
            for line in instructions:
                if line.split()[0] == 'token':
                    token = token
                elif line.split()[0] == 'start':
                    f.write(get_start(token))
                elif line.split()[0] == 'start_message':
                    f.write(start_message(line.strip().split('start_message')[1]))
                elif line.split()[0] == 'text_response':
                    text_res.append((line.split('\"\"')[1], line.split('\"\"')[3]))
                elif line.split()[0] == 'end':
                    pass
            f.write(text_response(res, req))
            f.write(end)
