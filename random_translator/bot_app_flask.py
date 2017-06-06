##логин бота @don_quijote_bot, он работает на http://donquijote.pythonanywhere.com
##базу лемм для бота делает отдельный код gramrazbs.py (в этой же папке)

import telebot
import conf
import random
import json
import flask
from pymorphy2 import MorphAnalyzer
morph = MorphAnalyzer()

WEBHOOK_URL_BASE = "https://{}:{}".format(conf.WEBHOOK_HOST, conf.WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/{}/".format(conf.TOKEN)

bot = telebot.TeleBot(conf.TOKEN, threaded=False)

bot.remove_webhook()

# ставим новый вебхук = Слышь, если кто мне напишет, стукни сюда — url
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH)

app = flask.Flask(__name__)
def translator (word):
    #try:
        f = open ('home\\donquijote\\mysite\\grams.txt', 'r', encoding = 'utf-8')
        string = f.read()
        grams = json.loads (string)
        ana = morph.parse(word)
        first = ana[0]
        print(first.tag)
        gramm = str(first.tag)
        grammems = []
        if ' ' in gramm:
            grammarr = gramm.split (' ')
            gramrazb = grammarr [-2] #неизменяемые признаки
            gramrazb2 = grammarr [-1] #изменяемые признаки
            if ',' in gramrazb2:
                print (gramrazb2)
                gramrazb2 = gramrazb2.split (',')
                for gr in gramrazb2:
                    grammems.append (gr)
            else:
                grammems.append (gramrazb2)
            print (grammems)
        else:
                gramrazb = gramm
        if gramrazb in grams:
                word2 = random.choice(grams[gramrazb])
                prog = morph.parse(word2)[0]
                print (prog)
                if prog != None:
                        print (grammems)
                        for i in grammems:
                            if prog.tag.POS == 'NPRO':
                                word2 = word
                                print ('!')

                            else:
                                print (i)
                                prog = prog.inflect({i})
                                if prog != None:
                                    print (prog)
                                    word2 = str(prog.word)
                                    print (word2)
                else:
                    print ('что-то не то')
                print (word2)
        else:
            word2 = '(странные у тебя слова какие-то)'
        if 'PREP' in first.tag:
            print ('предлог!')
            word2 = word
##    except:
##        print ('ошибка!!!')
##        word2 = word
        return word2


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Это бот, умеющий переводить русские предложения в полную бессмыслицу, но с сохранением грамматических форм.")

@bot.message_handler(func=lambda m: True)
def get_answer(message):
    sentence = message.text
    sentence = sentence.split (" ")
    sentence_out = ''
    for word in sentence:
        word = translator (word)
        sentence_out = sentence_out + ' ' + word
    bot.send_message(message.chat.id, sentence_out)


# пустая главная страничка для проверки
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return 'ok'


# обрабатываем вызовы вебхука = функция, которая запускается, когда к нам постучался телеграм
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)
    
