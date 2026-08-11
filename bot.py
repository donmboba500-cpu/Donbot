from flask import Flask
from threading import Thread
import os
import telebot

# 1. KEEP ALIVE POUR RENDER
app = Flask('')

@app.route('/')
def home():
    return "DonBot is alive"

def run():
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. TON BOT TELEGRAM
TOKEN = "COLLE_TON_TOKEN_ICI"  # Va sur @BotFather et copie ton token ici
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Salut! DonBot est en ligne 🚀")

@bot.message_handler(commands=['signal'])
def send_signal(message):
    bot.reply_to(message, "📊 SIGNAL BTC: ACHAT à 60000$ \nTP: 61000$ \nSL: 59500$")

# 3. LANCEMENT
keep_alive()  # Garde Render en vie
bot.polling()
