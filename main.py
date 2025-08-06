import telebot
import time
import threading
from flask import Flask
import os
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

bot = telebot.TeleBot(TOKEN)

app = Flask(__name__)

@app.route('/')
def home():
    return "Bot is running!"

# Game signup links
aviator_link = "https://1weaou.life/?open=register&p=tebq"
luckyjet_link = "https://1weaou.life/?open=register&p=tebq"

# Promo images
aviator_promo_image = "https://imgur.com/a/vaJwOa6"
luckyjet_promo_image = "https://imgur.com/a/5twyJLU"

channel_link = "https://t.me/tips4winner"

# /start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    aviator_button = telebot.types.KeyboardButton("1️⃣ Aviator")
    luckyjet_button = telebot.types.KeyboardButton("2️⃣ Lucky Jet")
    markup.add(aviator_button, luckyjet_button)

    bot.send_message(
        message.chat.id,
        "Which game do you want to play now?",
        reply_markup=markup
    )

# Game selection handler
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
        caption=f"🔥 Welcome to {game_name} bot 🔥\n\n"
                "Follow these steps to sign up:\n"
                f"1. Click the link: {signup_link}\n"
                "2. Register and create an account\n"
                "3. ADD 300 RUPEES AND MESSAGE ME ON @Aviatorboss7!\n\n"
    )

    # Schedule automatic follow-up message
    threading.Thread(target=send_followup, args=(message.chat.id,)).start()

# Follow-up message
def send_followup(chat_id):
    time.sleep(50)
    bot.send_message(
        chat_id,
        f"Join this for cracked BOT version APK FILE {channel_link}"
    )

# Start bot polling
def run_bot():
    bot.infinity_polling()

# Start both Flask and bot when running
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
