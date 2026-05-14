import os
from dotenv import load_dotenv
import telebot

load_dotenv("pyfile/.env")

API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("API_KEY is missing. Add it to pyfile/.env")

bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=["hi"])
def greet_user(message):
    bot.reply_to(message, "How is your day?")


@bot.message_handler(commands=["bot"])
def show_help(message):
    bot.send_message(message.chat.id, "Hi, send /hi")


def main():
    bot.polling()


if __name__ == "__main__":
    main()
