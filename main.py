import telebot
from telebot import types
import reply

TOKEN = "6101196560:AAE9Te6XfIfldcJcqdnh6Yb7SHPVi_z3hR"

bot = telebot.TeleBot(TOKEN)

# Command handlers
@bot.message_handler(commands=['start'])
def start(message):
    reply_text = "Hello! I'm your bot. How can I assist you?"
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['help'])
def help(message):
    reply_text = "You can use the following commands:\n" \
                 "/start - Start the bot\n" \
                 "/help - Get help\n" \
                 "/info - Get information\n" \
                 "/status - Get status\n" \
                 "/weather - Get weather\n" \
                 "/time - Get current time\n" \
                 "/date - Get current date"
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['info'])
def info(message):
    reply_text = "This is a bot that can provide various information. How can I assist you?"
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['status'])
def status(message):
    reply_text = "The bot is currently running and operational."
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['weather'])
def weather(message):
    reply_text = "The current weather is sunny."
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['time'])
def time(message):
    reply_text = "The current time is 10:00 AM."
    bot.reply_to(message, reply_text)

@bot.message_handler(commands=['date'])
def date(message):
    reply_text = "The current date is May 24, 2023."
    bot.reply_to(message, reply_text)

# Message handler for other commands or questions
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    question = message.text.lower()
    reply_text = reply.question_replies.get(question, "Sorry, I don't have a reply for that.")
    bot.reply_to(message, reply_text)

# Start the bot
bot.polling()
