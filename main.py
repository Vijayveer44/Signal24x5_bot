import os
import telebot
import time
import threading
from flask import Flask

# Securely get Telegram bot token from environment variable
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Flask server to keep Replit or Railway app running
app = Flask(_name_)


@app.route('/')
def home():
    return "Bot is running!"


# Game signup links
aviator_link = "https://1weaou.life/?open=register&p=tebq"
luckyjet_link = "https://1weaou.life/?open=register&p=tebq"

# Promo images
aviator_promo_image = "https://imgur.com/a/vaJwOa6"
luckyjet_promo_image = "https://imgur.com/a/5twyJLU"

# Telegram channel
channel_link = "https://t.me/tips4winner"


# Start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    aviator_button = telebot.types.KeyboardButton("1️⃣ Aviator")
    luckyjet_button = telebot.types.KeyboardButton("2️⃣ Lucky Jet")
    markup.add(aviator_button, luckyjet_button)

    bot.send_message(message.chat.id,
                     "Which game do you want to play with (A.I) bot to earn?",
                     reply_markup=markup)


# Handle game selection
@bot.message_handler(func=lambda message: message.text in ["1️⃣ Aviator", "2️⃣ Lucky Jet"])
def game_selection(message):
    if message.text == "1️⃣ Aviator":
        game_name = "Aviator"
        signup_link = aviator_link
        promo_image = aviator_promo_image
    else:
        game_name = "Lucky Jet"
        signup_link = luckyjet_link
        promo_image = luckyjet_promo_image

    bot.send_photo(
        message.chat.id,
        promo_image,
        caption=f"🔥 Welcome to {game_name} bot🔥\n\n"
                "Follow these steps to sign up:\n"
                f"1. Click the link: {signup_link}\n"
                "2. Register and create an account\n"
                "3. Start playing and earning!\n\n"
                "⚠️ Terms and Conditions:\n"
                "- Make new id on this website (must be new).\n"
                "- Do not use old IDs.\n"
                "- Add ₹300 after registration to get the bot link in 3–4 mins."
    )

    # Schedule follow-up message
    threading.Thread(target=send_followup, args=(message.chat.id,)).start()


# Send follow-up message after 50 seconds
def send_followup(chat_id):
    time.sleep(50)
    bot.send_message(chat_id, f"Join this channel for A.I signals! {channel_link}")


# Run bot and Flask server
def run_bot():
    bot.polling(none_stop=True)


if _name_ == "_main_":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8080)
