import Telebot

bot = telebot.Telebot('6777841195:AAHITPyMYgYI5baFPImB0mzDekDprr0GKcw')

@bot.message_handler(commands == ['start'])
def start(message):
    bot.send.message(message.chat.id, f'привет,{message.from_user.first_name}{message.from_user.last_name}')


@bot.message_handlare(commands == ['help'])
def start(message):
    bot.send.message(message.chat.id,'help informathion:'
                                     'Телеграм-боты — это мини-программы внутри мессенджера, которые управляются текстовыми командами в чате по принципу «вопрос — ответ».'
                                     'Подобная технология была еще в «Аське» конца нулевых: боты присылали анекдоты, гороскопы, статьи из «Википедии» и переводили тексты.'
                                      'Если же у вас не работает бот=>есть 2 варианта '
                                     '1-вы сломали бот и вам нужно перезапустить его'
                                     '2-бот завис и вам стоит перезапустить его (если же это тоже не работает то обратитесь в администарайию )'
                                     'если вам помогла эта информацтя то поставте нам лайк 👍 на аакаунте ютуб'
                                     'https://www.youtube.com/@tehnikum.school')