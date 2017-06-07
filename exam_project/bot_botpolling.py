#этот код создаёт бота, умеющего генерировать случайные предложения на основе корпуса
# -*- coding: utf-8 -*-

import re
from random import uniform
from collections import defaultdict
import telebot
import conf

bot = telebot.TeleBot(conf.TOKEN, threaded=False)

r_alphabet = re.compile(u'[а-яА-Я0-9-]+|[.,:;?!]+')

def gen_lines(corpus):
    data = open(corpus, encoding = 'utf-8')
    for line in data:
        yield line.lower()

def gen_tokens(lines):
    for line in lines:
        for token in r_alphabet.findall(line):
            yield token

def gen_trigrams(tokens):
    t0, t1 = '$', '$'
    for t2 in tokens:
        yield t0, t1, t2
        if t2 in '.!?':
            yield t1, t2, '$'
            yield t2, '$','$'
            t0, t1 = '$', '$'
        else:
            t0, t1 = t1, t2

def train(corpus):
    lines = gen_lines(corpus)
    tokens = gen_tokens(lines)
    trigrams = gen_trigrams(tokens)

    bi, tri = defaultdict(lambda: 0.0), defaultdict(lambda: 0.0)

    for t0, t1, t2 in trigrams:
        bi[t0, t1] += 1
        tri[t0, t1, t2] += 1

    model = {}
    for (t0, t1, t2), freq in tri.items():
        if (t0, t1) in model:
            model[t0, t1].append((t2, freq/bi[t0, t1]))
        else:
            model[t0, t1] = [(t2, freq/bi[t0, t1])]
    return model

def generate_sentence(model):
    phrase = ''
    t0, t1 = '$', '$'
    while 1:
        t0, t1 = t1, unirand(model[t0, t1])
        if t1 == '$': break
        if t1 in ('.!?,;:') or t0 == '$':
            phrase += t1
        else:
            phrase += ' ' + t1
    return phrase.capitalize()

def unirand(seq):
    sum_, freq_ = 0, 0
    for item, freq in seq:
        sum_ += freq
    rnd = uniform(0, sum_)
    for token, freq in seq:
        freq_ += freq
        if rnd < freq_:
            return token

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Здравствуйте! Я бот, начитавшийся русских субтитров к сериалу ONCE UPON A TIME")

@bot.message_handler(func=lambda m: True)
def get_answer(message):
    model = train('D:\\OneDrive\\Documents\\2016-2017\\Python16-17\\exam_project\\corpus.txt')
    sent = generate_sentence(model)
    bot.send_message(message.chat.id, sent)


if __name__ == '__main__':
    bot.polling(none_stop=True)
