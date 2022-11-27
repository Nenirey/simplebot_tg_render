from flask import Flask, request
import os
import telebot
from telebot import types, util

TOKEN = os.environ.get('TOKEN')
WEBHOOK = os.environ.get('RENDER_EXTERNAL_URL')+'/'

bot = telebot.TeleBot(token=TOKEN, skip_pending=False)
server = Flask(__name__)

@bot.message_handler(commands=['help','Help','HELP','hELP'])
def send_welcome(message):
    bot.reply_to(message, 'This is a simplebot_tg helper')

@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url=WEBHOOK + TOKEN, allowed_updates=util.update_types, drop_pending_updates = False)
    return "!", 200
       
server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 10000)))

