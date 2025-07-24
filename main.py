import telebot
import time
import threading
from flask import Flask

# Replace with your actual Telegram bot token from BotFather
TOKEN = "7612668714: AAE00igNpcb_UCXRtjB
t14vrEKdeOXNCrw"
bot = telebot.TeleBot(TOKEN)

# Flask server to keep Replit running
app = Flask(__name__)


@app.route('/')
def home():
    return "Bot is running!"


# Game signup links (replace with actual links)
aviator_link = "https://1weaou.life/?open=register&p=tebq"
luckyjet_link = "https://1weaou.life/?open=register&p=tebq"

# Different promo images for each game (replace with actual image URLs)
aviator_promo_image = "https://imgur.com/a/vaJwOa6"
luckyjet_promo_image = "https://imgur.com/a/5twyJLU"

channel_link = "https://t.me/tips4winner"  # Replace with your Telegram channel link


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
@bot.message_handler(
    func=lambda message: message.text in ["1️⃣ Aviator", "2️⃣ Lucky Jet"])
def game_selection(message):
    if message.text == "1️⃣ Aviator":
        game_name = "Aviator"
        signup_link = aviator_link
        promo_image = aviator_promo_image  # Use Aviator promo image
    else:
        game_name = "Lucky Jet"
        signup_link = luckyjet_link
        promo_image = luckyjet_promo_image  # Use Lucky Jet promo image

    bot.send_photo(
        message.chat.id,
        promo_image,
        caption=f"🔥 Welcome to {game_name} bot🔥\n\n"
        "Follow these steps to sign up:\n"
        f"1. Click the link: {signup_link}\n"
        "2. Register and create an account\n"
        "3. Start playing and earning!\n\n"
        "⚠️ Terms and Conditions:\n"
        "- Make new id on this website(must new).\n"
        "- No old id use to get A.I bot.\n"
        "- If you have old id on this website please dont use. first make new .\n"
        "- After new id add 300 to start. after this within 3-4 minutes you get bot link."
    )

    # Schedule automatic message after 70 seconds
    threading.Thread(target=send_followup, args=(message.chat.id, )).start()


# Send follow-up message after 50 seconds
def send_followup(chat_id):
    time.sleep(50)
    bot.send_message(
        chat_id, f"Join this channel for A.I signals! HACKS {channel_link}")


# Run bot in a separate thread
def run_bot():
    bot.polling(none_stop=True)


threading.Thread(target=run_bot).start()

# Start bot and Flask server
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=8080)
